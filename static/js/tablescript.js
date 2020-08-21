$(document).ready(function() {
    $('#myTable').DataTable({
        "paging": false,
        "searching": false,
        "info": false,
        "order": [
            [2, "desc"]
        ]
    });
});