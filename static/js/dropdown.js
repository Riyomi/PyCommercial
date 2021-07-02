function openMenu(id) {
  $(`#${id}`).next().toggleClass("hidden");
}

window.onclick = function (event) {
  const targetIsCart = event.target.closest("#dropbtncart");
  const targetIsAccount = event.target.closest("#dropbtn");

  if (targetIsAccount) {
    $("#cartDropDown").addClass("hidden");
  } else if (targetIsCart) {
    $("#accountDropDown").addClass("hidden");
  } else {
    $("#cartDropDown").addClass("hidden");
    $("#accountDropDown").addClass("hidden");
  }
};
