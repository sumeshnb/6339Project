var globalMovieDetails = [];//global array to store movie details, it will have maximum 5 active movies
var data_bar = [];
var data_pie = [];
//var pie_name = [];
//console.log("test test");
//Movie class
function Movie (status,title,rating,genres,votes,languages,runtime,cast,director,tweets,positive_tweets,negative_tweets) {
        this.status = status;
        this.title = title;
        this.rating = rating;
        this.genres = genres;
        this.votes = votes;
        this.languages = languages;
        this.runtime = runtime;
        this.cast = cast;
        this.director = director;
        this.tweets = tweets;
        this.positive_tweets = positive_tweets;
        this.negative_tweets = negative_tweets;
        this.getStatus = getMovieStatus;
        this.getTitle = getMovieTitle;
        this.getRating = getMovieRating;
        this.getGenres = getMovieGenres;
        this.getVotes = getMovieVotes;
        this.getLanguages = getMovieLanguages;
        this.getRuntime = getMovieRuntime;
        this.getCast = getMovieCast;
        this.getDirector = getMovieDirector;
        this.getTweets = getMovieTotalTweets;
        this.getPositiveTweets = getMoviePositiveTweets;
        this.getNegativeTweets = getMovieNegativeTweets;
    }
     
    // anti-pattern! keep reading...
    function getMovieStatus() {
        return this.status;
    }
    function getMovieTitle() {
        return this.title;
    }
    function getMovieRating() {
        return this.rating;
    }
    function getMovieGenres() {
        return this.genres;
    }
    function getMovieVotes() {
        return this.votes;
    }
    function getMovieLanguages() {
        return this.languages;
    }
    function getMovieRuntime() {
        return this.runtime;
    }
    function getMovieCast() {
        return this.cast;
    }
    function getMovieDirector() {
        return this.director;
    }
     function getMovieTotalTweets() {
        return this.tweets;
    }
    function getMoviePositiveTweets() {
        return this.positive_tweets;
    }
    function getMovieNegativeTweets() {
        return this.negative_tweets;
    }

    //initialize all the movies to empty
    for(var i=0;i<5;i++){
      globalMovieDetails[i] = new Movie(false,"","","","","","","","");
    }

    console.log(globalMovieDetails);

    function isMovieFull(){
      for(var i=0;i<5;i++){
        if(globalMovieDetails[i].getStatus() == false){
        return false;//some empty slot present for comparision
        }
      }
      return true;//all five moves are already added
    }

    function numberOfMovies(){
      var movie_count = 0;
      for(var i=0;i<5;i++){
        if(globalMovieDetails[i].getStatus() == true){
        movie_count++;
        }
      }
      return movie_count;
    }

    function getMovieEmptySlot(){
      if(isMovieFull()){
        return -1;
      }

      for(var i=0;i<5;i++){
        if(globalMovieDetails[i].getStatus() == false){
        return i;// ith slot is free
        }
      }
    }    

    var availableTags = [
        "American Sniper (2014)",
        "Chappie (2015)",
        "Cinderella (2015)",
        "Clouds of Sils Maria (2014)",
        "Danny Collins (2015)",
        "Desert Dancer (2014)",
        "Do You Believe? (2015)",
        "Ex Machina (2015)",
        "Fifty Shades of Grey (2015)",
        "Furious Seven (2015)",
        "Get Hard (2015)",
        "Insurgent (2015)",
        "Into the Woods (2014)",
        "It Follows (2014)",
        "Kill Me Three Times (2014)",
        "Kingsman: The Secret Service (2014)",
        "Lost River (2014)",
        "Night at the Museum: Secret of the Tomb (2014)",
        "Paddington (2014)",
        "Run All Night (2015)",
        "Selma (2014)",
        "Seventh Son (I) (2014)",
        "The Gunman (2015)",
        "The Imitation Game (2014)",
        "The Longest Ride (2015)",
        "The Second Best Exotic Marigold Hotel (2015)",
        "The SpongeBob Movie: Sponge Out of Water (2015)",
        "While We're Young (2014)",
        "Woman in Gold (2015)"
    ];

