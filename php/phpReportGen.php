<?php

/*******************************************************************************************
*
* Class Name : phpReportGenerator
* Version    : 1.0
* Written By : Hasin Hayder
* Start Date : 4th July, 2004
* Copyright  : Systech Digital. 
*
********************************************************************************************
*
* Script to generate report from a valid my sql connection.
* user have to supply which fields he want to display in table.
* All properties are changable.
*
*/

class phpReportGenerator
{
	var $mysql_resource;
	var $header;
	var $foolter;
    var $fields = array();
	var $cellpad;
	var $cellspace;
	var $border;
	var $width;
	var $modified_width;
	var $header_color;
	var $header_textcolor;
	var $header_alignment;
	var $body_color;
	var $body_textcolor;
	var $body_alignment;
	var $surrounded;
	var $hashfeild;
	
	function generateReport()
	{
		$this->border = (empty($this->border))?"0":$this->border;
		$this->cellpad = (empty($this->cellpad))?"1":$this->cellpad;
		$this->cellspace = (empty($this->cellspace))?"0":$this->cellspace;
		$this->width = (empty($this->width))?"100%":$this->width;
		$this->header_color = (empty($this->header_color))?"#FFFFFF":$this->header_color;
		$this->header_textcolor = (empty($this->header_textcolor))?"#000000":$this->header_textcolor;		
		$this->header_alignment = (empty($this->header_alignment))?"left":$this->header_alignment;
		$this->body_color = (empty($this->body_color))?"#FFFFFF":$this->body_color;
		$this->body_textcolor = (empty($this->body_textcolor))?"#000000":$this->body_textcolor;
		$this->body_alignment = (empty($this->body_alignment))?"left":$this->body_alignment;
		$this->surrounded = (empty($this->surrounded))?false:true;
		$this->modified_width = ($this->surrounded==true)?"100%":$this->width;
		
		//echo "modified_width : ".$this->modified_width."<br>"; 
		
		if (!($this->mysql_resource instanceof mysqli_result))
		{
			echo "Hi--";
			die ("User doesn't supply any valid mysql resource after executing query result");
		}
		/*
		* Lets calculate how many fields are there in supplied resource
		* and store their name in $this->fields[] array
		*/
		$res = $this->mysql_resource;
		$field_count = $res->field_count;
		$i = 0;
		
		while ($i < $field_count)
		{
			$field = mysqli_fetch_field($this->mysql_resource);
			$this->fields[$i] = $field->name;
			$this->fields[$i][0] = strtoupper($this->fields[$i][0]);
			$i++;
		}
		
		
		/*
		* Now start table generation
		* We must draw this table according to number of fields
		*/
		echo "<style>
#customers {
    font-family: 'Trebuchet MS', Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

#customers td, #customers th {
    border: 1px solid #ddd;
    padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
    padding-top: 12px;
    padding-bottom: 12px;
    text-align: left;
    background-color: #2980b9;
    color: white;
}
</style>";
		echo "<b><i>".$this->header."</i></b>";
		echo "<P></P>";
		
		//Check If our table has to be surrounded by an additional table
		//which increase style of this table
		if ($this->surrounded == true) 
			echo "<table id='customers'><tr><td>";
			
		echo "<table id='customers'>";
		echo "<tr bgcolor = '$this->header_color'>";
		
		//Header Draw
		for ($i = 0; $i< $field_count; $i++)
		{
			//Now Draw Headers
			echo "<th align = '$this->header_alignment'><font color = '$this->header_textcolor'>&nbsp;".$this->fields[$i]."</font></th>"; 
			
			if(strcmp($this->fields[$i],"Hash")==0)
			{
				$hashfeild=$i;
			}
		}
		
		echo "</tr>";
		
		//Now fill the table with data
		while ($rows = mysqli_fetch_row($this->mysql_resource))
		{
			echo "<tr align = '$this->body_alignment' bgcolor = '$this->body_color'>";
			for ($i = 0; $i < $field_count; $i++)
			{
				
				//Now Draw Data
				if($i == $hashfeild)
				{
					$h=explode("#",$rows[$i]);
					if(sizeof($h)>1)
					{
						echo "<td><font color = '$this->body_textcolor'>&nbsp;"."<strong>Original :</strong>".$h[0]."<strong> Modified : </strong>".$h[1]."</font></td>";
					}
					else
					{
						echo "<td><font color = '$this->body_textcolor'>&nbsp;".$rows[$i]."</font></td>";
						
					}
				}
				else
				{
				
					echo "<td><font color = '$this->body_textcolor'>&nbsp;".$rows[$i]."</font></td>";
				}
			}
			echo "</tr>";
		}
		echo "</table>";
		
		if ($this->surrounded == true) 
			echo "</td></tr></table>";

		
		
	}
}

?>
