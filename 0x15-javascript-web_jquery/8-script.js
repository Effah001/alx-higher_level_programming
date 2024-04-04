$(document).ready(function() {
  $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
    const movieList = $("#list_movies");
    $.each(data.results, function(index, movie) {
      const listItem = $("<li>");
      listItem.text(movie.title);
      movieList.append(listItem);
    });
  });
});
