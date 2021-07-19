$("#id_cc_number").on("keyup", function () {
  var cc_number = $(this).val().split(" ").join("");
  if (cc_number.length > 0) {
    cc_number = cc_number.match(new RegExp(".{1,4}", "g")).join(" ");
  }
  $(this).val(cc_number);
});

$("#id_cc_expiry").on("keyup", function () {
  var cc_expiry = $(this).val().split("/").join("");
  if (cc_expiry.length > 0) {
    cc_expiry = cc_expiry.match(new RegExp(".{1,2}", "g")).join("/");
  }
  $(this).val(cc_expiry);
});

$("#id_cc_number, #id_cc_expiry, #id_cc_code").keypress(function (e) {
  if ((e.which < 48 || e.which > 57) && e.which !== 8 && e.which !== 0) {
    return false;
  }

  return true;
});
