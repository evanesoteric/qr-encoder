// Load QR code
$(document).ready(function() {
    $('#qr-form').submit(function(event) {
        event.preventDefault();

        var csrf_token = "{{ csrf_token() }}";

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
            }
        });

        $.ajax({
            type: 'POST',
            url: '/',
            data: $('#qr-form').serialize(),
            beforeSend: function(){
                // Show image container
                $("#arcaloader").show();
                $("#qr-reload").hide();
                $('#borderpop').css('border', 'unset');
                $('#borderpop').removeClass('animate__animated animate__tada');
            },
            success: function(data) {
                if (data.errors) {
                    $('#result').html('<span id="qr-reload"><p>' + data.errors + '</p></span>');
                    $('#borderpop').css('border', '2px solid #f0506e');
                    $('#borderpop').addClass('animate__animated animate__tada');
                    UIkit.notification({
                     message: 'Error: The URL is not valid!',
                     status: 'danger',
                     timeout: 2000
                    });
                    return;
                }
                $('#result').html('<span id="qr-reload"><p><a href="data.url" target="_blank">' + data.url + '</a><br><img id="picture" src="' + data.qr_code + '"></p></span>');
                $('#borderpop').css('border', '2px solid #32d296');
                $('#borderpop').addClass('animate__animated animate__tada');
                UIkit.notification({
                     message: 'Successfiully generated QR code!',
                     status: 'success',
                     timeout: 2000
                    });
            },
            complete:function(data){
                // Hide image container
                $("#arcaloader").hide();
            }
        });

    });

});




