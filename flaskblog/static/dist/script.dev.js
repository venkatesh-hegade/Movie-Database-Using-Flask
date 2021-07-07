"use strict";

// getting all required elements
var searchWrapper = document.querySelector(".search-input");
var inputBox = searchWrapper.querySelector("input");
var suggBox = searchWrapper.querySelector(".autocom-box");
var icon = searchWrapper.querySelector(".icon");
var linkTag = searchWrapper.querySelector("a");
var webLink; // if user press any key and release

inputBox.onkeyup = function (e) {
  var userData = e.target.value; //user enetered data

  var emptyArray = [];

  if (userData) {
    icon.onclick = function () {
      webLink = "/post/" + userData;
      linkTag.setAttribute("href", webLink);
      console.log(webLink);
      linkTag.click();
    };

    emptyArray = suggestions.filter(function (data) {
      //filtering array value and user characters to lowercase and return only those words which are start with user enetered chars
      return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
    });
    emptyArray = emptyArray.map(function (data) {
      // passing return data inside li tag
      return data = "<li>" + data + "</li>";
    });
    searchWrapper.classList.add("active"); //show autocomplete box

    showSuggestions(emptyArray);
    var allList = suggBox.querySelectorAll("li");

    for (var i = 0; i < allList.length; i++) {
      //adding onclick attribute in all li tag
      allList[i].setAttribute("onclick", "select(this)");
    }
  } else {
    searchWrapper.classList.remove("active"); //hide autocomplete box
  }
};

function select(element) {
  var selectData = element.textContent;
  inputBox.value = selectData;

  icon.onclick = function () {
    webLink = "/post/" + selectData;
    linkTag.setAttribute("href", webLink);
    linkTag.click();
  };

  searchWrapper.classList.remove("active");
}

function showSuggestions(list) {
  var listData;

  if (!list.length) {
    userValue = inputBox.value;
    listData = "<li>" + userValue + "</li>";
  } else {
    listData = list.join("");
  }

  suggBox.innerHTML = listData;
} // webLink = "https://www.google.com/search?q=" + userData;
// webLink = "https://www.google.com/search?q=" + selectData;