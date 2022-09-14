document.addEventListener("DOMContentLoaded", function () {
 
    const submitForm = document.getElementById("Form");
 
    submitForm.addEventListener("masuk", function (event) {
        event.preventDefault();
        addUser();
    });
});
