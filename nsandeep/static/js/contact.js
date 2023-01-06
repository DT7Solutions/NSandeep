
let contactform = document.querySelector('#contactForm');
let inputs = document.querySelectorAll('input')
let textariea = document.querySelector('textarea')
contactform.addEventListener('submit', function(event){
          event.preventDefault();
          $.ajax({
            type:'POST',
            url:'/',
            data:{
              name:$("#name").val(),
              email:$("#email").val(),
              message:$("#message").val(),
              csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data) {
         
              swal("success", "Your Message was sending successfully ", "success");
            
            },
            error: function(xhr, status, error) {
              swal("error!", "Please Try Agian", "error");
            
            },
            dataType: 'text'
        })
        inputs.forEach(input => input.value = '');
        textariea.value =''
}) 
