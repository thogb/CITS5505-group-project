function onItemRequestRespondClick(e) {
  const btn = $(this);

  console.log(btn);
}

$(function () {
  $(document).on("click", "#btnRejectRequest", onItemRequestRespondClick);
  $(document).on("click", "#btnAcceptRequest", onItemRequestRespondClick);
});
