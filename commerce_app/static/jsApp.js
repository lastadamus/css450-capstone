// Redirect to Registration Page
function redirectToRegistration() {
    window.location.href = '/register';
}
var registerButton = document.getElementById('register');
registerButton.addEventListener('click', redirectToRegistration);

// Redirect to Login Page 
function redirectToLoginPage() {
    window.location.href = '/login'
}
var loginPageButton = document.getElementById('login_page');
registerButton.addEventListener('click', redirectToLoginPage);
