<!--
Lab 02-1 Build the Product Discount Calculator application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Discount Calculator
Purpose:    Page receives user input for a product description, list price, and discount amount.
            Then, it calculates and returns the value of the discount and the net price of the product.
File:       display_discount.php
Related     index.html
-->

<!DOCTYPE html>
<html>
<head>
    <title>Product Discount Calculator</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
    <main>
        <h1>Product Discount Calculator</h1>
<?php
        // define variables for receiving and filtering user input

        $product_description = $_POST['product_description'];
        // validate float values for price and discount variables
        $list_price = filter_input(INPUT_POST,'list_price', FILTER_VALIDATE_FLOAT);
        $discount_percent = filter_input(INPUT_POST,'discount_percent', FILTER_VALIDATE_FLOAT);

        // calculate the discount amount and discount price
        $discount_amount = $list_price * $discount_percent * .01;
        $discount_price = $list_price - $discount_amount;

        // format the output to currency and percentages with number_format() method
        $list_price_f = '$'.number_format($list_price, 2);
        $discount_percent_f = $discount_percent.'%';
        $discount_amount_f = '$'.number_format($discount_amount, 2);
        $discount_price_f = '$'.number_format($discount_price, 2);
?>
        <label>Product Description:</label>
        <!-- the htmlspecialchars function prevents user inut from being processed as html code -->
        <span><?php echo htmlspecialchars($product_description); ?></span><br>

        <!-- echo the formatted versions of each variable
        <label>List Price:</label>
        <span><?php echo $list_price_f; ?></span><br>

        <label>Discount Percent:</label>
        <span><?php echo $discount_percent_f; ?></span><br>

        <label>Discount Amount:</label>
        <span><?php echo $discount_amount_f; ?></span><br>

        <label>Discount Price:</label>
        <span><?php echo $discount_price_f; ?></span><br>
    </main>
</body>
</html>