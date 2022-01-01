<?php include_once("../../db/connection.php"); ?>

<?php

$title = "Employee Table";

$select_all_query = "SELECT * FROM employee";

$result = mysqli_query($mysqli, $select_all_query);

?>

<?php include_once("../../partial/header.php") ?>

<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">

        <?php include_once("../../partial/sidebar.php") ?>

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <?php include_once("../../partial/topbar.php") ?>

                <!-- Begin Page Content -->
                <div class="container-fluid">

                    <!-- Page Heading -->
                    <h1 class="h3 mb-2 text-gray-800">Data Karyawan</h1>

                    <!-- DataTales Example -->
                    <div class="card shadow mb-4">
                        <div class="card-header py-3">
                            <h6 class="m-0 font-weight-bold text-primary">Tabel Karyawan</h6>
                        </div>
                        <div class="card-body">
                            <div class="table-responsive">
                                <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                                    <thead>
                                        <tr>
                                            <th>Nama Lengkap</th>
                                            <th>Jenis Kelamin</th>
                                            <th>Tanggal Lahir</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <?php
                                        while ($item_data = mysqli_fetch_array($result)) {
                                        ?>
                                            <tr>
                                                <td><?= $item_data['fullname'] ?></td>
                                                <td><?= $item_data['gender'] ?></td>
                                                <td><?= $item_data['birth_date'] ?></td>
                                            </tr>
                                        <?php } ?>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>

                </div>
                <!-- /.container-fluid -->

            </div>
            <!-- /.container-fluid -->

        </div>
        <!-- End of Main Content -->
    </div>

    <?php include_once("../../partial/footer.php") ?>

</body>

</html>