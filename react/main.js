document.getElementById("assessment-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent page refresh

    // Collect form data
    const animalType = document.getElementById("animal-type").value;
    const condition = document.getElementById("condition").value;
    const location = document.getElementById("location").value;
    const description = document.getElementById("description").value;
    const photo = document.getElementById("photo").files[0];

    // Validate required fields
    if (!animalType || !condition || !location) {
        alert("Please fill in all required fields.");
        return;
    }

    // Display a confirmation message
    alert("Assessment submitted successfully!");

    // Optional: Reset the form
    this.reset();
});
