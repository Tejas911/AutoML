console.log("working");
document.addEventListener("DOMContentLoaded", function () {
  window.addEventListener("scroll", function () {
    var navbar = document.querySelector(".navbar");
    var scrollPosition = window.scrollY;

    if (scrollPosition > 100) {
      navbar.classList.add("fixed-navbar");
    } else {
      navbar.classList.remove("fixed-navbar");
    }
  });
});

