function addToCart(_productId) {
  const _button = $(`#${_productId}`);
  const _productName = $(`#${_productId}-name`).val();
  const _productImgUrl = $(`#${_productId}-img-url`).val();
  const _productPrice = $(`#${_productId}-price`).val();
  const _productQuantity = $(`#${_productId}-quantity`).val();

  console.log(`${_productName} ${_productImgUrl} ${_productPrice}`);

  // Run Ajax
  $.ajax({
    url: "/home/add-to-cart",
    data: {
      id: _productId,
      name: _productName,
      img_url: _productImgUrl,
      price: _productPrice,
      quantity: _productQuantity ? _productQuantity : 1,
    },
    dataType: "json",
    beforeSend: function () {
      _button.attr("disabled", true);
    },
    success: function (response) {
      $("#badge-count").text(response.totalitems);
      _button.attr("disabled", false);
    },
  });
}

function displayCartItems() {
  if (localStorage.getItem("cart") !== null) {
    cart = JSON.parse(localStorage.getItem("cart"));
    document.getElementById("cartDropDown").innerHTML = "";
    for (item in cart) {
      const node = document.createElement("a");
      node.classList.add("grid");
      node.classList.add("grid-cols-3");
      node.classList.add("text-white");

      const img = document
        .getElementById("product-" + item)
        .children[0].children[0].cloneNode(true);
      img.classList.add("w-12");

      const price_text = document.getElementById("product-" + item).children[1]
        .innerHTML;

      const price = document.createElement("p");
      price.innerHTML = price_text;

      const quantity = document.createElement("p");
      quantity.innerHTML = cart[item];
      quantity.classList.add("ml-2");

      node.appendChild(img);
      node.appendChild(price);
      node.appendChild(quantity);
      document.getElementById("cartDropDown").appendChild(node);
    }
  }
}

document
  .getElementById("dropbtncart")
  .addEventListener("click", displayCartItems);
