var baseUrl = window.location.origin;

// Ajax setup to make all calls JSON
$.ajaxSetup({
  headers: {
    "content-type": "application/json",
  },
});
