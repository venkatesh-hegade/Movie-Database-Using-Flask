"use strict";

$(document).ready(function () {
  $("#searchForm").on("submit", function (e) {
    e.preventDefault();
    var searchText = $("#searchText").val();
    getMovies(searchText);
  });
});

function getMovies(searchText) {
  //make request to api using axios
  // Make a request for a user with a given ID
  axios.get("https://api.themoviedb.org/3/search/movie?api_key=98325a9d3ed3ec225e41ccc4d360c817&language=en-US&query=" + searchText).then(function (response) {
    var movies = response.data.results;
    var output = "";
    $.each(movies, function (index, movie) {
      output += "\n          <div class=\"col-md-3\">\n            <div class=\"well text-center\">\n              <img src=\"https://image.tmdb.org/t/p/w500".concat(movie.poster_path, "\">\n              <h5>").concat(movie.title, "</h5>\n              <a onclick=\"movieSelected('").concat(movie.id, "')\" class=\"btn btn-primary\" href=\"#\">Movie Details</a>\n            </div>\n          </div>\n        ");
    });
    $("#movies").html(output);
  })["catch"](function (error) {
    console.log(error);
  });
}

function movieSelected(id) {
  sessionStorage.setItem("movieId", id);
  window.location = "movie.html";
  return false;
}

function getMovie() {
  var movieId = sessionStorage.getItem("movieId"); // Make a request for a user with a given ID

  axios.get("https://api.themoviedb.org/3/movie/" + movieId + "?api_key=98325a9d3ed3ec225e41ccc4d360c817").then(function (response) {
    var movie = response.data; //console.log(movie);

    var output = "\n        <div class=\"row\">\n          <div class=\"col-md-4\">\n            <img src=\"".concat(movie.poster_path, "\" class=\"thumbnail\">\n          </div>\n          <div class=\"col-md-8\">\n            <h2>").concat(movie.title, "</h2>\n            <ul class=\"list-group\">\n              <li class=\"list-group-item\"><strong>Genre:</strong> ").concat(movie.Genre, "</li>\n              <li class=\"list-group-item\"><strong>Released:</strong> ").concat(movie.Released, "</li>\n              <li class=\"list-group-item\"><strong>Rated:</strong> ").concat(movie.Rated, "</li>\n              <li class=\"list-group-item\"><strong>IMDB Rating:</strong> ").concat(movie.imdbRating, "</li>\n              <li class=\"list-group-item\"><strong>Director:</strong> ").concat(movie.Director, "</li>\n              <li class=\"list-group-item\"><strong>Writer:</strong> ").concat(movie.Writer, "</li>\n              <li class=\"list-group-item\"><strong>Actors:</strong> ").concat(movie.Actors, "</li>\n            </ul>\n          </div>\n        </div>\n        <div class=\"row\">\n          <div class=\"well\">\n            <h3>Plot</h3>\n            ").concat(movie.Plot, "\n            <hr>\n            <a href=\"http://imdb.com/title/").concat(post.imdb_id, "\" target=\"_blank\" class=\"btn btn-primary\">View IMDB</a>\n            <a href=\"home.html\" class=\"btn btn-default\">Go Back To Search</a>\n          </div>\n        </div>\n    ");
    $("#movie").html(output);
  })["catch"](function (error) {
    console.log(error);
  });
}