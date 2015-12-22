$("#geoCheck").click(initiate_geolocation);

function initiate_geolocation() {
    navigator.geolocation.getCurrentPosition(handle_geolocation_query);
}

function handle_geolocation_query(position){
    $("#latValue").val(position.coords.latitude);
    $("#longValue").val(position.coords.longitude);
}
