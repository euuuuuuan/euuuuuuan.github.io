// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const hamburgerMenu = document.querySelector(".hamburger-menu");
    const menu = document.querySelector(".nav-links");

    hamburgerMenu.addEventListener("click", function() {
        menu.classList.toggle("active");
    });
});
