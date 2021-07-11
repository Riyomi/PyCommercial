if (window.history.replaceState) {
  window.history.replaceState(null, null, window.location.href);
}

function setRating(id) {
  const rating = Number(id.split("-")[1]);

  $('input[name="rating"]').val(rating);

  for (let i = 1; i <= 5; i++) {
    if (i <= rating) {
      $(`#star-${i}`).addClass("fas");
    } else {
      $(`#star-${i}`).removeClass("fas");
    }
  }
}
