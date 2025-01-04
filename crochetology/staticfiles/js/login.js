function toggleForms() {
  const loginForm = document.getElementById("login");
  const signupForm = document.getElementById("signup");
  loginForm.style.display = loginForm.style.display === "none" ? "block" : "none";
  signupForm.style.display = signupForm.style.display === "none" ? "block" : "none";
}

document.getElementById("signup-form").addEventListener("submit", (event) => {
  event.preventDefault();

  const fullname = document.getElementById("fullname").value.trim();
  const username = document.getElementById("user").value.trim();
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();
  const address = document.getElementById("address").value.trim();
  const phone = document.getElementById("phone").value.trim();

  let isValid = true;

  document.getElementById("signup-fullname-error").textContent = "";
  document.getElementById("signup-username-error").textContent = "";
  document.getElementById("signup-email-error").textContent = "";
  document.getElementById("signup-password-error").textContent = "";
  document.getElementById("signup-address-error").textContent = "";
  document.getElementById("signup-phone-error").textContent = "";

  const usernamePattern = /^\w{3,15}$/;
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const phonePattern = /^\d{10,15}$/;

  if (!fullname) {
    document.getElementById("signup-fullname-error").textContent =
      "Full Name is required.";
    isValid = false;
  }

  if (!usernamePattern.test(username)) {
    document.getElementById("signup-username-error").textContent =
      "Username must be 3-15 characters long and contain only letters, numbers, or underscores.";
    isValid = false;
  }

  if (!emailPattern.test(email)) {
    document.getElementById("signup-email-error").textContent =
      "Enter a valid email address.";
    isValid = false;
  }

  if (password.length < 6) {
    document.getElementById("signup-password-error").textContent =
      "Password must be at least 6 characters long.";
    isValid = false;
  }

  if (!address) {
    document.getElementById("signup-address-error").textContent =
      "Address is required.";
    isValid = false;
  }

  if (!phonePattern.test(phone)) {
    document.getElementById("signup-phone-error").textContent =
      "Enter a valid phone number (10-15 digits).";
    isValid = false;
  }

  if (isValid) {
    alert("Signup Successful!");
  }
});

document.getElementById("login-form").addEventListener("submit", (event) => {
  event.preventDefault();

  const username = document.getElementById("user").value.trim();
  const password = document.getElementById("password").value.trim();

  let isValid = true;

  document.getElementById("login-username-error").textContent = "";
  document.getElementById("login-password-error").textContent = "";

  if (!username) {
    document.getElementById("login-username-error").textContent =
      "Username is required.";
    isValid = false;
  }

  if (!password) {
    document.getElementById("login-password-error").textContent =
      "Password is required.";
    isValid = false;
  }

  if (isValid) {
    alert("Login Successful!");
  }
});

function closeForm() {
  document.getElementById("login").style.display = "none";
  document.getElementById("signup").style.display = "none";

  // Get the last page URL from session storage
  const lastPage = sessionStorage.getItem("lastPage");

  // Redirect the page to the last page or home
  window.location.href = lastPage || "index.html";
}
