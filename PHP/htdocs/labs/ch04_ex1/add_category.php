<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The add_category.php page takes the user input category
            name and inserts it into the MySQL database.
File:       add_category.php
Related:    category_list.php, database.php, error.php
-->

<?php
// Get the category name for the new category
$name = filter_input(INPUT_POST, 'name');

// Validate the user input and pass to error.php if the category name is not set
if ($name == NULL) {
    $error = "Invalid category data. Check all fields and try again";
    include('error.php');
} else {
    require_once('database.php');

    // Add the new category to the categories database
    // insert into the categories database a new row containing the category_name value, which is
    // bound to the $name variable
    $query = 'INSERT INTO categories
                (categoryName)
              VALUES
                (:category_name)';

    // open the query, prepare the data to be saved, write it to the database, and close.
    $statement = $db->prepare($query);
    $statement->bindValue(':category_name', $name);
    $statement->execute();
    $statement->closeCursor();

    //Display the Category List page, including the new category that was just added
    include('category_list.php');

}
?>