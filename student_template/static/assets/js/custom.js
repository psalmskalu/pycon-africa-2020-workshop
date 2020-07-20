$("#post-form").on("submit", function(e){
    e.preventDefault();

    var spinner = $("#loader");
    spinner.show();
    
    $.ajax({
		
		url: $(this).attr('action'),
        type: "POST",
        
        headers: {
            "X-CSRFToken": csrf_token
        },

		data: new FormData(this),
		
		contentType: false,
		cache: false,
        processData: false,
        dataType:'json',

		success: function(data){

			spinner.hide();
            alert(data.message + ": " + data.prediction +"\n");
			window.location.reload();
			
		},
		error: function(xhr, status, error) {

			spinner.hide();
			//Ajax request failed.
			var errorMessage = xhr.status + ': ' + xhr.statusText;
			alert('Error - ' + errorMessage);
		}
	})
	
});
    