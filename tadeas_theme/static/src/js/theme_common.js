$(document).ready(function () {
    $("#testimonial-slider").owlCarousel({
        pagination: false,
        navigation: true,
        navigationText: ["", ""],
        slideSpeed: 1000,
        autoplay: true,
        nav: true,
        responsive: {
            768: {
                items: 2
            },
            979: {
                items: 2
            },
            479: {
                items: 1
            },
            320: {
                items: 1
            },
            1199: {
                items: 3
            },
        },
    });
    var viewportWidth=$(window).width();if($("#nav_top_fix").length){viewportWidth>600&&(window.onscroll=function(){myFunction()});var navbar=document.getElementById("nav_top_fix"),sticky=navbar.offsetTop}function myFunction(){window.pageYOffset>=sticky?(navbar.classList.add("o_header_affix"),navbar.classList.add("affixed"),navbar.classList.add("affix")):(navbar.classList.remove("o_header_affix"),navbar.classList.add("affixed"),navbar.classList.add("affix"))}
});
$(document).ready(function () {
    $("#news-slider").owlCarousel({
        navigation: false,
        pagination: false,
        items: 3,
        itemsDesktop: [1199, 3],
        itemsDesktopSmall: [980, 2],
        itemsMobile: [600, 1]
    });
});