//start of D3 code
function plotD3Barchart(){
console.log("compare button clicked");

var margin = {top: 120, right: 80, bottom: 270, left: 100},
    width = 550,
    height = 300;

var x0 = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var x1 = d3.scale.ordinal();

//var x2 = d3.scale.ordinal();

var y = d3.scale.linear()
    .range([height, 0]);

var color = d3.scale.ordinal()
    .range(["#009933","#CC3300","#006699", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

var xAxis = d3.svg.axis()
    .scale(x0)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

/*var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return "<strong>Rating:</strong> <span style='color:red'>" + Math.round((d.value/d.total)*100) + "</span>";
  })*/

var svg = d3.select("#visualization1").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//svg.call(tip);
  
/*d3.tsv("twitter_statistics.tsv", function(error, data) {
  var movieNames = d3.keys(data[0]).filter(function(key) { return key !== "name" && key !== "total"; });*/

  var categories = ["positive", "negative","imdb_rating"];
  //var categories = ["positive", "negative"];

   //console.log(categories);
  data_bar.forEach(function(d) {
    d.count = categories.map(function(name) { return {name: name, value: +d[name], total: +d.total}; });
    console.log(d.count);
  });



  x0.domain(data_bar.map(function(d) { return d.name; }));
  x1.domain(categories).rangeRoundBands([0, x0.rangeBand()]);
  y.domain([0, d3.max(data_bar, function(d) { return d3.max(d.count, function(d) { return Math.round((d.value)); }); })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .selectAll("text")  
            .style("text-anchor", "end")
            .attr("dx", "-1.2em")
            .attr("dy", "-0.5em")
            .attr("transform", function(d) {
                return "rotate(-45)" 
                });

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 40 - margin.left)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Rating (0 - 100)");

  var name = svg.selectAll(".name")
      .data(data_bar)
    .enter().append("g")
      .attr("class", "g")
      .attr("transform", function(d) { return "translate(" + x0(d.name) + ",0)"; });

  name.selectAll("rect")
      .data(function(d) { return d.count; })
    .enter().append("rect")
      .attr("width", /*x1.rangeBand()*/30)
      .attr("x", function(d) { return x1(d.name); })
      .attr("y", function(d) { return y(Math.round(d.value)); })
      .attr("height", function(d) { return height - y(Math.round((d.value))); })
      //.on('mouseover', tip.show)
      //.on('mouseout', tip.hide)
      .style("fill", function(d) { return color(d.name); });

  var legend = svg.selectAll(".legend")
      .data(categories.slice().reverse())
    .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

  legend.append("rect")
      .attr("x", width - 18)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

  legend.append("text")
      .attr("x", width - 24)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d; });

/*});*/
}

function plotD3Donutchart(){
    
    var radius = 150,
    padding = 10;

    var color = d3.scale.ordinal()
    .range(["#009933","#CC3300","#006699", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

    var arc = d3.svg.arc()
    .outerRadius(radius)
    .innerRadius(radius - 75);

    var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.rating; });

    /*d3.csv("donut.csv", function(error, data) {
      console.log(data);
    color.domain(d3.keys(data[0]).filter(function(key) { return key !== "name"; }));*/


    color.domain(d3.keys(data_pie[0]).filter(function(key) { return key !== "name"; }));

    data_pie.forEach(function(d) {
    d.ratings = color.domain().map(function(name) {
      return {name: name, rating: +d[name]};
    });
    console.log(d.ratings);
    });

    //console.log(data_pie);

  var legend = d3.select("#visualization2").append("svg")
      .attr("class", "legend")
      .attr("width", radius * 2.5)
      .attr("height", radius * 3)
      .selectAll("g")
      .data(color.domain().slice().reverse())
      .enter().append("g")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

  legend.append("rect")
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

  legend.append("text")
      .attr("x", 24)
      .attr("y", 9)
      .attr("dy", ".35em")
      .text(function(d) { return d; });

  var svg = d3.select("#visualization2").selectAll(".pie")
      .data(data_pie)
      .enter().append("svg")
      .attr("class", "pie")
      .attr("width", radius * 2.5)
      .attr("height", radius * 3)
      .append("g")
      .attr("transform", "translate(" + radius + "," + radius + ")");

  svg.selectAll(".arc")
      .data(function(d) { return pie(d.ratings); })
      .enter().append("path")
      .attr("class", "arc")
      .attr("d", arc)
      .style("fill", function(d) { return color(d.data.name); });

  svg.append("text")
      .attr("dy", ".35em")
      .style("text-anchor", "middle")
      .text(function(d) { return d.name; });

  // });

}

//end of D3 code
$(document).ready(function(){

//---------------------------------------


//--------------------------------------
    //console.log("ready");

    /*$('.clickable').on('click',function(){
      var effect = $(this).data('effect');
      $(this).closest('.panel')[effect]();
    });*/


    //hide all movie panels
    $("#movie1").hide(5);
    $("#movie2").hide(5);
    $("#movie3").hide(5);
    $("#movie4").hide(5);
    $("#movie5").hide(5);

    $("#movie_btn1").click(function(event){
        $("#movie1").hide(800);
        globalMovieDetails[0] = new Movie(false,"","","","","","","","");
    });
    $("#movie_btn2").click(function(event){
        $("#movie2").hide(800);
        globalMovieDetails[1] = new Movie(false,"","","","","","","","");
    });
    $("#movie_btn3").click(function(event){
        $("#movie3").hide(800);
        globalMovieDetails[2] = new Movie(false,"","","","","","","","");
    });
    $("#movie_btn4").click(function(event){
        $("#movie4").hide(800);
        globalMovieDetails[3] = new Movie(false,"","","","","","","","");
    });
    $("#movie_btn5").click(function(event){
        $("#movie5").hide(800);
        globalMovieDetails[4] = new Movie(false,"","","","","","","","");
    });

    $("#movie_max_btn").click(function(event){
        $("#max_movie").hide(2000);
    });
    /*$("button").click(function(){
        $("p").hide();
    });*/

    $("#search_box").autocomplete({
      source: availableTags
    });

    //-------compare clicked
    $("#compare_btn").click(function(event){
        event.preventDefault();
        data_bar = [];
        if(numberOfMovies() < 2){
            alert("Please select atleast two movies for comparison");
        }else{
        //clear current visualization
        $("#visualization1").text(" ");

        var movie_count = 0;
        for(var i=0;i<5;i++){
        if(globalMovieDetails[i].getStatus() == true){
            
            /*data_bar[i] = {"name":(globalMovieDetails[i].getTitle()).toString(),"positive":(globalMovieDetails[i].getPositiveTweets()).toString(),
                            "negative":(globalMovieDetails[i].getNegativeTweets()).toString(),"total":(globalMovieDetails[i].getTweets()).toString(),
                            "imdb_rating":(globalMovieDetails[i].getRating()*10).toString()};*/

                            //fill data for barchart -------------------------------------------------------
                            var mname1 = globalMovieDetails[i].getTitle();
                            //console.log(xyz);
                            var mname2 = mname1.toString();

                            var mpos1 = globalMovieDetails[i].getPositiveTweets();
                            var mneg1 = globalMovieDetails[i].getNegativeTweets();
                            var mtotal1 = globalMovieDetails[i].getTweets();
                            var mrating1 = globalMovieDetails[i].getRating();

                            mpos1 = (mpos1/mtotal1)*100;//store the percentage of positive tweets
                            mneg1 = (mneg1/mtotal1)*100;//store the percentage of positive tweets
                            mrating1 = mrating1*10;//make it to a scale of 1-100

                            var mpos2 = mpos1.toString();
                            var mneg2 = mneg1.toString();
                            var mtotal2 = mtotal1.toString();
                            var mrating2 = mrating1.toString();

                            data_bar[movie_count] = {"name":mname2,"positive":mpos2,
                            "negative":mneg2,"total":mtotal2,"imdb_rating":mrating2};
                            //fill data for barchart -------------------------------------------------------end
                            movie_count++;
                            //console.log(data_bar[i]);
            }
        }

        //---------------------------Donut Chart starts
        $("#visualization2").text(" ");
        var obj1 = {name:"imdb"};
        var obj2 = {name:"twitter"};
        for(var i=0;i<5;i++){
          if(globalMovieDetails[i].getStatus() == true){
            obj1[globalMovieDetails[i].getTitle()] = globalMovieDetails[i].getRating();
            obj2[globalMovieDetails[i].getTitle()] = (globalMovieDetails[i].getPositiveTweets()/
                                                      globalMovieDetails[i].getTweets())*100;
          }
        }
        data_pie[0] = obj1;
        data_pie[1] = obj2;
        console.log(data_pie);
        //---------------------------Donut Chart ends
        plotD3Barchart();
        plotD3Donutchart();
    }
    });
    //-------compare clicked - end

    $("#search_btn").click(function(event){


        console.log("search button clicked");
      if(isMovieFull()){
        
        event.preventDefault();
        /*var htmlAlertString = '<div class="alert alert-dismissible alert-danger">
  <button type="button" class="close" data-dismiss="alert">×</button>
  <strong>Sorry!</strong> You can compare a maximum of 5 movies only. Try removing some movies and then add 
            new movies for comparison
</div>';
        var escaped = $("#max_movie").text(htmlAlertString).html();

        $("#max_movie").html('<div class="alert alert-dismissible alert-danger">
  <button type="button" class="close" data-dismiss="alert">×</button>
  <strong>Sorry!</strong> You can compare a maximum of 5 movies only. Try removing some movies and then add 
            new movies for comparison
</div>');*/
        alert("Sorry! You can compare a maximum of 5 movies, try after removing some movies");

      }else{
        console.log("test1");
        event.preventDefault();

        var movie_name = $("#search_box").val();
        $("#search_box").val("");

        $.getJSON("/moviedetails/",{"movie_name": movie_name}, function(data){
            //alert("Data: " + data + "\nStatus: " + status);
            var title = data["Title"];
            var rating = data["Rating"];
            //------------genres contain multiple items without space , so make it look nice
            var gen = data["Genres"];
            var genarray = gen.toString().split(',');
            console.log(genarray);
            var genres = (genarray[0]).toString();
            for(var idx=1;idx<genarray.length;idx++){
              genres = genres.concat(", ");
              genres = genres.concat(genarray[idx]);
            }
            console.log(genres);
            //------------genres contain multiple items without space , so make it look nice - end
            var votes = data["Votes"];
            var languages = data["Languages"];
            var runtime = data["Runtime"];
            var cast = data["Cast"];
            var director_array = data["Director"];

            var dirlist = "";

            for(var count=0;count<director_array.length;count++){
              dirlist += director_array[count]["dirname"];

            //get tweet related info
            var tweets = data["Tweets"];
            var positive_tweets = data["Positive_Tweets"];
            var negative_tweets = data["Negative_Tweets"];
            }

            var empty_slot = getMovieEmptySlot();
            //add the movie to global array
            globalMovieDetails[empty_slot] = new Movie(true,title,rating,genres,votes,languages,runtime,cast,director_array,
                tweets,positive_tweets,negative_tweets);

            console.log(globalMovieDetails[empty_slot]);

            console.log("global array filled..");
            //var director = director_array[0]["dirname"];
            //alert("Title :" + title);
            //$("#title1").text(title);

            empty_slot++;//change subscript from 0 based array to movie1-5
            var title_selector = "#title"+empty_slot;
            var selector = "#movie_body"+empty_slot;
            console.log(selector);
            $(selector).html("<b>Title: </b>"+title+"</br><b>Director: </b>"+dirlist+"</br>"+"<b>Cast: </b>"+cast+"</br>"+"<b>Genres: </b>"+genres
              +"</br>"+"<b>Votes: </b>"+votes+"</br>"+"<b>Languages: </b>"+languages+"</br>"+"<b>Total tweets: </b>"+
              tweets+"</br>"+"<b>Positive Tweets: </b>"+positive_tweets+"</br>"+"<b>Negative_Tweets: </b>"+negative_tweets);
            var footer = "#footer"+empty_slot;
            $(footer).text("IMDB Rating : "+rating);
            $(title_selector).text(title);
            var movie_selector = "#movie"+empty_slot;
            $(movie_selector).show(700);

        });
      }
    });
});

