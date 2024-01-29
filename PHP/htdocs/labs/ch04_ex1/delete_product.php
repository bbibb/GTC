<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The delete_product.php page takes the user input product
            and category IDs and deletes them from the products table.
File:       delete_product.php
Related:    database.php, index.php
-->

<!-- database connection -->
<?php
require_once('database.php');

// Get IDs from user input and filter/validate INT values
$product_id = filter_input(INPUT_POST, 'product_id', FILTER_VALIDATE_INT);
$category_id = filter_input(INPUT_POST, 'category_id', FILTER_VALIDATE_INT);

// Delete the product from the database if the productID and categoryID exist in the table
if ($product_id != FALSE && $category_id != FALSE) {
    // construct query
    $query = 'DELETE FROM products
              WHERE productID = :product_id';
    // open query, prepare data, execute statement, and close
    $statement = $db->prepare($query);
    $statement->bindValue(':product_id', $product_id);
    $success = $statement->execute();
    $statement->closeCursor();    
}

// Display the Product List page
include('index.php');