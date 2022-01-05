<?php include_once("db/connection.php"); ?>


<?php

$title = "Dashboard";

?>

<?php include_once("partial/header.php") ?>


<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">

        <?php include_once("partial/sidebar.php") ?>

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <?php include_once("partial/topbar.php") ?>

                <!-- Begin Page Content -->
                <div class="container-fluid">

                    <div class="row">
                        <div class="col-12 mb-4">
                            <div class="card shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="text-center">
                                        <a href="http://localhost/FaceRecognitionMatchingTemplate/command-absens.php?type=absen">
                                            <div class="text-lg font-weight-bold text-primary text-uppercase mb-1">Jalankan Absensi</div>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="card shadow h-100 py-2">
                                <div class="card-body">
                                    <div class="text-center">
                                        <a href="http://localhost/FaceRecognitionMatchingTemplate/command-absens.php?type=rekam">
                                            <div class="text-lg font-weight-bold text-primary text-uppercase mb-1">Jalankan Rekam Wajah</div>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
                <!-- /.container-fluid -->

            </div>
            <!-- End of Main Content -->

            <?php include_once("partial/footer.php") ?>

</body>

</html>