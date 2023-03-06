$(document).ready(function () {
    $('.d-flex.align-items-center.mb-3.mb-md-0.me-md-auto.text-white.text-decoration-none').click(function (event){
        $('.d-flex.align-items-center.mb-3.mb-md-0.me-md-auto.text-white.text-decoration-none, .d-flex.flex-column.flex-shrink-0.p-0.text-bg-dark, .nav.nav-pills.flex-column.mb-auto').toggleClass('active');
        $('body').toggleClass('lock');
    });
})
$(document).ready(function () {
    $('.friend,.user, .popup-close').click(function (event){
        $('body').toggleClass('lock');
    });
});