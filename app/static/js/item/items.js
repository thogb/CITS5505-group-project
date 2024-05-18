// import { baseUrl } from "../base";

const attrDataItemSaved = "data-item-saved";

function onItemSavedClick(e) {
  const icon_btn = $(this);

  // Using data attribute to check if item is saved or not
  const itemSaved = icon_btn.attr(attrDataItemSaved);

  if (!itemSaved) return;

  // Saved then param to unsaved else save
  const param = itemSaved === "true" ? 0 : 1;
  const itemId = icon_btn.data("item-id");

  // Set the action saved to null so button cli ck has no effect
  icon_btn.attr(attrDataItemSaved, null);

  $.post({
    url: `${baseApiUrl}/items/${itemId}/save/${param}`,
    // data: JSON.stringify({ message: "test" }),
    success: function (data, status) {
      if (param) {
        icon_btn.toggleClass("fa-solid");
      } else {
        icon_btn.toggleClass("fa-regular");
      }

      icon_btn.attr(attrDataItemSaved, param ? "true" : "false");
    },
    error: function (data, status) {
      icon_btn.attr(attrDataItemSaved, param ? "false" : "true");
    },
  });
}

function onApplyFilterClick() {
  const category = $("#itemsFilterCategory").val();
  const city = $("#itemsFilterCity").val();
  const minPrice = parseFloat($("#itemsFilterMinPrice").val());
  const maxPrice = parseFloat($("#itemsFilterMaxPrice").val());

  const filterObj = {};

  if (category) {
    filterObj["category"] = category;
  }

  if (city) {
    filterObj["city"] = city;
  }

  if (minPrice) {
    filterObj["min_price"] = minPrice;
  }

  if (maxPrice) {
    filterObj["max_price"] = maxPrice;
  }

  if (minPrice && maxPrice) {
    filterObj["min_price"] = Math.min(minPrice, maxPrice);
    filterObj["max_price"] = Math.max(minPrice, maxPrice);
  }

  applyItemsFilter(filterObj);
}

function onResetFilterClick() {
  window.location.href = baseUrl + itemsUrl;
}

$(function () {
  // $(".i-btn-save-item").on("click", onItemSavedClick);
  // The above solution does not work, when any jquery class modification is
  // called the on click weill be removed
  $(document).on("click", ".i-btn-save-item", onItemSavedClick);
  $(document).on("click", "#btnApplyFilter", onApplyFilterClick);
  $(document).on("click", "#btnResetFilter", onResetFilterClick);
});


