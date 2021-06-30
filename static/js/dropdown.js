function openMenu(id) {
  document
    .getElementById(id)
    .nextSibling.nextSibling.classList.toggle("hidden");
}

window.onclick = function (event) {
  const targetIsCart = event.target.closest("#dropbtncart");
  const targetIsAccount = event.target.closest("#dropbtn");

  if (targetIsAccount) {
    document.getElementById("cartDropDown").classList.add("hidden");
  } else if (targetIsCart) {
    document.getElementById("accountDropDown").classList.add("hidden");
  } else {
    document.getElementById("cartDropDown").classList.add("hidden");
    document.getElementById("accountDropDown").classList.add("hidden");
  }
};
