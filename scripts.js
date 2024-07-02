// scripts.js
$(document).ready(function() {
    // 네비게이션 바 토글
    $('.navbar-toggler').click(function() {
        $('#navbarNav').toggleClass('show');
    });

    // 부드러운 스크롤링
    $('a.nav-link').click(function(event) {
        if (this.hash !== "") {
            event.preventDefault();
            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 800, function(){
                window.location.hash = hash;
            });
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.querySelector("#navbarNav");

    navbarToggler.addEventListener("click", function() {
        navbarCollapse.classList.toggle("show");
    });
});
