document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');
    const email = document.getElementById('email');
    const password = document.getElementById('password');

    // Set Google button
    const googleButton = document.createElement('button');
    googleButton.setAttribute('id', 'g_id_signin');
    googleButton.setAttribute('data-clientid', 'YOUR_GOOGLE_CLIENT_ID');
    googleButton.setAttribute('data-theme', 'dark');
    googleButton.setAttribute('data-size', 'large');
    googleButton.setAttribute('data-onsuccess', 'onSignIn');
    googleButton.innerHTML = 'Login with Google';
    document.getElementById('googleButton').appendChild(googleButton);

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();

        // Your login code here
        console.log('Email:', email.value);
        console.log('Password:', password.value);
    });
});

function onSignIn(googleUser) {
    // Your Google sign-in code here
    const profile = googleUser.getBasicProfile();
    console.log('Google User ID:', profile.getId());
    console.log('Google User Name:', profile.getName());
    console.log('Google User Email:', profile.getEmail());
}
// Initialize Firebase
var firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_STORAGE_BUCKET",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

firebase.initializeApp(firebaseConfig);

var loader = document.getElementById('loader');
var loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', function(e) {
    e.preventDefault();

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    loader.classList.remove('hide');

    firebase.auth().signInWithEmailAndPassword(email, password)
        .then(function(result) {
            loader.classList.add('hide');
            window.location.href = 'dashboard.html';
        })
        .catch(function(error) {
            loader.classList.add('hide');
            alert('Error: ' + error.message);
        });
});

