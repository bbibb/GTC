<!DOCTYPE html>
<!--    Bryan Bibb, CPT283-W01, Feb 1 2024
        Program: Project Lab 3: form data input with INSERT INTO database. Demonstrates the use of form input,
                 assigning PHP variables, and constructing a database query to create a new record.
        Related: config.php, error.php, projectlab2.php, projectlab3.php, add_vehicle.php -->
<!-- This is a landing page that shows information about the program and includes placeholders
     links to the main sections. The first section that is working is the ability to view all
      vehicles (projectlab2.php) and to add a vehicle to the database (projectlab3.php) -->
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="Bryan Bibb" />
        <title>Vehicle Log - Bryan Bibb</title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <!-- Bootstrap icons-->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body class="bg-secondary">
        <!-- Responsive navbar-->
        <nav class="navbar navbar-expand-lg navbar-dark text-light bg-dark">
            <div class="container px-lg-5">
                <a class="navbar-brand" href="/index.php">Bryan Bibb</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="index.php">Home</a></li>
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="projectlab2.php">Vehicles</a></li>
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="">Fuel</a></li>
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="">Maintenance</a></li>
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="">Admin</a></li>
                        <li class="nav-item"><a class="nav-link" target="_self" href="/index.php">CPT283 Work</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Header-->
        <header class="py-5">
            <div class="container px-lg-5">
                <div class="p-1 p-lg-1 bg-light rounded-3 text-center row justify-content-center text-dark d-flex">
<!-- header is divided into two columns, one for the title and one for the description -->
                    <div class="m-3 m-lg-5 col-4 flex-fill">
                        <h1 class="display-5 fw-bold">Vehicle Log</h1>
                        <p class="fs-4">Welcome to the Vehicle Log Web Application <br>
                            Developed by Bryan Bibb for CPT283 PHP Programming, at
                            <a href="https://www.gvltec.edu/academics_learning/business-computer/computer_technology/index.html" target="_blank ">Greenville Technical College</a>.</p>
                        <p class="fs-4">
                            <a class="btn btn-primary btn-lg" href="#!">Login</a>

                        </p>
                    </div>
                    <div class="m-4 m-lg-5 col-4">
                    <ul class="list-group text-start list-group-flush">
                        <li class="list-group-item">Track your fleet of vehicles</li>
                        <li class="list-group-item">Add and edit vehicle information</li>
                        <li class="list-group-item">Monitor fuel usage and calculate costs</li>
                        <li class="list-group-item">Document maintenance history and expenses</li>
                        <li class="list-group-item">Generate vehicle reports and fuel/maintenance records</li>
                        <li class="list-group-item">Administrator account: edit users, add data entities, export and delete records</li>
                    </ul>
                </div>
                </div>
                </div>
                </div>
            </div>
        </header>

        <!-- Page Content-->
<!-- One box for each section of the application with a link. Each link gets a custom icon from
     the Bootstrap svg icon collection -->
        <section class="pt-4">
            <div class="container px-lg-5">
                <!-- Page Features-->
                <div class="row gx-lg-5">
                    <div class="col-lg-6 col-xl-3 mb-5">
                        <div class="card bg-light border-0 h-100">
                            <div class="card-body text-center p-4 p-lg-5 pt-0 pt-lg-0">
<!-- Change this temporary URL when the filenames get refactored at the end -->
                                <a href="projectlab2.php" class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><i class="bi bi-car-front"></i></a>
                                <h2 class="fs-4 fw-bold">Vehicles</h2>
                                <p class="mb-0">View data about all fleet vehicles</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-xl-3 mb-5">
                        <div class="card bg-light border-0 h-100">
                            <div class="card-body text-center p-4 p-lg-5 pt-0 pt-lg-0">
                                <div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><i class="bi bi-fuel-pump"></i></div>
                                <h2 class="fs-4 fw-bold">Fuel Data</h2>
                                <p class="mb-0">View fuel usage and cost report</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-xl-3 mb-5">
                        <div class="card bg-light border-0 h-100">
                            <div class="card-body text-center p-4 p-lg-5 pt-0 pt-lg-0">
                                <div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><i class="bi bi-wrench-adjustable"></i></div>
                                <h2 class="fs-4 fw-bold">Maintenance</h2>
                                <p class="mb-0">View maintenance history and costs</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 col-xl-3 mb-5">
                        <div class="card bg-light border-0 h-100">
                            <div class="card-body text-center p-4 p-lg-5 pt-0 pt-lg-0">
                                <div class="feature bg-primary bg-gradient text-white rounded-3 mb-4 mt-n4"><i class="bi bi-database-fill-gear"></i></div>
                                <h2 class="fs-4 fw-bold">Admin</h2>
                                <p class="mb-0">Administrative area</p>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>

<!--  Temporary links for the Project Lab assignments    -->
        <div class="row justify-content-center">
            <div class="card py-3 text-center text-dark m-5 my-3 col-3">
                <h4>Temp Links for Project Labs</a></h4>
                <h5><a href="projectlab2.php">ProjectLab2.php</a></h5>
                <h5><a href="projectlab3.php">ProjectLab3.php</a></h5>
            </div>
        </div>

        <!-- Footer-->
        <footer class="py-5 bg-dark">
            <div class="container"><p class="m-0 text-center text-white">Copyright &copy; Bryan Bibb 2024</p></div>
        </footer>
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
    </body>
</html>
