$(document).ready(function () {
  $("#category-selection input[type=checkbox]").change(function () {
    const currentCheckbox = $(this);

    const siblings = currentCheckbox
      .parents("ul")
      .siblings('input[type="checkbox"]');

    // checks & unchecks parents
    $(siblings).each(function () {
      if (!uncheckParents(currentCheckbox)) {
        $(this).prop("checked", currentCheckbox.prop("checked"));
      }
    });

    // Checks & unchecks all children
    currentCheckbox
      .siblings("ul")
      .find('input[type="checkbox"]')
      .prop("checked", currentCheckbox.prop("checked"));
  });
});

function uncheckParents(checkbox) {
  // if at least one sibling is checked
  // or any of the siblings of the parent is checked
  // no need to uncheck the parent

  console.log();
  return (
    checkbox.closest("li").siblings().children("input:checked").length > 0 ||
    checkbox
      .closest("ul")
      .parents("ul")
      .children("li")
      .children("input:checked").length > 0
  );
}
