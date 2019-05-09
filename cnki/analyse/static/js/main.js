jQuery(function ($) {
    'use strict';

    //Responsive Nav
    $('li.dropdown').find('.fa-angle-down').each(function () {
        $(this).on('click', function () {
            if ($(window).width() < 768) {
                $(this).parent().next().slideToggle();
            }
            return false;
        });
    });

    //Fit Vids
    if ($('#video-container').length) {
        $("#video-container").fitVids();
    }

    //Initiat WOW JS
    new WOW().init();

    // portfolio filter
    $(window).load(function () {

        $('.main-slider').addClass('animate-in');
        $('.preloader').remove();
        //End Preloader

        if ($('.masonery_area').length) {
            $('.masonery_area').masonry();//Masonry
        }

        var $portfolio_selectors = $('.portfolio-filter >li>a');
        if ($portfolio_selectors.length) {
            // console.log($portfolio_selectors.length);
            var $portfolio = $('.portfolio-items');
            console.log($portfolio)
            if ($portfolio.isotope({
                    itemSelector: '.portfolio-item',
                    layoutMode: 'fitRows'
                })) {
                console.log('susscess')
            }
            ;

            $portfolio_selectors.on('click', function () {
                $portfolio_selectors.removeClass('active');
                $(this).addClass('active');
                var selector = $(this).attr('data-filter');
                $portfolio.isotope({filter: selector});
                return false;
            });
        }

    });


    $('.timer').each(count);

    function count(options) {
        var $this = $(this);
        options = $.extend({}, options || {}, $this.data('countToOptions') || {});
        $this.countTo(options);
    }

    // Search
    $('.fa-search').on('click', function () {
        $('.field-toggle').fadeToggle(200);
    });

    // Contact form
    var form = $('#main-contact-form');
    form.submit(function (event) {
        event.preventDefault();
        var form_status = $('<div class="form_status"></div>');

        console.log('开始提交');
        $.ajax({
            url: 'http://localhost:8000/cnki/message',
            type: "get",
            dataType: "JSON",
            data: $("#main-contact-form").serialize(),
            success: function (args) {
                console.log('结束提交');

                console.log(args)
                if (args.status == "ok") {
                    form.prepend(form_status.html('<p><i class="fa fa-spinner fa-spin"></i> Email is sending...</p>').fadeIn());

                    form_status.html('<p class="text-success">邮件发送成功，请耐心等待回复</p>').delay(3000).fadeOut();
                } else {
                    form.prepend(form_status.html('<p><i class="fa fa-spinner fa-spin"></i> Email is sending...</p>').fadeIn());

                    form_status.html('<p class="text-success">邮件发送失败，请稍后再试</p>').delay(3000).fadeOut();

                }
            }
        })
    });

    // Progress Bar
    $.each($('div.progress-bar'), function () {
        $(this).css('width', $(this).attr('data-transition') + '%');
    });

    if ($('#gmap').length) {
        var map;

        map = new GMaps({
            el: '#gmap',
            lat: 43.04446,
            lng: -76.130791,
            scrollwheel: false,
            zoom: 16,
            zoomControl: false,
            panControl: false,
            streetViewControl: false,
            mapTypeControl: false,
            overviewMapControl: false,
            clickable: false
        });

        map.addMarker({
            lat: 43.04446,
            lng: -76.130791,
            animation: google.maps.Animation.DROP,
            verticalAlign: 'bottom',
            horizontalAlign: 'center',
            backgroundColor: '#3e8bff',
        });
    }

});