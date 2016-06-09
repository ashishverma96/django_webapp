

$( document ).ready(function() {


        $.validator.addMethod("regex", function(value, element, regexpr) {
                return regexpr.test(value);
           }, "Please enter a valid Username.");

            $("#registration").validate({
            rules: {
                username: {
                    required: true,
                    regex: /((^[0-9]+[a-z])|(^[a-z]+[0-9])|(^[a-z]+[0-9])+ $)/
                    }
             }

        });



    });


function CheckId() {
$.get('/check_username/', {username: $('#username').val()},
    function(data){
        if(data == "True"){
            $('#idval').html("You may use this ID");
        } else {
            $('#idval').html("Unavailable");
        }
});
}
function onChange(){
 $("#username").change( function() {CheckId()});
}





