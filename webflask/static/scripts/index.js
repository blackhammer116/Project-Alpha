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

function filterTable() {
  const input = document.getElementById("searchInput");
  const filter = input.value.toUpperCase();
  const table = document.getElementById("resultsTable");
  const rows = table.getElementsByTagName("tr");

  for (let i = 0; i < rows.length; i++) {
    const tdService = rows[i].getElementsByTagName("td")[0];
    const tdIP = rows[i].getElementsByTagName("td")[1];

    if (tdService || tdIP) {
      const serviceText = tdService.textContent || tdService.innerText;
      const ipText = tdIP.textContent || tdIP.innerText;

      if (serviceText.toUpperCase().indexOf(filter) > -1 || ipText.toUpperCase().indexOf(filter) > -1) {
        rows[i].style.display = "";
      } else {
        rows[i].style.display = "none";
      }
    }
  }
}
document.getElementById("searchInput").addEventListener("keyup", filterTable);
