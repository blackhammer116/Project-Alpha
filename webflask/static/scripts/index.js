function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/home";
  });
}

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function deleteTestRequest(requestId) {
  fetch(`/services/delete-test-request/${requestId}`, {
      method: 'POST',
      credentials: 'same-origin',
  })
  .then(response => {
      if (response.status === 204) {
          // Successful deletion, remove the row from the table
          const row = document.getElementById(`test-request-row-${requestId}`);
          row.parentNode.removeChild(row);
      } else if (response.status === 401) {
          // Unauthorized, show an error message (optional)
          alert('Unauthorized to delete this test request.');
      } else {
          // Other error, show an error message (optional)
          alert('Error occurred while deleting the test request.');
      }
  })
  .catch(error => {
      // Fetch error, show an error message (optional)
      alert('Error occurred while deleting the test request.');
  })
}