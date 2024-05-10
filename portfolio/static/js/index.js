axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

$(function () {
    $('#contact-form').on('submit', async (e) => {
        e.preventDefault()

        let name = $('#name').val()
        let email = $('#email').val()
        let contactNumber = $('#contact_number').val()
        let inquiry = $('#inquiry').val()
        let message = $('#message').val()
        const contactData = {
            name: name,
            email: email,
            contactNumber: contactNumber,
            inquiry: inquiry,
            message: message,
        }
        const response = await axios.post('/contact/', contactData)
        if (response.status == 200) {
            swal("Thank you!", "We appreciate your confidence in Koji Ichikawa Hairstylist. We'll be in touch soon!", "success");
            $('#name').val('')
            $('#email').val('')
            $('#contact_number').val('')
            $('#message').val('')
        }
        console.log(response)
    })
})
