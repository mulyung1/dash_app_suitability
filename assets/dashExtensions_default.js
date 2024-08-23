window.dashExtensions = Object.assign({}, window.dashExtensions, {
    default: {
        function0: function(e, ctx) {
            ctx.setProps({
                data: 'You clicked at Latitude: ' + e.latlng.lat + ', Longitude: ' + e.latlng.lng
            });
        }
    }
});