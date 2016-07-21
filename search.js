$(function() {
    $("#search-button").submit(function(e) {
        e.preventDefault();
        if ($("#search-box").val() === "") {
            alert("Please insert some text to search for.");
            return;
        }

        $.ajax({
            url: "search.php",
            type: "get",
            data: { q: $("#search-box").val() },
            success: function(response) {
                $("#search-result-count").text("We found: " + response.count);
                $("#search-results").empty();
                response.results.forEach(function(result) {
                    $("#search-results").append("<li><a href='http://saskartists.ca/" + result.short + "'>" + result.first + " " + result.last + "</a></li>");
                });
            },
            error: function(xhr) {
                alert("An error occured. Sorry.");
            }
        });
    });
});
