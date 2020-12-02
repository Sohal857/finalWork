$(document).ready(function() {
    if (window.location.pathname === '/' || window.location.pathname === '/index.html') {
        // Static slider

        var sliderContainerWidth = parseInt($('#slider').width())
        var leftPosition = parseInt( ( ( sliderContainerWidth  - 200 ) / 2 ) )

        $(".slide-3-1").hide()
        $(".slide-3-2").hide()
        $(".slide-3-1").css({top: 0, left: 0})
        $(".slide-3-2").css({top: 0, left: 0})
        
        $(".slide-1").hide()
        $(".slide-2").hide()
        $(".slide-3").hide()
        firstSlide(leftPosition)
        console.log(leftPosition)

        // Reset slider on size change
        $('#slider').sizeChanged(function() {
            location.reload()
        })

        // Featured product slider
        $("#content-slider").lightSlider({
            item: 1,
            pauseOnHover: true,
            pause: 5000,
            loop: true,
            keyPress: true,
            auto: true,
            slideMargin: 0,
            controls: false
        })
    }
});

// Slide 1
function firstSlide(leftPosition) {
    $(".slide-3-1").hide()
    $(".slide-3-2").hide()
    $(".slide-3-1").css({top: 0, left: 0})
    $(".slide-3-2").css({top: 0, left: 0})
    
    $(".slide-1").hide()
    $(".slide-2").hide()
    $(".slide-3").hide()
    
    $(".slide-1").show("slide", { direction: "left" }, 1000, function() {
        $(".slide-1-1").show().animate({
            "opacity": 1,
            "width": "200px",
            "height": "200px",
            "top": "80px", 
            "left": leftPosition+"px"}, 1500, "swing", function() {
                $(".slide-1-2").show().animate({"width": "200px",
                "height": "200px",
                "top": "80px", 
                "left": leftPosition+"px"}, 500, "swing").animateRotate(360, {
                    duration: 1500,
                    easing: 'linear',
                    complete: function() {
                        setTimeout(function() {
                            secondSlide(leftPosition)
                        }, 2500)
                    },
                    setp: function() {}
                })
            })
        })
}

// Slide 2
function secondSlide(leftPosition) {
    $(".slide-1-1").hide()
    $(".slide-1-2").hide()
    $(".slide-1-1").css({top: 0, left: 0})
    $(".slide-1-2").css({top: 0, left: 0})
    // $(".slide-1").hide()
    $(".slide-2").show("slide", { direction: "right" }, 1000, function() {
        $(".slide-2-1").show().animate({
            "opacity": 1,
            "width": "200px",
            "height": "200px",
            "top": "80px", 
            "left": leftPosition+"px"}, 1500, "swing", function() {
                $(".slide-2-2").show().animate({"width": "200px",
                "height": "200px",
                "top": "80px", 
                "left": leftPosition+"px"}, 500, "swing").animateRotate(360, {
                    duration: 1500,
                    easing: 'linear',
                    complete: function() {
                        setTimeout(function() {
                            thirdSlide(leftPosition)
                        }, 2500)
                    },
                    setp: function() {}
                })
            })
        })
}

// Slide 3
function thirdSlide(leftPosition) {
    $(".slide-2-1").hide()
    $(".slide-2-2").hide()
    $(".slide-2-1").css({top: 0, left: 0})
    $(".slide-2-2").css({top: 0, left: 0})
    $(".slide-2").hide()
    $(".slide-3").show("slide", { direction: "left" }, 1000, function() {
        $(".slide-3-1").show().animate({
            "opacity": 1,
            "width": "200px",
            "height": "200px",
            "top": "80px", 
            "left": leftPosition+"px"}, 1500, "swing", function() {
                $(".slide-3-2").show().animate({"width": "200px",
                "height": "200px",
                "top": "80px", 
                "left": leftPosition+"px"}, 500, "swing").animateRotate(360, {
                    duration: 1500,
                    easing: 'linear',
                    complete: function() {
                        setTimeout(function() {
                            firstSlide(leftPosition)
                        }, 2500)
                    },
                    setp: function() {}
                })
            })
        })
}

// Sticky header on scroll
$(window).scroll(function(){
    var header = $('#header'), scroll = $(window).scrollTop();
    var body = document.body, html = document.documentElement;
    var height = Math.max( body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
    if (scroll >= (height * .25)) {
        header.addClass('sticky');
    } else {
        header.removeClass('sticky');
    }
});

// Menu drop-down on mouse hover
$(document).ready(function () {
    $("div#header > .menu > a.menu-click").hover(
        function () {
            $('ul.dropdown-menu').stop(true, true).slideDown('medium');
        }, 
        function () { //.stop(true,true).slideUp('medium');
            $('ul.dropdown-menu').mouseleave(function() {
                var thisUI = $('ul.dropdown-menu')
                thisUI.hide()
                $('html').click(function(){
                    thisUI.hide()
                    $('html').unbind('hover')
                })
            })
        }
    );

    $("ul.dropdown-menu li#product-submenu").hover(
        function() {
            $("ul.dropdown-submenu").stop(true, true).slideDown('medium');
        },
        function() {
            $('ul.dropdown-menu').mouseleave(function() {
                $("ul.dropdown-submenu").hide()
                $('html').click(function() {
                    $('html').unbind('hover')
                })
            })
        }
    )
});

// Contact us modal
$(function() {
    $("#phones").dialog({
        width: "auto",
        height: "auto",
        position: {my: "left bottom", at: "top",  of: $('#phone-click')},
        autoOpen: false,
        title: 'Contact Us',
        show: {
            effect: "blind",
            duration: 1000
        },
        hide: {
            effect: "explode",
            duration: 1000
        }
    });
    $("#phone-click").on("click", function() {
        $("#phones").dialog("open", 'position', [0,0]);
    });
    $("#phones").on('click',function(){
        $("#phones").dialog('close');
    });
});

// Rotate animation
$.fn.animateRotate = function(angle, duration, easing, complete) {
    var args = $.speed(duration, easing, complete);
    var step = args.step;
    return this.each(function(i, e) {
        args.complete = $.proxy(args.complete, e);
        args.step = function(now) {
        $.style(e, 'transform', 'rotate(' + now + 'deg)');
        if (step) return step.apply(e, arguments);
        };

        $({deg: 0}).animate({deg: angle}, args);
    });
};

// Detect div resize
(function ($) {
    $.fn.sizeChanged = function (handleFunction) {
        var element = this;
        var lastWidth = element.width();
        var lastHeight = element.height();
        setInterval(function () {
            if (lastWidth === element.width()&&lastHeight === element.height())
                return;
            if (typeof (handleFunction) == 'function') {
                handleFunction({ width: lastWidth, height: lastHeight },
                { width: element.width(), height: element.height() });
                lastWidth = element.width();
                lastHeight = element.height();
            }
        }, 100);
        return element;
    };
} (jQuery));