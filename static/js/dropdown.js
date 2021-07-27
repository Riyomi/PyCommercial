$("#mobiledropdown").on("click", function () {
  $("#mobileDropDownMenu").toggleClass("hidden");

  if (!$("#mobileDropDownMenu").hasClass("hidden")) {
    $("#menuIcon").attr("d", "M6 18L18 6M6 6l12 12");
  } else {
    $("#menuIcon").attr("d", "M4 6h16M4 12h16M4 18h16");
  }
});

$("#mobileaccountdropdown").on("click", function () {
  $("#mobileAccountDropDown").toggleClass("hidden");

  if (!$("#mobileAccountDropDown").hasClass("hidden")) {
    $("#accountMenuIcon").attr("d", "M6 18L18 6M6 6l12 12");
  } else {
    $("#accountMenuIcon").attr("d", "M4 6h16M4 12h16M4 18h16");
  }
});

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
