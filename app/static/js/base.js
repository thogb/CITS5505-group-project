// export const baseUrl = window.location.origin;
const baseUrl = window.location.origin;
const baseApiUrl = baseUrl + "/api";

const htmlBtnLoading = `
<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
`;

function applyItemsFilter(obj) {
  const paramString = window.location.search;
  const urlSearchParams = new URLSearchParams(paramString);

  urlSearchParams.delete("page");
  urlSearchParams.delete("per_page");

  for (const [name, value] of Object.entries(obj)) {
    if (name) {
      if (value === "" || value === undefined || value === null) {
        urlSearchParams.delete(name);
      } else {
        urlSearchParams.set(name, value);
      }
    }
  }

  window.location.href = baseUrl + itemsUrl + "?" + urlSearchParams.toString();
}

// Ajax setup to make all calls JSON
$.ajaxSetup({
  headers: {
    "content-type": "application/json",
  },
});
