<?php

  include('config.php');
  //connect to the database
  $db = new mysqli($mysql_host, $mysql_user, $mysql_password, $mysql_db);
  if ($db->connect_errno) {
      die("Failed to connect to database");
  }

  $q = $db->query('SELECT * FROM locations');
  echo '[';
  $x = 1;
  while($row=$q->fetch_assoc()){
    echo "{\"lat\":".$row['lat'].",\"lng\":".$row['lon'].",\"data\":{\"name\":\"".$row['name']."\"}}";
    if($x != $q->num_rows){
      echo ",";
    }
    $x += 1;
  }
  echo ']';

 ?>
