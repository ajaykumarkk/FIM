<?php
header("Access-Control-Allow-Origin: *");
include 'config.php';
// Escape user inputs for security
$link = mysqli_connect("localhost", "root", "root123", "fim");
 
// Check connection
if($link === false)
{
    die("ERROR: Could not connect. " . mysqli_connect_error());
}

$mac = $_GET['mac_id'];

$resultset_1 = $conn->query("select * from systems where mac_id='".$mac."';") or die(mysql_error());
$count = $resultset_1->num_rows;
   if($count == 0)
    {
       $resultset_2 = $conn->query("INSERT INTO `systems` (`serial`, `mac_id`, `system_name`) VALUES (NULL, '$mac', 'NULL');")  or
       die(mysql_error());
    }
	else{
       $row = $resultset_1->fetch_assoc();
       echo $row["serial"];
    }


?>