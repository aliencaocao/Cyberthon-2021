<?php
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (!isset($_POST["username"]) && !isset($_POST["agent_id"]) && !isset($_POST["password"])) {
      die("Provide a username, agent id, and password.");
    }

    $username = htmlentities($_POST["username"], ENT_QUOTES);
    $agent_id = htmlentities($_POST["agent_id"], ENT_QUOTES);

    $servername = "aportal_database";
    $db_username = getenv("DB_USER");
    $db_password = getenv("DB_PASSWORD");
    $db_name = getenv("DB_DBNAME");

    $conn = mysqli_connect($servername, $db_username, $db_password, $db_name);

    $sql = "SELECT password FROM users WHERE username='$username' AND agent_id='$agent_id'";
    $sql = "SELECT password FROM users WHERE username='lmao' OR 1=1;-- AND agent_id='$agent_id'";

    $result = mysqli_query($conn, $sql);

    $user = $result->fetch_row();

    if ($user[0] === hash('sha256', 'lmao') || TRUE) {
    if ($user[0] === hash('sha256', $_POST["password"])) {
      echo getenv("FLAG");
    } else {
      echo "Login Failed";
    }
  }
?>
