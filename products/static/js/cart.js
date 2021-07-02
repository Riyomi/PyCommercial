function addToCart(_productId) {
  const _button = $(`#${_productId}`);
  const _name = $(`#${_productId}-name`).val();
  const _productImgUrl = $(`#${_productId}-img-url`).val();
  const _productPrice = $(`#${_productId}-price`).val();
  const _productQty = $(`#${_productId}-qty`).val();

  // Run Ajax
  $.ajax({
    url: "/home/add-to-cart",
    data: {
      id: _productId,
      name: _name,
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

      if ($(`#cartDropDown > #cart-${_productId}`).length) {
        const qty_span = $(
          `#cartDropDown > #cart-${_productId} > #cart-qty-${_productId}`
        );
        const currentQty = Number(qty_span.text().substring(1));
        qty_span.text(`x${currentQty + 1}`);
      } else {
        $(
          cartItemHTML(_productId, _name, _productImgUrl, _productPrice)
        ).insertBefore("#cart-total");
      }
      $("#cart-total").text(`Total price: $${response.totalprice}`);
      _button.attr("disabled", false);
    },
  });
}

function removeFromCart(_productId) {
  const _button = $(`#${_productId}`);
  const _id = _productId.substring(7);

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
      $(`#cartDropDown > #cart-${_id}`).remove();

      $("#badge-count").text(response.totalitems);
      $("#cart-total").text(`Total price: $${response.totalprice}`);

      _button.attr("disabled", false);
    },
  });
}

function cartItemHTML(id, name, img, price) {
  return `<div id="cart-${id}"  class="grid grid-flow-col auto-cols-max border-t border-b p-2 hover:bg-purple-100">
  <a href="/home/browse/product/${id}" class="grid grid-flow-col auto-cols-max w-40 my-auto">
      <img src="${img}" class="w-16 my-auto"></img>
      <span class="break-words w-24 pl-2 pr-2 my-auto"> ${name} </span>
  </a>
  <span id="cart-qty-${id}" class="w-6 my-auto">x1</span>
  <span class="w-16 font-bold my-auto">$${price}</span>
  <button id="remove-${id}" onclick="removeFromCart(this.id)" class="my-auto inline-flex items-center justify-center w-4 h-4 text-red-500 bg-white hover:text-white hover:bg-red-500 rounded-lg outline-none focus:outline-none">
  X
  </button>
  </div>`;
}
