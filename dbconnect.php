<?php
	$dbHost = "localhost";
	$dbUser = "root";
	$dbPass = "pass";
	$dbDatabase = "truktales";

	// Connect to DB
	$dbhandle = mysql_connect($dbHost, $dbUser) or die("Could not connect");
	mysql_select_db($dbDatabase, $dbhandle) or die ("could not select DB"); 

?>