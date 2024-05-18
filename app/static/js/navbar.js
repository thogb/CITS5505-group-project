function onNavbarSearch() {
  const searchText = $("#navbarSearchInput").val();

  applyItemsFilter({
    search_text: searchText,
  });
}

function loadNavbarSearchValue() {
  const urlSearchParams = new URLSearchParams(window.location.search);

  $("#navbarSearchInput").val(urlSearchParams.get("search_text") || "");
}

$(function () {
  $("#btnNavbarSearch").on("click", onNavbarSearch);
  loadNavbarSearchValue();
});
