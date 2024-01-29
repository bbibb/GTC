<?php
// Bryan Bibb, CPT283-W01, Jan 26, 2024
// Program:  Guitar Shop
// Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
//           inventory items and product categories.
// File:     model/product_db.php
//
// This file uses PHP code to construct and run queries against the Guitar Shop database. The syntax for
//     each is the same structure for each function: the database is opened, the query is constructed and prepared
// and then executed and closed. The results of the query are then passed back to the calling via a $variable.
// get a list of products currently in the database with a given categoryID
function get_products_by_category($category_id) {
    global $db;
    $query = 'SELECT * FROM products
              WHERE products.categoryID = :category_id
              ORDER BY productID';
    $statement = $db->prepare($query);
    $statement->bindValue(':category_id', $category_id);
    $statement->execute();
    $products = $statement->fetchAll();
    $statement->closeCursor();
    return $products;
}

// get a specific product from the database with a given productID
function get_product($product_id) {
    global $db;
    $query = 'SELECT * FROM products
              WHERE productID = :product_id';
    $statement = $db->prepare($query);
    $statement->bindValue(':product_id', $product_id);
    $statement->execute();
    $product = $statement->fetch();
    $statement->closeCursor();
    return $product;
}

// delete a specific product from the database with a given productID
function delete_product($product_id) {
    global $db;
    $query = 'DELETE FROM products
              WHERE productID = :product_id';
    $statement = $db->prepare($query);
    $statement->bindValue(':product_id', $product_id);
    $statement->execute();
    $statement->closeCursor();
}

// add a product to the database with 4 variables passed to INSERT INTO SQL statement
function add_product($category_id, $code, $name, $price) {
    global $db;
    $query = 'INSERT INTO products
                 (categoryID, productCode, productName, listPrice)
              VALUES
                 (:category_id, :code, :name, :price)';
    $statement = $db->prepare($query);
    $statement->bindValue(':category_id', $category_id);
    $statement->bindValue(':code', $code);
    $statement->bindValue(':name', $name);
    $statement->bindValue(':price', $price);
    $statement->execute();
    $statement->closeCursor();
}
?>