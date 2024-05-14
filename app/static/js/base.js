// export const baseUrl = window.location.origin;
const baseUrl = window.location.origin;
const baseApiUrl = baseUrl + "/api";

const htmlBtnLoading = `
<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
`;

// Ajax setup to make all calls JSON
$.ajaxSetup({
  headers: {
    "content-type": "application/json",
  },
});
