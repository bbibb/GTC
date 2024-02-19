<?php

include('classes/test.php');

$vehicle_list = new Test();
$vehicles = $vehicle_list->getVehicles();
//print_r($vehicles);
?>

<HTML>

<?php include('includes/header.php') ?>

<body class="bg-secondary">
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

    <?php
        foreach ($vehicles as $vehicle) { ?>
    <tr>
        <td><?= $vehicle['vehicle_class']; ?></td>
        <td><?= $vehicle['vehicle_make']; ?></td>
        <td><?= $vehicle['vehicle_model']; ?></td>
        <td><?= $vehicle['vehicle_year']; ?></td>
        <td><?= $vehicle['vehicle_year_purchased']; ?></td>
        <td><?= $vehicle['vehicle_color']; ?></td>
        <td><?= $vehicle['vehicle_VIN']; ?></td>
        <td><?= $vehicle['vehicle_license_tag']; ?></td>
        <td><?= $vehicle['vehicle_license_state']; ?></td>
        <td><?= $vehicle['vehicle_purchase_price']; ?></td>
        <td><?= $vehicle['vehicle_purchase_mileage']; ?></td>
        <td><?= $vehicle['vehicle_current_mileage']; ?></td>
        <td>
            <form action="edit_vehicle.php" method="post"
                id="edit_vehicle_form">
            <button type="submit" class="btn btn-outline-primary btn-sm" name="vehicle_VIN"
                    value="<?php echo $vehicle['vehicle_VIN'];?>">edit</button>
            </form>
        </td>
    <?php
        }
        ?>
    </tr>
    </table>
</HTML>