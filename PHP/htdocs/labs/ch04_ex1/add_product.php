<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The add_product.php page takes the user input for
            the new product from add_product_form.php, inserts that data it into the MySQL database,
            and redisplays the list on the index page.
File:       add_product.php
Related:    indexold.php, database.php, error.php, add_product_form.php
-->

<?php
// Get the product data from user input. Validate the INT and FLOAT values and save all input to variables.
$category_id = filter_input(INPUT_POST, 'category_id', FILTER_VALIDATE_INT);
$code = filter_input(INPUT_POST, 'code');
$name = filter_input(INPUT_POST, 'name');
$price = filter_input(INPUT_POST, 'price', FILTER_VALIDATE_FLOAT);

// If any of the variables are not set correctly, trigger an error and pass to error.php
if ($category_id == NULL || $category_id == FALSE || $code == NULL || 
        $name == NULL || $price == NULL || $price == FALSE) {
    $error = "Invalid product data. Check all fields and try again.";
    include('error.php');
// If all is well, connect to the database
} else {
    require_once('database.php');

    // Add the product to the database through a formatted SQL query
    // Insert data into a new row with values from the variables set above.
    $query = 'INSERT INTO products
                 (categoryID, productCode, productName, listPrice)
              VALUES
                 (:category_id, :code, :name, :price)';
    // Open the query, prepare the data, execute the statement, and close
    $statement = $db->prepare($query);
    $statement->bindValue(':category_id', $category_id);
    $statement->bindValue(':code', $code);
    $statement->bindValue(':name', $name);
    $statement->bindValue(':price', $price);
    $statement->execute();
    $statement->closeCursor();

    // Display the Product List (index.php), now with the new row of product data
    include('index.php');
}
?>