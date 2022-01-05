<?php
if ($_GET['type'] == "absen") {
    shell_exec("python xa.py");
    header("location: web/index.php");
} elseif ($_GET['type'] == "rekam") {
    shell_exec("python python-gui-cam-rekam-wajah.py");
    header("location: web/index.php");
}
