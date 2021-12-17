<?php 

    require_once 'employee_method.php';
    $emp = new Employee();
    $request_method = $_SERVER['REQUEST_METHOD'];
    switch($request_method) {
        case 'GET':
            if(empty($_GET['id'])) {
                $emp->get_faces_employee();
            } else {

            }
            break;
    }
