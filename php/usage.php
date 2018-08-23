<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>REPORT</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
 
<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<script>

function down(e)
{
	window.print();
	
}


</script>
</head>

<body>
	<?php
	include("phpReportGen.php");
	include("config.php");
	
	
	
	
	echo "<center><h3> <div class='container well'>File Integrity Monitor</h3></div></center>";
	
	$sql="select * from systems";
	$res1 = $conn->query($sql);
	if ($res1->num_rows > 0) {
    // output data of each row
	
    while($row12 = $res1->fetch_assoc())
	{	
		$sql="SELECT path,hash,Time from hashes where sysid=".$row12['serial'];
		$res = $conn->query($sql);
		if($res->num_rows>0)
		{
			echo "<div class='container panel panel-default panel-heading'><strong>System Id : </strong>".$row12['serial']."<strong>     Mac Id :</strong> ".$row12['mac_id']."</div>";
				
			$prg = new phpReportGenerator();
			$prg->width = "100%";
			$prg->cellpad = "0";
			$prg->cellspace = "2";
			$prg->border = "0";
			$prg->header_color = "#ea6153";
			$prg->header_textcolor="#FFFFFF";
			$prg->body_alignment = "left";
			$prg->body_color = "#f6f6f6";
			$prg->body_textcolor = "#800022";
			$prg->surrounded = '2';
			$prg->mysql_resource = $res; //<---
			$prg->title = "Test Table";
			$prg->generateReport();
			echo "<br/>";
		}
		
	}
		
		
		
    
	} 
	
	
	?>
	<br/>
	<center><button onclick="down(event)"> Download PDF</button></center>
</body>
</html>
