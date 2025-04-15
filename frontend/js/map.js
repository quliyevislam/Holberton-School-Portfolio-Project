// const locations = [
//     { lat: 40.406854, lng: 49.848369, title: "Marker 1" },
//     { lat: 40.406800, lng: 49.848369, title: "Marker 2" },
//     { lat: 40.407000, lng: 49.848500, title: "Marker 3" },
//     { lat: 40.407200, lng: 49.848600, title: "Marker 4" },
//     { lat: 40.406600, lng: 49.848200, title: "Marker 5" },
//     { lat: 40.406900, lng: 49.848100, title: "Marker 6" },
//     { lat: 40.407100, lng: 49.848000, title: "Marker 7" },
//     { lat: 40.406750, lng: 49.848500, title: "Marker 8" },
//     { lat: 40.407050, lng: 49.848300, title: "Marker 9" },
//     { lat: 40.407300, lng: 49.848400, title: "Marker 10" },
// ];

// const map = new google.maps.Map(
//     document.querySelector('#googleMap'),
//     { zoom: 20, center: locations[0] }
// );



// locations.forEach((location) => {
//     new google.maps.Marker({
//         position: {
//             lat: location.lat,
//             lng: location.lng,
//         },
//         map,
//         title: location.title,
//     });
//       // Back to top button
//   const backToTopButton = document.getElementById('backToTop');
  
//   if (backToTopButton) {
//     window.addEventListener('scroll', function() {
//       if (window.pageYOffset > 300) {
//         backToTopButton.classList.add('visible');
//       } else {
//         backToTopButton.classList.remove('visible');
//       }
//     });
    
//     backToTopButton.addEventListener('click', function() {
//       window.scrollTo({
//         top: 0,
//         behavior: 'smooth'
//       });
//     });
//   }
// });

//50.13565215581905
const locations = [
  { lat: 40.412972938873715, lng: 49.89988156345417, title: "Lost Cat", icon: "./assets/images/lost-cat.JPG" },
  { lat: 40.406800, lng: 49.848369, title: "Lost Dog", icon: "./assets/images/lost-dog.JPG" },
  { lat: 40.383768512586435, lng: 49.825310067423686, title: "Veterinar Klinaka (Dr.Xetai)"},
  { lat: 40.4899156735452, lng: 50.13565215581905, title: "Caspian Veterinar Klinıkası"},
  { lat: 40.456012772553, lng: 49.66913248650856, title: "Animal Rescue Center"},
];

const map = new google.maps.Map(
  document.querySelector('#googleMap'),
  { zoom: 11, center: locations[0] }
);

locations.forEach((location) => {
  new google.maps.Marker({
      position: {
          lat: location.lat,
          lng: location.lng,
      },
      map,
      title: location.title,
      icon: {
          url: location.icon, // Use the animal's picture as the marker icon
          scaledSize: new google.maps.Size(50, 50), // Adjust the size of the icon
      },
  });
});

// Back to top button
const backToTopButton = document.getElementById('backToTop');

if (backToTopButton) {
  window.addEventListener('scroll', function() {
      if (window.pageYOffset > 300) {
          backToTopButton.classList.add('visible');
      } else {
          backToTopButton.classList.remove('visible');
      }
  });

  backToTopButton.addEventListener('click', function() {
      window.scrollTo({
          top: 0,
          behavior: 'smooth'
      });
  });
}