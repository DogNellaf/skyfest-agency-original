"use strict";
function getCookie(name) {
  var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined
}

function setCookie (name, value, options) {
  options = options || {};

  if (!options.path) {
    options.path = '/'
  }

  let expires = options.expires;

  if (typeof expires === 'number' && expires) {
    let d = new Date();
    d.setTime(d.getTime() + expires * 1000);
    expires = options.expires = d
  }
  if (expires && expires.toUTCString) {
    options.expires = expires.toUTCString()
  }

  value = encodeURIComponent(value);

  let updatedCookie = name + '=' + value;

  for (var propName in options) {
    if (options.hasOwnProperty(propName)) {
      updatedCookie += '; ' + propName;
      var propValue = options[propName];
      if (propValue !== true) {
        updatedCookie += '=' + propValue
      }
    }
  }

  document.cookie = updatedCookie;
  return true
}

function screenh100 () {
  // $("#sb-site").css({"position": "relative"});
  $(".height100").each(function () {
    $(this).height($(window).height()).css({"position": "relative", "z-index": 99});
  });

  $("#new_window").css({"position": "fixed", "z-index": 999});
}

function Form() {
  var T = this;
  this.button = '.submit,input[type="submit"]';
  this.message = '.form__messages';
  this.error = '.form__err';
  this.inputs = 'input, select, textarea';
  this.hasErrorClass = '.has-error';
  this.hasSuccessClass = '.has-success';
  this.excludes = 'input[type=radio],input[type=hidden],input[type=submit],input[type=image],input[type=button]';

  this.populateDataAjaxForm = function (form) {
    var data = {};
    $(T.inputs, form).each(function () {
      if ($(this).attr('type') === 'checkbox' || $(this).attr('type') === 'radio') {
        if ($(this).is(':checked')) {
          data[$(this).attr('name')] = $(this).val();
        }

      } else if (typeof($(this).attr('name')) !== 'undefined') {
        data[$(this).attr('name')] = $(this).val();
      }
    });
    data.url = window.location.href;
    return data;
  };

  this.clearFormErrors = function (form) {
    $(T.error, form).html('');
    $(T.hasErrorClass, form).removeClass(this.hasErrorClass.substr(1));
  };

  this.setFormSuccess = function (form, message) {
    T.clearFormErrors(form);
    if (typeof(message) !== 'string') {
      message = message.detail;
    }
    $(T.message, form).addClass('success').removeClass('failure').html(message).fadeIn(200);
  };

  this.setFormErrors = function (form, errors) {
    T.clearFormErrors(form);
    $(T.inputs, form).each(function () {
      var name = $(this).attr('name'),
        line = $(this).parents('.form-group');

      if (!name) {
        return true
      }

      if (name && name in errors) {
        if (errors.hasOwnProperty(name)) {
          var error = errors[name].join(';');
          delete errors[name];

          if (line) {
            line.addClass(T.hasErrorClass.substr(1))
              .find(T.error).html(error);
          }
        }
      } else {
        line = $(this).parent();
        line.addClass(T.hasSuccessClass.substr(1))
          .find(T.error).html('');
      }
    });

    if (errors) {
      var error = [];
      for (var i in errors) {
        if (errors.hasOwnProperty(i)) {
          error.push(errors[i].join(';'));
        }
      }
      error = error.join('<br/>');
      $(T.message, form).removeClass('success').addClass('failure').html(error).fadeIn(200);
    }
  };

  this.clearFormValues = function (form) {
    $(T.inputs, form).not(T.excludes).val('');
    $('.checkbox input', form).val('0');
    $('input[type=radio]', form).removeAttr('checked');
  };

  this.manageForm = function (formCont, callback, clearOnSuccess) {
    callback = typeof(callback) === 'undefined' ? function () {
      } : callback;
    clearOnSuccess = typeof(clearOnSuccess) === 'undefined' ? true : clearOnSuccess;
    formCont = $(formCont);
    $(T.button, formCont).click(function (e) {
      e.preventDefault();
      var inactive = $(this).hasClass('inactive');
      if (typeof(inactive) === 'undefined' || !inactive) {
        $(this).parents('form').submit();
      }
      return false;
    });

    $(formCont).submit(function (e) {
      e.preventDefault();
      var form = $(this);
      $(T.button, form).data('inactive', true).addClass('inactive');
      $(T.message, form).fadeOut(160);
      T.clearFormErrors(form);
      var data = T.populateDataAjaxForm(form);

      var onSuccess = function (data) {
        if (data['status'] === 'ok') {
          if (clearOnSuccess) {
            T.clearFormValues(form);
          }
          T.setFormSuccess(form, data['detail']);
          callback(data);
        } else {
          T.setFormErrors(form, data['detail']['errors']);
        }
        $(T.button, form).data('inactive', false).removeClass('inactive');
      };

      $.ajax({
        url: form.attr('action'),
        data: data,
        dataType: 'json',
        type: 'POST',
        timeout: 60000,  // 1 min
        success: onSuccess,
        error: function (jqXHR, textStatus) {
          if (jqXHR.status > 400) {
            console.log(textStatus + ' ' + jqXHR.status + ': ' + jqXHR.statusText);

            if (jqXHR.statusText) {
              T.setFormErrors(form, {'Server error': [jqXHR.statusText]});
            }
            $(T.button, form).data('inactive', false).removeClass('inactive');
          } else if (jqXHR.status === 400) {
            onSuccess(jqXHR.responseJSON);
          }
        }
      });
      return false;
    });
  };
}

