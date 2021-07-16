var slideIndex = 0;
carousel();

function carousel() {
  const x = document.getElementsByClassName("slides");
  for (let i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > x.length) {
    slideIndex = 1;
  }
  x[slideIndex - 1].style.display = "flex";
  setTimeout(carousel, 2000); // Change image every 2 seconds
}
