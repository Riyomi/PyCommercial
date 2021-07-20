$("#id_number").on("keyup", function () {
  var id_number = $(this).val().split(" ").join("");
  if (id_number.length > 0) {
    id_number = id_number.match(new RegExp(".{1,4}", "g")).join(" ");
  }

  id_number = id_number.substring(0, 19);

  $(this).val(id_number);
});

$("#id_expiry_date").on("keyup", function () {
  var id_expiry_date = $(this).val().split("/").join("");
  if (id_expiry_date.length > 0) {
    id_expiry_date = id_expiry_date.match(new RegExp(".{1,2}", "g")).join("/");
  }

  id_expiry_date = id_expiry_date.substring(0, 5);

  $(this).val(id_expiry_date);
});

$("#id_number, #id_expiry_date, #id_security_code").keypress(function (e) {
  if ((e.which < 48 || e.which > 57) && e.which !== 8 && e.which !== 0) {
    return false;
  }

  return true;
});
