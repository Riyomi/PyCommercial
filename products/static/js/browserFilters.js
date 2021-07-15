$(document).ready(function () {
  persistFormInputs();

  // add event listener to every checkbox
  $("#category-selection input[type=checkbox]").change(function () {
    const checkbox = $(this);
    const parents = getParents(checkbox);

    checkChildren(checkbox);

    // if the checkbox got checked, recursively check all parents
    if (isChecked(checkbox)) {
      $(parents).each(function (_, parent) {
        check(parent);
      });
    } else {
      // if the checkbox got unchecked, only uncheck a parent if none of its children are checked
      $(parents)
        .reverse()
        .each(function (index, parent) {
          // the top category (=category without parents, which will always be the last element in the array) must be handled differently because of the way the HTML is structured
          if (index == parents.length - 1) {
            if (noSiblingsSelectedOfRoot(parent)) {
              uncheck(parent);
            }
          } else if (noSiblingsSelected(checkbox)) {
            uncheck(parent);
          }
        });
    }
  });
});

function getParents(checkbox) {
  return checkbox.parents("ul").siblings('input[type="checkbox"]');
}

function checkChildren(checkbox) {
  checkbox
    .siblings("ul")
    .find('input[type="checkbox"]')
    .prop("checked", checkbox.prop("checked"));
}

function noSiblingsSelected(checkbox) {
  return (
    checkbox.closest("li").siblings().children("input:checked").length == 0
  );
}

function noSiblingsSelectedOfRoot(root) {
  return (
    $(root).siblings("ul").children("li").children("input:checked").length == 0
  );
}

function isChecked(checkbox) {
  return checkbox.prop("checked");
}

function check(checkbox) {
  $(checkbox).prop("checked", true);
}

function uncheck(checkbox) {
  $(checkbox).prop("checked", false);
}

function getUrlVars() {
  var vars = [],
    hash;
  var hashes = window.location.href
    .slice(window.location.href.indexOf("?") + 1)
    .replaceAll("+", " ")
    .split("&");
  for (var i = 0; i < hashes.length; i++) {
    hash = hashes[i].split("=");
    vars[hash[0].replaceAll("%26", "&")] = hash[1];
  }

  return vars;
}

function persistFormInputs() {
  const params = getUrlVars();

  for (const [key, value] of Object.entries(params)) {
    if (value === "on") {
      check(`input[name="${key}"`);
    }
    if (key === "maxPrice") {
      $(`input[name=maxPrice]`).val(value);
    }
  }
}

jQuery.fn.reverse = [].reverse;
