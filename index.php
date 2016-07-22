<?php
include("config.php");
//FUNCTIONS
function generate_tabs() {
	$letters = range('A', 'Z');
	array_push($letters, "#");

	echo "<ul class=\"nav nav-tabs\">";
		echo "<li class=\"active\"><a data-toggle=\"tab\" href=\"#map\">Map</a></li>";
		foreach ($letters as $letter){
			if($letter == "#"){
				$letter = "Group";
				$text = "<i class=\"fa fa-users\" aria-hidden=\"true\"></i>";
			}else{
				$text = $letter;
			}
			echo "<li><a data-toggle=\"tab\" href=\"#$letter\">$text</a></li>";
		}
	echo "</ul>";
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

	<script type="text/javascript" src="jquery-3.1.0.min.js"></script>
	<script src="http://maps.googleapis.com/maps/api/js?sensor=false" type="text/javascript"></script>
	<script type="text/javascript" src="gmap3.js"></script>
	<!-- Latest compiled and minified CSS -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
	<style>

	body{
		width: 100%;
	}

		#container{
			position:relative;
			height:700px;
			width:1250px;
			display:block;
			margin-left:auto;
			margin-right:auto;
		}
		#googleMap{
			border: 1px dashed #C0C0C0;
			width: 75%;
			height: 700px;
			margin-bottom: 50px;
			margin-left:auto;
			margin-right:auto;
			margin-top: 50px;
		}

		/* cluster */
		.cluster{
			color: #FFFFFF;
			text-align:center;
			font-family: Verdana;
			font-size:14px;
			font-weight:bold;
			text-shadow: 0 0 2px #000;
			-moz-text-shadow: 0 0 2px #000;
			-webkit-text-shadow: 0 0 2px #000;
		}
		.cluster-1{
			background: url(images/m1.png) no-repeat;
			line-height:50px;
			width: 50px;
			height: 40px;
		}
		.cluster-2{
			background: url(images/m2.png) no-repeat;
			line-height:53px;
			width: 60px;
			height: 48px;
		}
		.cluster-3{
			background: url(images/m3.png) no-repeat;
			line-height:66px;
			width: 70px;
			height: 56px;
		}

		/* infobulle */
		.infobulle{
			overflow: hidden;
			cursor: default;
			clear: both;
			position: relative;
			height: 34px;
			padding: 0pt;
			background-color: rgb(57, 57, 57);
			border-radius: 4px 4px;
			-moz-border-radius: 4px 4px;
			-webkit-border-radius: 4px 4px;
			border: 1px solid #2C2C2C;
		}
		.infobulle .bg{
			font-size:1px;
			height:16px;
			border:0px;
			width:100%;
			padding: 0px;
			margin:0px;
			background-color: #5E5E5E;
		}
		.infobulle .text{
			color:#FFFFFF;
			font-family: Verdana;
			font-size:11px;
			font-weight:bold;
			line-height:25px;
			padding:4px 20px;
			text-shadow:0 -1px 0 #000000;
			white-space: nowrap;
			margin-top: -17px;
		}
		.infobulle.drive .text{
			background: url(images/drive.png) no-repeat 2px center;
			padding:4px 20px 4px 36px;
		}
		.arrow{
			position: absolute;
			left: 45px;
			height: 0pt;
			width: 0pt;
			margin-left: 0pt;
			border-width: 10px 10px 0pt 0pt;
			border-color: #2C2C2C transparent transparent;
			border-style: solid;
		}

	</style>

	<script type="text/javascript">

	var macDoList = <?php include('locations.php'); ?>;

	var artists = <?php include('artists.php'); ?>;

		$(function(){

			$("#googleMap").gmap3({
				map:{
					options: {
						center:[54.358277,-106.018448],
						zoom: 5,
						mapTypeId: google.maps.MapTypeId.TERRAIN
					}
				},
				marker: {
					values: macDoList,
					cluster:{
						radius:20,
						// This style will be used for clusters with more than 0 markers
						0: {
							content: "<div class='cluster cluster-1'>CLUSTER_COUNT</div>",
							width: 53,
							height: 52
						},
						// This style will be used for clusters with more than 20 markers
						20: {
							content: "<div class='cluster cluster-2'>CLUSTER_COUNT</div>",
							width: 56,
							height: 55
						},
						// This style will be used for clusters with more than 50 markers
						50: {
							content: "<div class='cluster cluster-3'>CLUSTER_COUNT</div>",
							width: 66,
							height: 65
						},
						events: {
							click: function(cluster) {
								var map = $(this).gmap3("get");
								map.setCenter(cluster.main.getPosition());
								map.setZoom(map.getZoom() + 1);
							}
						}
					},
					options: {
						icon: new google.maps.MarkerImage("http://maps.gstatic.com/mapfiles/icon_green.png")
					},
					events:{
						click: function(marker, event, context){
							$('#artists').html("<h1>"+context.data.name+"</h1>");
							var length = artists.length, element = null;
			for (var i = 0; i < length; i++) {
				if(artists[i].city == context.data.name)
						$('#artists').html($('#artists').html() + "</br><a href=\'" + artists[i].link + "\'>"+artists[i].name+"</a>");
			}
						},
						mouseover: function(marker, event, context){
							$(this).gmap3(
								{clear:"overlay"},
								{
								overlay:{
									latLng: marker.getPosition(),
									options:{
										content:  "<div class='infobulle'>" +
																"<div class='bg'></div>" +
																"<div class='text'>" + context.data.name + "</div>" +
															"</div>" +
															"<div class='arrow'></div>",
										offset: {
											x:-46,
											y:-73
										}
									}
								}
							});
						},
						mouseout: function(){
							$(this).gmap3({clear:"overlay"});
						}
					}
				}
			});

		});
		var isCtrl = false;

