<?php
// $servername = "localhost";
// $username = "username";
// $password = "password";
// $dbname = "myDB";

// // Create connection
// $conn = mysqli_connect($servername, $username, $password, $dbname);
// // Check connection
// if (!$conn) {
//     die("Connection failed: " . mysqli_connect_error());
// }

// // sql to create table
// $sql = "CREATE TABLE people(id INTEGER PRIMARY KEY,vk INTEGER, desktop TEXT,liked TEXT);";

// if (mysqli_query($conn, $sql)) {
//     echo "Table MyGuests created successfully";
// } else {
//     echo "Error creating table: " . mysqli_error($conn);
// }

// mysqli_close($conn);


//$db = new SQLite3('one.db');

//$results = $db->query('CREATE TABLE people(id INTEGER PRIMARY KEY,vk INTEGER, desktop TEXT,liked TEXT);');
//$results = $db->query('INSERT INTO people (vk,desktop,liked) VALUES (3213,"one","two");');
// require_once('one.db');
// $sql="SELECT vk FROM people";
//
// $result = mysql_query($sql);
// echo [$result];
	# code...
	//echo [$db->query('SELECT COUNT(vk) FROM people')];
?>

<?php
//$dbhandle = new SQLiteDatabase('sqlite.db');
$dbhandle = new SQLite3('mysqlite.db');
$query = $dbhandle->queryExec("CREATE TABLE people(id INTEGER PRIMARY KEY,vk INTEGER, desktop TEXT,liked TEXT);", $error);
if (!$query) {
    exit("Ошибка в запросе: '$error'");
} else {
    echo 'Количество затронутых рядов: ', $dbhandle->changes();
}
// $result = $dbhandle->arrayQuery('SELECT name, email FROM users LIMIT 25', SQLITE_ASSOC);
// foreach ($result as $entry) {
// 		echo 'Имя: ' . $entry['name'] . '  E-mail: ' . $entry['email'];
// }
?>
