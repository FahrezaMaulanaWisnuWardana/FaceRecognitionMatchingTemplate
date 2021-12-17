<?php

require_once('../db/connection.php');

class Face
{
    public function getFaces($id)
    {
        global $mysqli;
        $get_faces = "SELECT employee.fullname, face_data.value FROM face_data INNER JOIN employee ON face_data.employee_id = employee.employee_id WHERE employee.employee_id = $id";
        $result = mysqli_query($mysqli, $get_faces);

        while ($face_data = mysqli_fetch_array($result)) {
            $split = explode(",",$face_data['value']);
            $data[] = [
                'fullName' => $face_data['fullname'],
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
