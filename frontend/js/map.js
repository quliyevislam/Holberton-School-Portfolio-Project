const locations = [
    { lat: 40.406854, lng: 49.848369, title: "Marker 1" },
    { lat: 40.406800, lng: 49.848369, title: "Marker 2" },
    { lat: 40.407000, lng: 49.848500, title: "Marker 3" },
    { lat: 40.407200, lng: 49.848600, title: "Marker 4" },
    { lat: 40.406600, lng: 49.848200, title: "Marker 5" },
    { lat: 40.406900, lng: 49.848100, title: "Marker 6" },
    { lat: 40.407100, lng: 49.848000, title: "Marker 7" },
    { lat: 40.406750, lng: 49.848500, title: "Marker 8" },
    { lat: 40.407050, lng: 49.848300, title: "Marker 9" },
    { lat: 40.407300, lng: 49.848400, title: "Marker 10" },
];

const map = new google.maps.Map(
    document.querySelector('#googleMap'),
    { zoom: 20, center: locations[0] }
);



locations.forEach((location) => {
    new google.maps.Marker({
        position: {
            lat: location.lat,
            lng: location.lng,
        },
        map,
        title: location.title,
    });
});
