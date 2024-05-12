const attrDataAction = "data-action";

function onItemSavedClick(e) {
  console.log("ran");
  const icon_btn = $(this);

  const itemId = icon_btn.data("item-id");

  const action = icon_btn.attr(attrDataAction);

  if (!action) return;

  const parent = $(this).parent().closest(".saved-item-card");

  icon_btn.attr(attrDataAction, null);

  if (action === "unSave") {
    $.post({
      url: `${baseUrl}/items/${itemId}/save/0`,
      success: function (data, status) {
        parent.remove();
      },
      complete: function (data, status) {
        icon_btn.attr(attrDataAction, "unSave");
      },
    });
  }
}

$(function () {
  $(document).on("click", ".i-btn-save-item", onItemSavedClick);
});
