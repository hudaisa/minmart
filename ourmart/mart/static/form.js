$(".form").validate()

$(function(){
      
 
    $('.myForm').validate({
      rules: {
        name: {
          required: true
        },
        email: {
          required: true
        },
        message: {
          required: true
        },
        messages: {
          name: {
            required: 'Please enter your name'
          },
          email: {
            required: 'Please enter your email'
          },
          message: {
            required: 'Please enter your message'
          },
        }
      },
    });

  });  

$(function(){
    $(".review-form").validate({
        rules: {
            name: {
              required: true
            },
            review: {
              required: true
            },
            messages: {
              name: {
                required: 'Please enter your name'
              },
              review: {
                required: 'Please enter your review'
              },
            }
          },
    })
})  


