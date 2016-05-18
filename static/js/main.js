

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








