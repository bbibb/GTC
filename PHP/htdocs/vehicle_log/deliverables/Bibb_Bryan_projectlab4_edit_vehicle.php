<?php
//  Bryan Bibb, CPT283-W01, Feb 1 2024
//  Program: Project Lab 4: edit data with INSERT INTO database from user submitted form. Demonstrates the use of form input,
//           assigning PHP variables, and constructing a database query to create a new record.
//  Related: edit_vehicle_db.php
//
//  This PHP script loads vehicle data to populate the edit form, received user input and sends all field
//  to edit_vehicle_db for adding to the database.

// receive VIN data input from vehicle list table

$vehicle_VIN = $_POST['vehicle_VIN'];

// database connection info
require_once('config.php');

// create select query to populate current values
$query = 'SELECT * FROM vehicles WHERE vehicle_VIN = :vehicle_VIN';
$statement = $db->prepare($query);
$statement->bindValue("vehicle_VIN", $vehicle_VIN);
$statement->execute();
$vehicle = $statement->fetch();
$statement->closeCursor();
?>

<html lang="en">

<?php include('header.php') ?>

// Form to display data fields with current values that can be replaced
<body class="bg-secondary"> <!-- gray background -->

<div class="card-header py-3 text-center text-light m-5 my-3">
    <h1>Edit Vehicle Information</h1>
</div>
<!-- The outer container keeps the two inner containers in sync viz. width -->
<div class="container px-5">
<div class="container px-lg-3 py-0 bg-light">
    <!-- The form creates a POST array and sends to add_vehicle.php -->
    <form action="edit_vehicle_db.php" method="post"
          id="add_vehicle_form">
        <!-- The form is divided into two columns for ease of use -->
        <div class="row py-5 mx-5 justify-content-center">
            <div class="col-lg-4">
        <!-- Each input box creates a variable with a name that matches the database columns (for convenience)-->
        <div class="mb-3 mt-3">
            <label for="class" class="form-label">Class:</label>
            <input type="text" class="form-control" id="class" value="<?php echo $vehicle['vehicle_class']; ?>"
                   placeholder="Enter vehicle class" name="vehicle_class">
        </div>
        <div class="mb-3">
            <label for="make" class="form-label">Make:</label>
            <input type="text" class="form-control" id="make" value="<?php echo $vehicle['vehicle_make']; ?>"
                   placeholder="Enter vehicle make" name="vehicle_make">
        </div>
        <div class="mb-3">
            <label for="model" class="form-label">Model:</label>
            <input type="text" class="form-control" id="model" value="<?php echo $vehicle['vehicle_model']; ?>"
                   placeholder="Enter vehicle model" name="vehicle_model">
        </div>
        <div class="mb-3">
            <label for="year" class="form-label">Year:</label>
            <input type="text" class="form-control" id="year" value="<?php echo $vehicle['vehicle_year']; ?>"
                   placeholder="Enter vehicle year" name="vehicle_year">
        </div>
        <div class="mb-3">
            <label for="year_purchased" class="form-label">Year Purchased:</label>
            <input type="text" class="form-control" id="year_purchased" value="<?php echo $vehicle['vehicle_year_purchased']; ?>"
                   placeholder="Enter year purchased" name="vehicle_year_purchased">
        </div>
        <div class="mb-3">
            <label for="color" class="form-label">Color:</label>
            <input type="text" class="form-control" id="color" value="<?php echo $vehicle['vehicle_color']; ?>"
                   placeholder="Enter vehicle color" name="vehicle_color">
        </div>
            </div>
            <div class="col-lg-4">
        <div class="mb-0 py-3">
            <label for="vin" class="form-label">VIN:</label>
            <input type="text" class="form-control" id="vin" value="<?php echo $vehicle['vehicle_VIN']; ?>"
                   placeholder="Enter vehicle identification number" name="vehicle_VIN">
        </div>
        <div class="mb-3">
            <label for="tag" class="form-label">License Plate:</label>
            <input type="text" class="form-control" id="tag" value="<?php echo $vehicle['vehicle_license_tag']; ?>"
                   placeholder="Enter vehicle tag" name="vehicle_license_tag">
        </div>
        <div class="mb-3">
            <label for="state" class="form-label">State:</label>
            <input type="text" class="form-control" id="state" value="<?php echo $vehicle['vehicle_license_state']; ?>"
                   placeholder="Enter state where registered" name="vehicle_license_state">
        </div>
        <div class="mb-3">
            <label for="price" class="form-label">Price:</label>
            <input type="text" class="form-control" id="price" value="<?php echo $vehicle['vehicle_purchase_price']; ?>"
                   placeholder="Enter vehicle purchased price" name="vehicle_purchase_price">
        </div>
        <div class="mb-3">
            <label for="purchase_mileage" class="form-label">Purchase mileage:</label>
            <input type="text" class="form-control" id="purchase_mileage" value="<?php echo $vehicle['vehicle_purchase_mileage']; ?>"
                   placeholder="Enter mileage when purchased" name="vehicle_purchase_mileage">
        </div>
        <div class="mb-3">
            <label for="current_mileage" class="form-label">Current mileage:</label>
            <input type="text" class="form-control" id="current_mileage" value="<?php echo $vehicle['vehicle_current_mileage']; ?>"
                   placeholder="Enter current mileage" name="vehicle_current_mileage">
        </div>
        <!-- Submit button triggers the POST method and sending of data to edit_vehicle_db.php -->
        <button type="submit" class="btn btn-primary" value="edit vehicle">Submit</button>
        </div>
        </div>
    </form>

</div>
</div>
</body>
</html>