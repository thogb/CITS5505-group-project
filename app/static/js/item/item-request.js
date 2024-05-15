function onItemRequestSendClick(e) {
  const sender_amount = $("#item-request-sender-amount").val();
  const sender_message = $("#item-request-sender-message").val();
  const itemId = $(this).data("item-id");

  const itemRequestButton = $(this);
  itemRequestButton.html(htmlBtnLoading);
  $(".btn-item-send-request-modal").prop("disabled", true);

  $.post({
    url: `${baseApiUrl}/items/${itemId}/request`,
    data: JSON.stringify({
      amount: sender_amount,
      message: sender_message,
    }),
    success: function (data, status) {
      $("#item-request-sender-amount").val("");
      $("#item-request-sender-message").val("");
      $(`.btn-item-request[data-item-id=${itemId}]`).prop("disabled", true);
      $("#itemRequestModal")["modal"]("hide");
    },
    error: function (data, status) {},
    complete: function (data, status) {
      itemRequestButton.html("Send Request");
      $(".btn-item-send-request-modal").prop("disabled", false);
    },
  });
}

function onItemRequestModalOpenClick(e) {
  const itemId = $(this).data("item-id");
  $(".btn-item-send-request-modal").data("item-id", itemId);
}

$(function () {
  $(document).on(
    "click",
    ".btn-item-send-request-modal",
    onItemRequestSendClick
  );
  $(document).on("click", ".btn-item-request", onItemRequestModalOpenClick);
});
