# views.py
from django.shortcuts import render, redirect
from django.conf import settings
import os
import pandas as pd
from .forms import UploadFileForm
from django.views.decorators.http import require_POST


@require_POST
def process_options(request):
    # Retrieve form data
    encoding_method = request.POST.get("encoding_method")
    selected_columns = request.POST.getlist("selected_columns")
    mode = request.POST.get("mode")

    if mode == "Automatic":
        # Redirect to automatic page
        return redirect(
            "automatic_page",
            encoding_method=encoding_method,
            selected_columns=selected_columns,
        )
    elif mode == "Manual":
        # Get additional information for manual mode (e.g., algorithm name)
        algorithm_name = request.POST.get("algorithm_name")
        # Perform actions based on manual mode
        # For example, train the model using selected columns and algorithm name
        # Then, redirect or render a page accordingly
        return render(request, "manual_page.html", {"algorithm_name": algorithm_name})

    # If mode is not selected, redirect back to the form page
    return redirect("success")


def home(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            destination = os.path.join(settings.UPLOADS_DIR, uploaded_file.name)

            with open(destination, "wb+") as destination_file:
                for chunk in uploaded_file.chunks():
                    destination_file.write(chunk)

            try:
                df = pd.read_csv(destination, encoding="utf-8")
                if df.isnull().values.any():
                    os.remove(
                        destination
                    )  # Delete the file if it contains NaN or null values
                    return render(request, "error.html")
                else:
                    # Retrieve column names from the CSV file
                    columns = df.columns.tolist()
                    return render(
                        request,
                        "success.html",
                        {"file": uploaded_file.name, "columns": columns},
                    )
            except pd.errors.ParserError:
                os.remove(destination)  # Delete the file if there's an error parsing it
                return render(request, "error.html")
    else:
        form = UploadFileForm()
    return render(request, "index.html", {"form": form})
