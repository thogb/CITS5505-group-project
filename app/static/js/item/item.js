function getCommentHtml(
  comment_id,
  first_name,
  last_name,
  comment_description
) {
  return `
        <div class="comment" data-comment-id="${comment_id}">
            <div class="comment-avatar">
                <span>
                    ${first_name[0]}
                </span>
                <span>
                    ${last_name[0]}
                </span>
            </div>
            <div class="comment-content">
                <div>
                    <span class="comment-name">
                        ${first_name} ${last_name}
                    </span>
                    <span class="comment-time text-secondary">
                        Today                 
                    </span>
                </div>
                <p>
                    ${comment_description}
                </p>
                <span class="icon-button-delete" data-action="delete">
                    <i class="fa-solid fa-trash-can"></i>
                </span>
            </div>
        </div>
    `;
}

function onPostCommentClick() {
  const itemCard = $("#itemCard");
  const itemId = itemCard.attr("data-item-id");

  const commentInput = $("#commentInput");

  const commentMessage = commentInput.val();

  if (!commentMessage) return;

  $.post({
    url: `${baseApiUrl}/items/${itemId}/comments`,
    data: JSON.stringify({
      message: commentMessage,
    }),
    success: function (data, status) {
      commentInput.val("");
      console.log(data);
      $("#commentList").prepend(
        getCommentHtml(
          data.id,
          current_user.first_name,
          current_user.last_name,
          data.description
        )
      );
    },
    error: function (data, status) {
      console.log("error");
    },
    complete: function (data, status) {},
  });
}

function onCommentDeleteClick() {
  const thisBtn = $(this);
  const itemCard = $("#itemCard");
  const itemId = itemCard.attr("data-item-id");
  const commentId = thisBtn.closest(".comment").attr("data-comment-id");

  const action = thisBtn.attr("data-action");

  if (action !== "delete") return;

  $.ajax({
    url: `${baseApiUrl}/items/${itemId}/comments/${commentId}`,
    type: "DELETE",
    success: function (data, status) {
      thisBtn.closest(".comment").remove();
    },
    error: function (data, status) {
      thisBtn.attr("data-action", "delete");
      console.log("error");
    },
    complete: function (data, status) {},
  });
}

$(function () {
  $(document).on("click", "#btnPostComment", onPostCommentClick);
  $(document).on("click", ".comment .icon-button-delete", onCommentDeleteClick);
});
