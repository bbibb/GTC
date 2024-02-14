<!DOCTYPE html>
<html lang="en">
<!--    Bryan Bibb, CPT283-W01, Feb 1 2024
        Program: Project Lab 2: database test. Demonstrates the database connection and
                 the ability to get data from the server and display it nicely in a table. -->
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <meta name="description" content="" />
    <meta name="author" content="Bryan Bibb" />
    <title>Bryan Bibb | CPT283: PHP Programming | Vehicle Log</title>
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

<!-- PHP to get table data from the database. All columns are returned, but the table uses only
12 of the 15 columns in the vehicles. It seemed nicer to use a * wildcard than to type out 12 column names-->
<?php require('config.php');

    $query = 'SELECT * FROM vehicles ORDER BY vehicle_class';
    $statement = $db->prepare($query);
    $statement->execute();
    $vehicles = $statement->fetchAll();
    $statement->closeCursor();
?>
<!--table header-->
<div class="card-header py-3 text-center text-light m-5 my-3">
<h1>Vehicle Data</h1>
</div>
<div class="container container-fluid px-lg-3 py-0">
    <table class="table table-striped table-bordered table-responsive bg-light">
    <tr>
        <th>Class</th>
        <th>Make</th>
        <th>Model</th>
        <th>Year</th>
        <th>Purchased</th>
        <th>Color</th>
        <th>VIN</th>
        <th>Tag</th>
        <th>State</th>
        <th>Price</th>
        <th>Original Mileage</th>
        <th>Current Mileage</th>
    </tr>

<!-- PHP foreach loop prints out the cells for each row, one at a time-->
<?php foreach ($vehicles as $vehicle) : ?>
    <tr>
        <td><?php echo $vehicle['vehicle_class']; ?></td>
        <td><?php echo $vehicle['vehicle_make']; ?></td>
        <td><?php echo $vehicle['vehicle_model']; ?></td>
        <td><?php echo $vehicle['vehicle_year']; ?></td>
        <td><?php echo $vehicle['vehicle_year_purchased']; ?></td>
        <td><?php echo $vehicle['vehicle_color']; ?></td>
        <td><?php echo $vehicle['vehicle_VIN']; ?></td>
        <td><?php echo $vehicle['vehicle_license_tag']; ?></td>
        <td><?php echo $vehicle['vehicle_license_state']; ?></td>
        <td><?php echo $vehicle['vehicle_purchase_price']; ?></td>
        <td><?php echo $vehicle['vehicle_purchase_mileage']; ?></td>
        <td><?php echo $vehicle['vehicle_current_mileage']; ?></td>
        <td>
            <form action="edit_vehicle.php" method="post"
                id="edit_vehicle_form">
            <button type="submit" class="btn btn-outline-primary btn-sm" name="vehicle_VIN"
                    value="<?php echo $vehicle['vehicle_VIN'];?>">edit</button>
            </form>
        </td>
    </tr>
    <?php endforeach; ?>
    </table>
</div>
<div class="row justify-content-center">
<div class="card py-3 text-center bg-light m-5 my-3 col-3">
    <h3><a class="link-secondary" href="projectlab3.php">Add a new vehicle</a></h3>
</div>
</div>
</body>
</html>
