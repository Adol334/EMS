// ==========================================
// EMS JavaScript File
// Frontend helper functions only
// Backend logic handled by Django + MySQL
// ==========================================


// Confirm logout action
function confirmLogout() {
    return confirm("Are you sure you want to logout?");
}

// Load financial advisory message
function loadAdvisory() {
    const adviceText = document.getElementById("adviceText");

    if (adviceText) {
        adviceText.innerText =
            "Track expenses daily, save at least 15% of income, and avoid unnecessary spending.";
    }
}


// Load job listings dynamically
function loadJobs() {
    const jobsList = document.getElementById("jobsList");
    if (jobsList) {
        const jobs = ["Library Assistant", "Online Freelance Writing", "Campus IT Support", "Data Entry"];
        jobsList.innerHTML = "";
        jobs.forEach(job => {
            const li = document.createElement("li");
            li.className = "list-group-item";
            li.innerText = job;
            jobsList.appendChild(li);
        });
    }
}

// Run code after page loads
document.addEventListener("DOMContentLoaded", function() {
   // Run page-specific functions
    loadAdvisory();
    loadJobs();

    // Toggle between login and register forms
    const loginBox = document.getElementById("login-box");
    const regBox = document.getElementById("register-box");
    const toggleLinks = document.querySelectorAll(".toggle-form");

    // Safety check to prevent errors on other pages
    if (loginBox && regBox) { 
        toggleLinks.forEach(link => {
            link.addEventListener("click", function() {
                const isLoginVisible = loginBox.style.display !== "none";
                loginBox.style.display = isLoginVisible ? "none" : "block";
                regBox.style.display = isLoginVisible ? "block" : "none";
            });
        });
    }

    // Show/hide password help text on focus
    const passwordInput = document.querySelector("#register-box input[type='password']");
    const helpText = document.querySelector("#register-box .helptext");
    
    if (passwordInput && helpText) {
        passwordInput.addEventListener("focus", () => {
            helpText.style.setProperty("display", "block", "important");
        });
        passwordInput.addEventListener("blur", () => {
            if (passwordInput.value === "") {
                helpText.style.setProperty("display", "none", "important");
            }
        });
    }
});