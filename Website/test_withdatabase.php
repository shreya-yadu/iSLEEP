<?php
   class MyDB extends SQLite3 {
      function __construct() {
         $this->open('/Users/Shreya/Desktop/server/sys.db');
      }
   }
   
   $db = new MyDB();
   if(!$db) {
      #echo $db->lastErrorMsg();
   } else {
      #echo "Opened database successfully\n";
   }

   $sql =<<<EOF
      SELECT data from message order by time desc limit 2;
EOF;

   $ret = $db->query($sql);
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
      echo $row['data']/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000;
      #echo "NAME = ". $row['NAME'] ."\n";
      #echo "ADDRESS = ". $row['ADDRESS'] ."\n";
      #echo "SALARY = ".$row['SALARY'] ."\n\n";
   }
   #echo "Operation done successfully\n";
   $db->close();
?>