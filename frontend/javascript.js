$(document).ready(function() {

  var 
  validationRules = {
    email: {
      identifier  : 'email',
      rules: [
        {
            type   : 'empty',
            prompt : 'Please enter your email'
        }
      ]
    },
    password: {
      identifier  : 'password',
      rules: [
        {
            type   : 'empty',
            prompt : 'Please enter your password'
        }
      ]
    }

  }

  $('.ui.form')
    .form(validationRules, {
      on: 'blur'
    })
    ;
  $('.ui.dropdown')
    .dropdown({
      on: 'hover'
    })
  ;

});