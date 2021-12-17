<?php
require_once('../db/connection.php');

class Employee
{
    // select all employee data
    public function get_employee()
    {
        global $mysqli;
        $select_all_query = "SELECT * FROM employee";
        $data = array();
        $result = mysqli_query($mysqli, $select_all_query);
        while ($row = mysqli_fetch_object($result)) {
            $data[] = $row;
        }

        $response = array(
            'status' => 1,
            'message' => 'Berhasil',
            'data' => $data
        );

        header('Content-Type: application/json');
        echo json_encode($response);
    }

    // showing all faces employee data
    public function get_faces_employee()
    {
        global $mysqli;
        $get_faces = "SELECT employee.fullname, face_data.value FROM face_data INNER JOIN employee ON face_data.employee_id = employee.employee_id";
        $result = mysqli_query($mysqli, $get_faces);
        while ($row = mysqli_fetch_object($result)) {
            // splitting of column value by "," character
            $split = explode(",",$row->value);
            $data[] = [
                'fullName' => $row->fullname,
                'value'=> $split
            ];
        }
        $response = array(
            'status' => 1,
            'message' => 'Berhasil',
            'face_data' => $data
        );

        header('Content-Type: application/json, Authorization: ');
        echo json_encode($response);
    }
}
