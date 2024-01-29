<?php
// Bryan Bibb, CPT283-W01, Jan 26, 2024
// Program:  Guitar Shop
// Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
//           inventory items and product categories.
// File:     product_catalog/index.php
//
// the PHP require statement includes the code from these three pages into this one. Because it is 'require'
// and not include, execution will stop in the case of an error, not simply pass a message.
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
    $categories = get_categories();
    $category_name = get_category_name($category_id);
    $products = get_products_by_category($category_id);
    include('product_list.php');
} else if ($action == 'view_product') {
    $product_id = filter_input(INPUT_GET, 'product_id',
            FILTER_VALIDATE_INT);

    // error message if the product id is incorrect or null
    if ($product_id == NULL || $product_id == FALSE) {
        $error = 'Missing or incorrect product id.';
        include('../errors/error.php');
    } else {
        $categories = get_categories();
        $product = get_product($product_id);

        // Get product data from the $product array defined by product_list.php
        $code = $product['productCode'];
        $name = $product['productName'];
        $list_price = $product['listPrice'];

        // Calculate discounts, rounded to 2 decimal places
        $discount_percent = 30;  // 30% off for all web orders
        $discount_amount = round($list_price * ($discount_percent/100.0), 2);
        $unit_price = $list_price - $discount_amount;

        // Format the calculations
        $discount_amount_f = number_format($discount_amount, 2);
        $unit_price_f = number_format($unit_price, 2);

        // Get image URL and alternate text
        $image_filename = '../images/' . $code . '.png';
        $image_alt = 'Image: ' . $code . '.png';
        // include code to display the data returned by the query functions
        include('product_view.php');
    }
}
?>