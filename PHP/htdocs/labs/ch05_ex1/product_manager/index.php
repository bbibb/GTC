<?php
//Bryan Bibb, CPT283-W01, Jan 26, 2024
//Program:  Guitar Shop
//Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
//          inventory items and product categories.
//File:     product_manager/indexold.php
//
//This master page for the product manager application starts by importing the code for the three
//"model" php pages. These define all of the variables and interface with the database, and then
// return values to the index "view" page for sending to the browser.
require('../model/database.php');
require('../model/product_db.php');
require('../model/category_db.php');

// the rest of the script provides functionality for different actions based on user choice
// if there is no input, the default is to load the product list.
$action = filter_input(INPUT_POST, 'action');
if ($action == NULL) {
    $action = filter_input(INPUT_GET, 'action');
    if ($action == NULL) {
        $action = 'list_products';
    }
}

// code to load the product list of a particular category by passing the category_id to three functions:
// get_categories, get_category_name, and get_products_by_category. These are defined in category_db.php
if ($action == 'list_products') {
    $category_id = filter_input(INPUT_GET, 'category_id', 
            FILTER_VALIDATE_INT);
    if ($category_id == NULL || $category_id == FALSE) {
        $category_id = 1;
    }
    $category_name = get_category_name($category_id);
    $categories = get_categories();
    $products = get_products_by_category($category_id);
// load product_list.php to display products in chosen category
    include('product_list.php');

// code to delete a product with a given product_id with delete_product() function
} else if ($action == 'delete_product') {
    $product_id = filter_input(INPUT_POST, 'product_id', 
            FILTER_VALIDATE_INT);
    $category_id = filter_input(INPUT_POST, 'category_id', 
            FILTER_VALIDATE_INT);

    // error message if the product_id is incorrect or null
    if ($category_id == NULL || $category_id == FALSE ||
            $product_id == NULL || $product_id == FALSE) {
        $error = "Missing or incorrect product id or category id.";
        include('../errors/error.php');
    } else {
        delete_product($product_id);
        header("Location: .?category_id=$category_id");
    }
} else if ($action == 'show_add_form') {
    $categories = get_categories();
    include('product_add.php');    
// user input for code, name, and price
} else if ($action == 'add_product') {
    $category_id = filter_input(INPUT_POST, 'category_id', 
            FILTER_VALIDATE_INT);
    $code = filter_input(INPUT_POST, 'code');
    $name = filter_input(INPUT_POST, 'name');
    $price = filter_input(INPUT_POST, 'price');
    if ($category_id == NULL || $category_id == FALSE || $code == NULL ||
            $name == NULL || $price == NULL || $price == FALSE) {
        $error = "Invalid product data. Check all fields and try again.";
        include('../errors/error.php');
    } else { 
        add_product($category_id, $code, $name, $price);
// redirect to show the products in the current category
        header("Location: .?category_id=$category_id");
    }
// list categories
} else if ($action == 'list_categories') {
    $categories = get_categories();
    include('category_list.php');
// code to add a category with a given $name
} else if ($action == 'add_category') {
    $name = filter_input(INPUT_POST, 'name');

    // Validate inputs
    if ($name == NULL) {
        $error = "Invalid category name. Check name and try again.";
        include('view/error.php');
    } else {
        add_category($name);
        header('Location: .?action=list_categories');  // display the Category List page
    }
// code to delete a category of a given category_id
} else if ($action == 'delete_category') {
    $category_id = filter_input(INPUT_POST, 'category_id',
            FILTER_VALIDATE_INT);
    delete_category($category_id);
    header('Location: .?action=list_categories');      // display the Category List page
}
?>