(function () {
    window.addEventListener("map:init", function (e) {
        var markers = new L.FeatureGroup()
        var detail = e.detail
        var map = detail.map
        // Actuals should be declared as a global var
        actuals.forEach(element => {
          var marker = L.marker([element.fields.longitude, element.fields.latitude])
          markers.addLayer(marker)
        }, false);
        map.addLayer(markers)
        // Search functionality
        var searchBtn = $('#search-btn')
        var searchInput = $('#search-input')
        var resetBtn= $('#reset')
        var url = '/api/v1/restroom/list/?search='
        var forResetUrl = '/api/v1/restrooms/'
        var forResetUrl2 = '/api/v1/restroom/list/'
        resetBtn.click(function (e) {
          e.preventDefault()
          $.get(forResetUrl, function(data) {
            var restroomsData = data
            restroomsData.forEach(element =>{
            if (element !== "This post didn't verify by moderator") {
              var resMarker = L.marker([element.longitude, element.latitude])
              markers.addLayer(resMarker)}
            }, false)
            map.addLayer(markers)
          })
        })


        function clearMapAndAddMarkers (map, mrkrs, data) {
            map.removeLayer(mrkrs)
            var newMarkers = new L.FeatureGroup()
            data.forEach(function(element) {
                // Put coming markers to markers layer 
                var m = L.marker([element.longitude, element.latitude])
                newMarkers.addLayer(m)
            })
            // Put markers layer to map
            map.addLayer(newMarkers)
            return newMarkers
        }

        searchBtn.click(function (e) {
          e.preventDefault()
          var searchVal = searchInput.val()
          var fullUrl = url + searchVal
          $.get(fullUrl, function(data) {
            var res = data?.results
            if (res.length > 0) {
              markers = clearMapAndAddMarkers(map, markers, res)
            } else if (res.length === 0) {
            alert("Sorry, but so restroom didn't find")
            }
          })
        })
        if (isAddPage) {
            var address = $('#address');
            var region = $('#region');
            var lng = $('#lng');
            var lat = $('#lat');
            map.on('click', function(e) {
                var longitude = e.latlng.lng
                var latitude = e.latlng.lat
                lng.val(longitude)
                lat.val(latitude)
            })
            var saveBtn = $('#save-btn')
            var createUrl = '/api/v1/restroom/create/'
            saveBtn.click(function (e) {
                e.preventDefault()
                var data = {address:address.val(), region:region.val(), latitude:lng.val(), longitude:lat.val()}
                $.post(
                    createUrl,
                    data,
                    function(d) {
                        lng.val('')
                        lat.val('')
                        address.val('')
                        region.val('')
                        $.get(forResetUrl2, function(data) {
                            if (data?.length > 0) {
                              markers = clearMapAndAddMarkers(map, markers, data)
                            }
                        })
                    }
                )
            })
        }
      });
}) ()


