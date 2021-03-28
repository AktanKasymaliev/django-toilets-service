(function () {
    $( document ).ready(function(){
        var loginUrl = '/api-auth/login/?next=/api/v1/restroom/create/'
        var userName = $('#id_username')
        var password = $('#id_password')
        var loginBtn = $('.btn')
        loginBtn.click(function (e){
            $.post(
            loginUrl,
            {username: userName.val(), password:password.val()},
            function(data) {
            userName.val('')
            password.val('')
            })
        })
    })
}) ()