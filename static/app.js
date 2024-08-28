$(document).ready(function() {
    // Intercept form submission
    $('#newsForm').submit(function(event) {
        // Prevent default form submission
        event.preventDefault();
        
        // Get the news text from the textarea
        var newsText = $('#newsInput').val();
        
        // Send AJAX POST request to /detect endpoint
        $.ajax({
            type: 'POST',
            url: '/detect',
            data: {'news': newsText},
            success: function(response) {
                // Display the result in the result paragraph
                $('#result').text('Result: ' + response.result);
            },
            error: function(error) {
                // Display error message if request fails
                $('#result').text('Error: ' + error.responseJSON.error);
            }
        });
    });
});
