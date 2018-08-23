<?php
header("Access-Control-Allow-Origin: *");
include 'config.php';	
$data =$_POST["hashes"];
$sysId=$_POST["sysid"];
$hashes = array();
$path = array();
$fnames = array();
$result = json_decode($data);
$t = date('Y-m-d H:i:s');
foreach ($result as $key => $value) 
{
    array_push($hashes,$value);
	array_push($path,$key);	
}
if(sizeof($path) >0)
{
	for($i=0;$i<sizeof($hashes);$i++)
	{
		$sql = "INSERT INTO `hashes` (`serial`, `sysid`, `path`, `filename`, `hash`,`Time`) VALUES (NULL,'$sysId','$path[$i]','null','$hashes[$i]','$t');";
		$result = $conn->query($sql);
		
	}
	
}



?>