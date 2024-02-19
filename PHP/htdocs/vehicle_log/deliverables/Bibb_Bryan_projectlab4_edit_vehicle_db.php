<?php
//  Bryan Bibb, CPT283-W01, Feb 1 2024
//  Program: Project Lab 4: edit data with INSERT INTO database from user submitted form. Demonstrates the use of form input,
//           assigning PHP variables, and constructing a database query to create a new record.
//  Related: edit_vehicle.php
//
//  This PHP script is loaded with the POST array from edit_vehicle.php. The variables are filtered, tested, and then
//  send to the database a new record.

// filtering of variables
$vehicle_class = filter_input(INPUT_POST, 'vehicle_class');
$vehicle_make = filter_input(INPUT_POST, 'vehicle_make');
$vehicle_model = filter_input(INPUT_POST, 'vehicle_model');
$vehicle_year = filter_input(INPUT_POST, 'vehicle_year');
$vehicle_year_purchased = filter_input(INPUT_POST, 'vehicle_year_purchased');
$vehicle_color = filter_input(INPUT_POST, 'vehicle_color');
$vehicle_VIN = filter_input(INPUT_POST, 'vehicle_VIN');
$vehicle_license_tag = filter_input(INPUT_POST, 'vehicle_license_tag');
$vehicle_license_state = filter_input(INPUT_POST, 'vehicle_license_state');
$vehicle_purchase_price = filter_input(INPUT_POST, 'vehicle_purchase_price');
$vehicle_purchase_mileage = filter_input(INPUT_POST,'vehicle_purchase_mileage');
$vehicle_current_mileage = filter_input(INPUT_POST, 'vehicle_current_mileage');

// just in case the database has not been initialized
require_once('config.php');

// test to make sure that all fields have been filled in.
if (
    $vehicle_class == NULL || $vehicle_make == NULL || $vehicle_model == NULL || $vehicle_year == NULL ||
    $vehicle_year_purchased == NULL || $vehicle_color == NULL || $vehicle_VIN == NULL ||
    $vehicle_license_tag == NULL || $vehicle_license_state == NULL || $vehicle_purchase_price == NULL ||
    $vehicle_purchase_mileage == NULL || $vehicle_current_mileage == NULL) {
    $error = "Invalid product data. Check all fields and try again.";
    include('error.php');
} else {
// if so, the INSERT query runs, inserting each variable into its database column
    $query = 'UPDATE vehicles
              SET
                vehicle_class = :vehicle_class, 
                vehicle_make = :vehicle_make, 
                vehicle_model = :vehicle_model, 
                vehicle_year = :vehicle_year, 
                vehicle_year_purchased = :vehicle_year_purchased, 
                vehicle_color = :vehicle_color,
                vehicle_VIN = :vehicle_VIN, 
                vehicle_license_tag = :vehicle_license_tag, 
                vehicle_license_state = :vehicle_license_state, 
                vehicle_purchase_price = :vehicle_purchase_price, 
                vehicle_purchase_mileage = :vehicle_purchase_mileage, 
                vehicle_current_mileage = :vehicle_current_mileage
              WHERE
                  vehicle_VIN = :vehicle_VIN;';

    $statement = $db->prepare($query);
    // each value in the query statement must be bound to the PHP variable
    $statement->bindValue(':vehicle_class', $vehicle_class);
    $statement->bindValue(':vehicle_make', $vehicle_make);
    $statement->bindValue(':vehicle_model', $vehicle_model);
    $statement->bindValue(':vehicle_year', $vehicle_year);
    $statement->bindValue(':vehicle_year_purchased', $vehicle_year_purchased);
    $statement->bindValue(':vehicle_color', $vehicle_color);
    $statement->bindValue(':vehicle_VIN', $vehicle_VIN);
    $statement->bindValue(':vehicle_license_tag', $vehicle_license_tag);
    $statement->bindValue(':vehicle_license_state', $vehicle_license_state);
    $statement->bindValue(':vehicle_purchase_price', $vehicle_purchase_price);
    $statement->bindValue(':vehicle_purchase_mileage', $vehicle_purchase_mileage);
    $statement->bindValue(':vehicle_current_mileage', $vehicle_current_mileage);
    // query is executed after preparation
    $statement->execute();
    $statement->closeCursor();
    // after the record is created, load the page that views all vehicles
    header("Location: projectlab2.php");
}
?>