$(document).keyup(function (e) {
if(e.which == 17) isCtrl=false;
}).keydown(function (e) {
if(e.which == 17) isCtrl=true;
if(e.which == 74 && isCtrl == true) {
	$('#newInfo').show('slow');
	return false;
}
});
	</script>

	<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Saskatchewan Artists</title>
	<!-- Latest compiled and minified JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <script src="search.js"></script>
</head>
<body>
<div id="container">
	<font color="#800080"><h2><a href="index.php">Saskatchewan Artists</a></h2> </font>
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
                echo "<img src='".$row["work_url"]."'>";
                echo "<div class='carousel-caption'>";
                echo "<h3><a style='color:white;' href='".$row["short"]."'>".$row["first"]." ".$row["last"]."</a></h3>";
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
				$letters = range('A', 'Z');
				array_push($letters, "#");
				echo "<div class=\"tab-content\">";
				foreach ($letters as $letter){
					$q = $db->query("SELECT * FROM artists where sort LIKE \"%$letter%\"");
					if($letter == "#"){
						$letter = "Group";
					}
					echo "<div id=\"$letter\" class=\"tab-pane fade\">";
						echo "<h3>$letter Section</h3>";
					echo "<ul>";
					while ($row = $q->fetch_assoc()){
								echo "<li><a href=".$row['short'].">".$row['name']."</a></li>";
					}
					echo  "</ul>";
				echo  "</div>";
				}
            $db->close();
        ?>
		<div id="map" class="tab-pane fade in active">
            <h3>Search</h3>
            <div class="form-inline">
                <form id="search-form" class="form-group">
                    <input class="form-control" type="text" placeholder="Search..." id="search-box">
                    <input type="submit" class="btn btn-primary" id="search-button" value="Search">
                </form>
            </div>
            <p id="search-result-count"></p>
            <ul id="search-results">
            </ul>
    		<h3>Map of Artist Locations</h3>
				<div id='newInfo' style='display:none'><input type='button' id='scanMeta' value='Scan Metadata'/></div>
				<div id="googleMap"></div>
				<div id="artists"></div>
  		</div>
	</div>
    <footer class="text-center">
	<hr>
	<p>Visit us on <a href='https://github.com/SaskArtists/SaskArtists/'>GitHub</a></p>
	<p> <a href="http://www.metric-hosting.ca/">Sponsor</a> <br></p>
	<p><a href="disclaimer.html">Disclaimer:</p>
	<p>Revised: 2016</p>
</footer>
</div>

</body>
</html>
