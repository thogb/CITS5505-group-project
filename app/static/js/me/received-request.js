function onItemRequestRespondClick(e) {
  const btn = $(this);
  const modal = $("#receivedRequestModal");
  const form = modal.find("form");

  const action = btn.attr("data-action");

  const itemId = modal.attr("data-item-id");
  const itemRequestId = modal.attr("data-item-request-id");

  if (!itemRequestId || !itemId) {
    return;
  }

  const accepted = action === "accept";
  const message = form.find("#message").val();

  const payload = {
    accepted: accepted,
    message: message,
  };

  btn.find(".spinner-border").show();
  btn.find(".btn-text").hide();

  // Send the request to update
  $.post({
    url: `${baseApiUrl}/items/${itemId}/request/${itemRequestId}/respond`,
    data: JSON.stringify(payload),
    success: function (data, status) {
      modal.attr("data-item-request-id", null);
      modal.attr("data-item-id", null);
      modal["modal"]("hide");
      location.reload();
    },
    error: function (data, status) {
      console.log("error");
    },
    complete: function (data, status) {
      btn.find(".spinner-border").hide();
      btn.find(".btn-text").show();
    },
  });
}

function onOpenReceivedRequestModalClick(e) {
  const modal = $("#receivedRequestModal");
  const form = modal.find("form");

  // Clear the from of the reusable modal.
  form.find("#message").val("");

  const itemId = $(this).attr("data-item") ?? null;
  const itemRequestId = $(this).attr("data-item-request-id") ?? null;

  modal.attr("data-item-request-id", itemRequestId);
  modal.attr("data-item-id", itemId);
}

$(function () {
  $(document).on("click", "#btnRejectRequest", onItemRequestRespondClick);
  $(document).on("click", "#btnAcceptRequest", onItemRequestRespondClick);
  $(document).on(
    "click",
    "#btnOpenReceivedRequestModal",
    onOpenReceivedRequestModalClick
  );
});
