function addToCart(_productId) {
  const _button = $(`#${_productId}`);
  const _productName = $(`#${_productId}-name`).val();
  const _productImgUrl = $(`#${_productId}-img-url`).val();
  const _productPrice = $(`#${_productId}-price`).val();
  const _productQty = $(`#${_productId}-qty`).val();

  // Run Ajax
  $.ajax({
    url: "/home/add-to-cart",
    data: {
      id: _productId,
      name: _productName,
      img_url: _productImgUrl,
      price: _productPrice,
      qty: _productQty ? _productQty : 1,
    },
    dataType: "json",
    beforeSend: function () {
      _button.attr("disabled", true);
    },
    success: function (response) {
      $("#badge-count").text(response.totalitems);

      if ($(`#cartItems > #cart-${_productId}`).length) {
        const qty_span = $(
          `#cartItems > #cart-${_productId} > #cart-qty-${_productId}`
        );
        const currentQty = Number(qty_span.text().substring(1));
        qty_span.text(`x${currentQty + 1}`);

        const price_span = $(
          `#cartItems > #cart-${_productId} > #cart-price-${_productId}`
        );

        console.log(response);

        price_span.text(`$${response.data[_productId].total}`);
      } else {
        $("#cartItems")
          .last()
          .append(
            cartItemHTML(
              _productId,
              _productName,
              _productImgUrl,
              response.data[_productId].total
            )
          );
      }

      if (response.totalprice) {
        $("#cart-total").text(`Total price: $${response.totalprice}`);
        $("#checkout-btn").removeClass("hidden");
      } else {
        $("#cart-total").text("Your cart is empty.");
      }
      _button.attr("disabled", false);
    },
  });
}

function removeFromCart(_productId) {
  const _button = $(`#${_productId}`);
  var _id;

  if (_productId.indexOf("checkout-") >= 0) {
    _id = _productId.substring(16);
  } else {
    _id = _productId.substring(7);
  }

  // Run Ajax
  $.ajax({
    url: "/home/remove-from-cart",
    data: {
      id: _id,
    },
    dataType: "json",
    beforeSend: function () {
      _button.attr("disabled", true);
    },
    success: function (response) {
      $(`#cartItems > #cart-${_id}`).remove();
      $(`#product-checkout-${_id}`).remove();

      $("#badge-count").text(response.totalitems);
      if (response.totalprice) {
        $("#cart-total").text(`Total price: $${response.totalprice}`);
        $("#checkout-total").text(`Total: $${response.totalprice}`);
      } else {
        $("#cart-total").text("Your cart is empty");
        $("#checkout-btn").addClass("hidden");
        $("<span>Cart is empty.</span>").insertAfter("#checkout-summary");
        $("#checkout-summary").remove();
      }

      _button.attr("disabled", false);
    },
  });
}

function cartItemHTML(id, name, img, price) {
  return `<div id="cart-${id}"  class="cart-item-container">
  <a href="/home/browse/product/${id}" class="grid grid-flow-col auto-cols-max w-40 my-auto">
      <img src="${img}" class="w-16 my-auto"></img>
      <span class="break-words w-24 pl-2 pr-2 my-auto"> ${name} </span>
  </a>
  <span id="cart-qty-${id}" class="w-6 my-auto">x1</span>
  <span id="cart-price-${id}" class="w-16 font-bold my-auto">$${price}</span>
  <button id="remove-${id}" onclick="removeFromCart(this.id)" class="remove-btn">
  X
  </button>
  </div>`;
}

$("body").on("DOMSubtreeModified", "#badge-count", function () {
  const count = $("#badge-count").text();
  if (count === "0" || count === "") {
    $("#badge-count").addClass("hidden");
  } else {
    $("#badge-count").removeClass("hidden");
  }
});