var form = new Form();

function sharePopup (url) {
  var maxWidth = Math.min(window.outerWidth, 650);
  var maxHeight = Math.min(window.outerHeight, 420);
  window.open(url, '', `toolbar=0,status=0,width=${maxWidth},height=${maxHeight}`)
}

function share (network) {
  const shareUrl = encodeURIComponent(document.location.href);
  var title = encodeURIComponent(document.title);
  var url = null;

  if (network === 'facebook') {
    url = `http://www.facebook.com/sharer/sharer.php?u=${shareUrl}`
  }
  if (network === 'ok') {
    title = encodeURIComponent(document.title);
    url = `https://connect.ok.ru/offer?url=${shareUrl}&title=${title}`
  }
  if (network === 'vk') {
    url = `https://vk.com/share.php?url=${shareUrl}&title=${title}&noparse=true`
  }

  if (url) {
    sharePopup(url)
  }
}

function getBodyScrollTop () {
  return (document.documentElement && document.documentElement.scrollTop)
    || (document.body && document.body.scrollTop);
}

(function ($) {
  $(document).ready(function () {

    var subscribeForm = $('.subscribe-form');
    if (subscribeForm.length) {
      form.manageForm(subscribeForm, function () {
        $('input', subscribeForm).remove()
      });
    }

    var feedbackForm = $('.feedback-form');
    if (feedbackForm.length) {
      form.manageForm(feedbackForm, function () {
        if (window.ym) {
          if (feedbackForm.hasClass('.feedback-form--popup')) {
            window.ym(60701338, 'reachGoal', 'orderfotm_submit');
          } else {
            window.ym(60701338, 'reachGoal', 'contactsform_submit');
          }
        }

        $('.form-group', feedbackForm).remove()
      });
    }

    $('.social-share li').click(function () {
      share('' + this.classList);
    });

    // DATA BACKGROUND IMAGE
    var pageSection = $(".bg-image");
    pageSection.each(function (indx) {
      if ($(this).attr("data-background")) {
        $(this).css("background-image", "url(" + $(this).data("background") + ")");
      }
    });


    // HAMBURGER MENU
    $('.hamburger').on('click', function (e) {
      if ($(".site-navigation").hasClass("active")) {
        $(".hamburger").toggleClass("open");
        $("body").toggleClass("overflow");
        $(".site-navigation").removeClass("active")
          .css("transition-delay", "0.9s");
        $(".site-navigation .inner").css("transition-delay", "0s");
        $(".site-navigation .bottom").css("transition-delay", "0.1s");
        $(".site-navigation .layers span:nth-child(1)").css("transition-delay", "0.35s");
        $(".site-navigation .layers span:nth-child(2)").css("transition-delay", "0.50s");
        $(".site-navigation .layers span:nth-child(3)").css("transition-delay", "0.65s");
      } else {
        $(".site-nagivation").addClass('active');
        $(".hamburger").toggleClass("open");
        $("body").toggleClass("overflow");
        $(".site-navigation").toggleClass("active")
          .css("transition-delay", "0s");
        $(".site-navigation .inner").css("transition-delay", "0.65s");
        $(".site-navigation .bottom").css("transition-delay", "0.80s");

      }
      $(this).toggleClass("active");
    });


    // PAGE TRANSITION
    $('body a').on('click', function (e) {
      var target = $(this).attr('target');
      var fancybox = $(this).data('fancybox');
      var url = this.getAttribute("href");
      if (target !== '_blank' && typeof fancybox == 'undefined' && url.indexOf('#') < 0) {
        e.preventDefault();
        var url = this.getAttribute("href");
        if (url.indexOf('#') != -1) {
          var hash = url.substring(url.indexOf('#'));

          if ($('body ' + hash).length != 0) {
            $('.page-transition').removeClass("active");

          }
        } else {
          $('.page-transition').toggleClass("active");
          setTimeout(function () {
            window.location = url;
          }, 1300);
        }
      }
    });


    // SWITHER
    $('.switcher .holder').on('click', function (e) {
      $(this).toggleClass("switch");
      $('.pricing-block').toggleClass("change");
    });


    // PARALLAX
    $.stellar({
      horizontalScrolling: false,
      verticalOffset: 0,
      responsive: true
    });


    // CONTACT FORM INPUT LABEL
    function checkForInput(element) {
      const $label = $(element).siblings('span');
      if ($(element).val().length > 0) {
        $label.addClass('label-up');
      } else {
        $label.removeClass('label-up');
      }
    }

    // The lines below are executed on page load
    $('input, textarea, select').each(function () {
      checkForInput(this);
    });

    // The lines below (inside) are executed on change & keyup
    $('input, textarea, select').on('change keyup', function () {
      checkForInput(this);
    });


  });
  // END DOCUMENT READY


  new Swiper('.carousel-slider', {
    slidesPerView: 'auto',
    spaceBetween: 5,
    centeredSlides: true,
    loop: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    }
  });


  new Swiper('.testimonials-slider', {
    slidesPerView: 'auto',
    spaceBetween: 5,
    centeredSlides: true,
    loop: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    }
  });


  new Swiper('.simple-slider', {
    slidesPerView: 1,
    spaceBetween: 0,
    centeredSlides: true,
    loop: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    }
  });

  // COUNTER
  $(document).scroll(function () {
    $('.odometer').each(function () {
      var parent_section_postion = $(this).closest('section').position();
      var parent_section_top = parent_section_postion.top;
      if ($(document).scrollTop() > parent_section_top - 300) {
        if ($(this).data('status') === 'yes') {
          $(this).html($(this).data('count'));
          $(this).data('status', 'no')
        }
      }
    });
  });

  // WOW ANIMATION
  var wow = new WOW(
    {
      animateClass: 'animated',
      offset: 50
    }
  );
  wow.init();

  screenh100();

  $(".order-btn").click(function (e) {
    e.preventDefault();

    if (window.ym) {
      window.ym(60701338, 'reachGoal', 'button_orderform');
    }

    if ($(window).width() > 480) $("#new_window").show().css({
      "top": -$(window).height(),
      "display": "table",
      "position": "fixed",
      "overflow": "hidden"
    }).animate({"top": 0}, 500).css({"show": "table"});
    else $("#new_window").show().css({
      "top": getBodyScrollTop() - $(window).height(),
      "display": "table"
    }).animate({"top": getBodyScrollTop()}, 500).css({"show": "table"});
    return false;
  });

  $("#new_window .close_window").click(function () {
    $("#new_window").animate({"top": -$(window).height()}, 500, function () {
      $(this).hide();
    });
    return false;
  });

})(jQuery);
