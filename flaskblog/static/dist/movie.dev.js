"use strict";

$(function () {
  var timer = null;
  var xhr = null;
  $(".user_popup").hover(function (event) {
    // mouse in event handler
    var elem = $(event.currentTarget);
    timer = setTimeout(function () {
      timer = null;
      xhr = $.ajax("/user/" + elem.first().text().trim() + "/popup").done(function (data) {
        xhr = null; // create and display popup here
      });
    }, 1000);
  }, function (event) {
    // mouse out event handler
    var elem = $(event.currentTarget);

    if (timer) {
      clearTimeout(timer);
      timer = null;
    } else if (xhr) {
      xhr.abort();
      xhr = null;
    } else {// destroy popup here
    }
  });
});