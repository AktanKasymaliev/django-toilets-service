(function () {
    $( document ).ready(function() {
        var createBtn = $('#create')
        var forResetUrl = '/api/v1/restrooms/'
        createBtn.click(function (e) {
            e.preventDefault()
            var userName = $('#id_username')
            var email = $('#id_email')
            var password = $('#id_password1')
            var password2 = $('#id_password2')
            var register = '/user/register/'
            var reg = {username:userName.val(), email:email.val(), password:password.val()}
            $.post(register, reg, headers: {
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
              }, function (d) {
                userName.val('')
                email.val('')
                password.val('')
                password2.val('')
            $.get(forResetUrl, function(data) {
            var restroomsData = data
            restroomsData.forEach(element =>{
            if (element !== "This post didn't verify by moderator") {
              alert('Your account created successfully, please confirm your email for log in')
              var resMarker = L.marker([element.longitude, element.latitude])
              markers.addLayer(resMarker)}
            }, false)
            map.addLayer(markers)
          })
            })
            })
        })
    })
}) ()