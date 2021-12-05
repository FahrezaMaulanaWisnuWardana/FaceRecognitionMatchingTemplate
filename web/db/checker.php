<?php

include_once dirname(__DIR__) . '...\vendor\autoload.php';

use Dotenv\Dotenv as dotEnv;

$dotenv = dotEnv::createImmutable(__DIR__);
$dotenv->load();

$base_url = $_ENV["BASE_URL"];

$db_host = $_ENV["DB_HOST"];
$db_username = $_ENV["DB_USERNAME"];
$db_name = $_ENV["DB_NAME"];

?>