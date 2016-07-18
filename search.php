<?php
include('config.php');
$db = new mysqli($mysql_host, $mysql_user, $mysql_password, $mysql_db);
if ($db->connect_errno) {
    die("Failed to connect to database.");
}

$q = $_GET["q"];

$res = $db->query("SELECT * FROM artists WHERE first LIKE '%$q%' OR last LIKE '%$q%' ORDER BY last");

header("Content-Type: application/json");

$results = array("count" => $res->num_rows, "results" => array());
while ($row = $res->fetch_assoc()) {
    array_push($results["results"], $row);
}
echo json_encode($results);
$db->close();
?>
