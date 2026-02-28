(function ($) {
$(function () {
    var $for = $('.slider-for');
    var $nav = $('.slider-nav');

    if ($for.length && $nav.length) {
        // Основной слайдер
        $for.slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            arrows: true,
            fade: true,
            asNavFor: '.slider-nav',
            adaptiveHeight: true
        });

        // Навигационный слайдер
        $nav.slick({
            slidesToShow: 5,
            slidesToScroll: 1,
            asNavFor: '.slider-for',
            dots: false,
            centerMode: false,
            focusOnSelect: true,
            variableWidth: false
        });

        // Полноэкранная галерея
        $for.slickLightbox({
            src: function(element) {
                return element.getAttribute('src');
            },
            itemSelector: 'img',
            caption: function(element) {
                return element.getAttribute('alt') || '';
            }
        });
    }
});
})(jQuery);