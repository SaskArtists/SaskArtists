<?php
include("config.php");
//FUNCTIONS
function generate_tabs() {
	echo '<ul class="nav nav-tabs">
			<li class="active"><a data-toggle="tab" href="#map">Map</a></li>';

	$alphas = range('A', 'Z');
	foreach ($alphas as $alpha) {
		echo '<li><a data-toggle="tab" href="#'.strtolower($alpha).'">'.$alpha.'</a></li>';
	}
    echo '<li><a data-toggle="tab" href="#num">#</a></li>';
	echo '</ul>';
}

function generate_carousel_indicators($num_slides) {
    echo "<ol class='carousel-indicators'>";
     
    echo "<li data-target='#myCarousel' data-slide-to='0' class='active'></li>";
    for ($i = 0; $i < ($num_slides - 1); $i++) {
        echo "<li data-target='#myCarousel' data-slide-to='0'></li>";
    }
    echo "</ol>"; 
}
//connect to the database
$db = new mysqli($mysql_host, $mysql_user, $mysql_password, $mysql_db);
if ($db->connect_errno) {
    die("Failed to connect to database");
}

?>

<html>
<head>
    
	<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Saskatchewan Artists</title>
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
	<!-- Latest compiled and minified JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <script src="search.js"></script>
</head>
<body>
<div class="container">
	<font color="#800080"><h2><a href="http://saskartists.ca/saskartists.html">Saskatchewan Artists</a></h2> </font>
	<p>Artists presented here were born, raised, or live in Saskatchewan, Canada. </p>
    
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
        <?php 
            $res = $db->query("SELECT * FROM `new_artists` INNER JOIN `artists` on new_artists.artist = artists.id");
            
            generate_carousel_indicators($res->num_rows);
            
            echo "<div class='carousel-inner'  role='listbox'>";
            $first = true;
            while ($row = $res->fetch_assoc()) {
                if ($first) { 
                    echo "<div class='item active'>";
                }
                else {
                    echo "<div class='item'>";
                }
                echo "<img src='".$row["work_url"]."' style='max-height: 500px; width:100%;'>";
                echo "<div class='carousel-caption'>";
                echo "<h3><a style='color:white;' href='http://saskartists.ca/".$row["short"]."'>".$row["first"]." ".$row["last"]."</a></h3>";
                echo "<p>".$row["title"]."</p>";
                echo "</div>";
                echo "</div>";
                $first = false;
            }
            echo "</div>";
            /* var_dump($new_artists); */
        ?>
        <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
            <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
            <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>

    <!-- TAB SECTION --> 
    <?php generate_tabs(); ?>

	<div class="tab-content">
        <?php
            //fetch the artist info
            $res = $db->query("SELECT * FROM artists ORDER BY last");

            //init the artists assoc array. We sort them into an assoc array by last name, first letter
            $artists = array();
            foreach(range('a', 'z') as $char) {
                $artists[$char] = array();
            }
            $artists["num"] = array();
            
            //this fills the assoc array with values from the database
            while ($row = $res->fetch_assoc()) {
                if ($row) {
                    $link = '<li><a href="http://saskartists.ca/'.$row['short'].'">'.$row['first']. ' ' .$row['last']. '</a> '.$row['description'].'</li>';
                    $last_name_letter = strtolower(substr($row['last'], 0, 1));
                    if (is_numeric($last_name_letter)) {
                        array_push($artists["num"], $link); 
                    } else {
                        array_push($artists[$last_name_letter], $link); 
                    }
                }
            }

            foreach($artists as $letter => $names) {
                if (count($names) == 0) {
                    array_push($artists[$letter], "<li>There are no artists here, yet.</li>");
                }
            }
            
            //now me have to make the divs to put the names into and actually put them there. Not really a big deal.
            foreach($artists as $letter => $names) {
                echo '<div id="'.$letter.'" class="tab-pane fade"><h3>'.ucwords($letter).' Section</h3><br /><ul>';
                foreach($names as $name) {
                    echo $name;
                }
                echo '</ul></div>';
            }
            $db->close();
        ?>
		<div id="map" class="tab-pane fade in active">
            <h3>Search</h3>
            <div class="form-inline">
                <div class="form-group">
                    <input class="form-control" type="text" placeholder="Search..." id="search-box">
                    <button class="btn btn-primary" id="search-button">Search</button>
                </div>
            </div>
            <p id="search-result-count"></p>
            <ul id="search-results">
            </ul>
    		<h3>Map of Artist Locations</h3>
            <a href="http://saskartists.ca/map.html">Map</a>
  		</div>
	</div>
</div>
<footer class="container text-center">
	<hr>
	<p> <a href="http://www.metric-hosting.ca/index.php">Sponsor</a> <br>
	Revised: 2015
</footer>
</p>
</body>
</html>
