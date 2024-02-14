<!DOCTYPE html>
<html>
<!--    Bryan Bibb, CPT283-W01, Feb 1 2024
        Program: Project Lab 3: form data input with INSERT INTO database. Demonstrates the use of form input,
                 assigning PHP variables, and constructing a database query to create a new record.
        Related: config.php, error.php, projectlab2.php, add_vehicle.php -->

<?php include('header.php') ?>

<body class="bg-secondary"> <!-- gray background -->

<!--Page header with white background and centered text -->
<div class="card-header py-3 text-center text-light m-5 my-3">
    <h1>Add a Vehicle</h1>
</div>
<!-- The outer container keeps the two inner containers in sync viz. width -->
<div class="container px-5">
<div class="container px-lg-3 py-0 bg-light">
    <!-- The form creates a POST array and sends to add_vehicle.php -->
    <form action="add_vehicle_db.php" method="post"
          id="add_vehicle_form">
        <!-- The form is divided into two columns for ease of use -->
        <div class="row py-5 mx-5 justify-content-center">
            <div class="col-lg-4">
        <!-- Each input box creates a variable with a name that matches the database columns (for convenience)-->
        <div class="mb-3 mt-3">
            <label for="class" class="form-label">Class:</label>
            <input type="text" class="form-control" id="class" placeholder="Enter vehicle class" name="vehicle_class">
        </div>
        <div class="mb-3">
            <label for="make" class="form-label">Make:</label>
            <input type="text" class="form-control" id="make" placeholder="Enter vehicle make" name="vehicle_make">
        </div>
        <div class="mb-3">
            <label for="model" class="form-label">Model:</label>
            <input type="text" class="form-control" id="model" placeholder="Enter vehicle model" name="vehicle_model">
        </div>
        <div class="mb-3">
            <label for="year" class="form-label">Year:</label>
            <input type="text" class="form-control" id="year" placeholder="Enter vehicle year" name="vehicle_year">
        </div>
        <div class="mb-3">
            <label for="year_purchased" class="form-label">Year Purchased:</label>
            <input type="text" class="form-control" id="year_purchased" placeholder="Enter year purchased" name="vehicle_year_purchased">
        </div>
        <div class="mb-3">
            <label for="color" class="form-label">Color:</label>
            <input type="text" class="form-control" id="color" placeholder="Enter vehicle color" name="vehicle_color">
        </div>
            </div>
            <div class="col-lg-4">
        <div class="mb-0 py-3">
            <label for="vin" class="form-label">VIN:</label>
            <input type="text" class="form-control" id="vin" placeholder="Enter vehicle identification number" name="vehicle_VIN">
        </div>
        <div class="mb-3">
            <label for="tag" class="form-label">License Plate:</label>
            <input type="text" class="form-control" id="tag" placeholder="Enter vehicle tag" name="vehicle_license_tag">
        </div>
        <div class="mb-3">
            <label for="state" class="form-label">State:</label>
            <input type="text" class="form-control" id="state" placeholder="Enter state where registered" name="vehicle_license_state">
        </div>
        <div class="mb-3">
            <label for="price" class="form-label">Price:</label>
            <input type="text" class="form-control" id="price" placeholder="Enter vehicle purchased price" name="vehicle_purchase_price">
        </div>
        <div class="mb-3">
            <label for="purchase_mileage" class="form-label">Purchase mileage:</label>
            <input type="text" class="form-control" id="purchase_mileage" placeholder="Enter mileage when purchased" name="vehicle_purchase_mileage">
        </div>
        <div class="mb-3">
            <label for="current_mileage" class="form-label">Current mileage:</label>
            <input type="text" class="form-control" id="current_mileage" placeholder="Enter current mileage" name="vehicle_current_mileage">
        </div>
        <!-- Submit button triggers the POST method and sending of data to add_vehicle.php -->
        <button type="submit" class="btn btn-primary" value="add vehicle">Submit</button>
        </div>
        </div>
    </form>

</div>
</div>
</body>
</html>