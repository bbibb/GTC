<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The delete_product.php page takes the user input product
            and category IDs and deletes them from the products table.
File:       delete_category.php
Related:    database.php, category_list.php
-->

<?php

// // Get categoryID from user input and filter/validate INT values
$category_id = filter_input(INPUT_POST, 'category_id', FILTER_VALIDATE_INT);

// Delete that category from the database, if it is found in the table
if ($category_id == NULL || $category_id == FALSE) {
    // error message if not found
    $error = "Invalid category.";
    include('error.php');
} else {
    // database connection
    require_once('database.php');

    // construct query
    $query = 'DELETE FROM categories
               WHERE categoryID = :category_id';
    // open query, prepare data, execute statement, and close
    $statement = $db->prepare($query);
    $statement->bindValue(':category_id', $category_id);
    $statement->execute();
    $statement->closeCursor();

    // load the category_list.php page to display list including new category
    include('category_list.php');
}
?>

