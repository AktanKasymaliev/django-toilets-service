(function () {
    $( document ).ready(function() {
        var createBtn = $('#create')
        createBtn.click(function (e) {
            e.preventDefault()
            var userName = $('#id_username')
            var email = $('#id_email')
            var password = $('#id_password1')
            var register = '/user/register/'
            var reg = {username:userName.val(), email:email.val(), password:password.val()}
            $.post(register, reg, function (d) {
                userName.val('')
                email.val('')
                password.val('')
            })
        })
    })
}) ()