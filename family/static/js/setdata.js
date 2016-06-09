
$( document ).ready(function() {



            $("#form-setdata").validate({
            rules: {
                name: {
                    required: true,
                    minlength: 2
                     },
                last_name: {
                    required: true,
                    minlength: 5
                     },
                father_name: {
                    required: true,
                    minlength: 5
                     },
                phone_no: {
                    required: true,
                    minlength: 10
                     },
                date_of_birth: {
                    required: true,
                    },
                Address: {
                    required: true,
                    },
                bloodgroup: {
                    required: true,
                    },
                },
            messages:{
                 name: {
                    required: 'Please enter a name',
                    minlength: 'Name is not long enough'
                        },
                 father_name: {
                    required: 'Please enter Father name',
                    minlength: 'Name is not long enough'
                        },

                 last_name: {
                    required: 'Please enter a Last Name',
                    minlength: 'Not long enough'
                        },
                 phone_no: {
                    required: 'Please enter a name',
                    minlength: 'Please Enter Correct Phone No.'
                        },
                 date_of_birth: {
                    required: 'Please enter Date of Birth',
                        },
                 Address: {
                    required: 'Please enter Address',
                        },







                    }




        });




    });
