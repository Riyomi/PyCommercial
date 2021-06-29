function addToCart(item) {
  if (localStorage.getItem("cart") === null) {
    cart = {};
  } else {
    cart = JSON.parse(localStorage.getItem("cart"));
  }
  if (item in cart) {
    cart[item]++;
  } else {
    cart[item] = 1;
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  countItems();
}

function countItems() {
  if (localStorage.getItem("cart") !== null) {
    var count = 0;
    cart = JSON.parse(localStorage.getItem("cart"));
    Object.keys(cart).forEach((key) => {
      count += cart[key];
    });
    console.log(count);
    document.getElementById("badge-count").innerHTML = count;
    return;
  }
  document.getElementById("badge-count").innerHTML = 0;
}

window.onload = countItems;
