<!DOCTYPE html>
<html lang="en">
<!--    Bryan Bibb, CPT283-W01, Feb 1 2024
        Program: Project Lab 2: database test. Demonstrates the database connection and
                 the ability to get data from the server and display it nicely in a table. -->

<?php include('header.php') ?>

<body class="bg-secondary">

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
