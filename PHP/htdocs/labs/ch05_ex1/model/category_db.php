<?php
// Bryan Bibb, CPT283-W01, Jan 26, 2024
// Program:  Guitar Shop
// Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
//           inventory items and product categories.
// File:     model/category_db.php
// This file uses PHP code to construct and run queries against the Guitar Shop database. The syntax for
//     each is the same structure for each function: the database is opened, the query is constructed and prepared
// and then executed. The results of the query are then passed back to the calling via a $variable.
function get_categories() {
// get a list of the categories currently in the database
    global $db;
    $query = 'SELECT * FROM categories
              ORDER BY categoryID';
    $statement = $db->prepare($query);
    $statement->execute();
    return $statement;    
}

// get a specific category name from the database column categoryID
function get_category_name($category_id) {
    global $db;
    $query = 'SELECT * FROM categories
              WHERE categoryID = :category_id';    
    $statement = $db->prepare($query);
    $statement->bindValue(':category_id', $category_id);
    $statement->execute();    
    $category = $statement->fetch();
    $statement->closeCursor();    
    $category_name = $category['categoryName'];
    return $category_name;
}

// add a category into the database from the $name parameter passed to the function
function add_category($name) {
    global $db;
    $query = 'INSERT INTO categories (categoryName) VALUES (:name)';
    $statement = $db->prepare($query);
    $statement->bindValue(':name', $name);
    $statement->execute();
    $statement->closeCursor();
}

// delete a category from the database as identified by $category_id
function delete_category($category_id) {
    global $db;
    $query = 'DELETE FROM categories WHERE categoryID = :category_id';
    $statement = $db->prepare($query);
    $statement->bindValue(':category_id', $category_id);
    $statement->execute();
    $statement->closeCursor();

}
?>