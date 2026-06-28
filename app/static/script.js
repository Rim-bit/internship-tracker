const companyName = document.getElementById("company");
const status = document.getElementById("status");
const addForm = document.getElementById("add-form");

// Validate user input and display message
addForm.addEventListener("submit", function(event) {
    let companyMissing = companyName.value.trim() === "";
    let statusMissing = status.value.trim() === "";
    if (companyMissing || statusMissing) {
        event.preventDefault();

        if (companyMissing) {
            companyName.value = "";
            companyName.placeholder = "Company Required*";
            companyName.classList.add("input-error");
        }
        
        if (statusMissing) {
            status.value = "";
            status.placeholder = "Status Required*";
            status.classList.add("input-error");
        }

        if (companyMissing) {
            companyName.focus();
        }
        else if (statusMissing) {
            status.focus();
        }
    }
});

// Remove error message
companyName.addEventListener("input", function() {
    companyName.placeholder = "Company";
    companyName.classList.remove("input-error");
});