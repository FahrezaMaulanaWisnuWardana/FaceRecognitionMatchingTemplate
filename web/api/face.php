<?php 

    require_once 'face_method.php';
    $face = new Face();
    $request_method = $_SERVER['REQUEST_METHOD'];
    switch($request_method) {
        case 'GET':
            $face->getFaces($_GET['id']);
    }

?>