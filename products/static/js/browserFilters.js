$(document).ready(function () {
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

  $("#selected-max-price").text(
    "Max price: $" + $('input[name="maxPrice"]').val()
  );

  $('input[name="maxPrice"]').change(function () {
    $("#selected-max-price").text(
      "Max price: $" + $('input[name="maxPrice"]').val()
    );
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

jQuery.fn.reverse = [].reverse;
