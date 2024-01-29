<!--Bryan Bibb, CPT283-W01, Jan 26, 2024
Program:  Guitar Shop
Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
          inventory items and product categories.
File:     product_catalog/product_view.php
-->
<!--the PHP include statement includes the code from the header.php and footer.php files into this one.
In the case of an error, an error message will be generated.
-->
<?php include '../view/header.php'; ?>
<main>
    <aside>
        <h1>Categories</h1>
<!--        categories_nav.php provides the site-wide code for listing each category with a link at the top-->
        <?php include '../view/categories_nav.php'; ?>
    </aside>
<!--    2-column arrangement for showing the name and image on the left, and the data on the right.-->
<!--    These variables are defined by 'product_catalog/index.php' which includes the current file at the end.-->
    <section>
        <h1><?php echo $name; ?></h1>
        <div id="left_column">
            <p>
                <img src="<?php echo $image_filename; ?>"
                    alt="<?php echo $image_alt; ?>" />
            </p>
        </div>

        <!--  right column; these variables are defined by 'product_catalog/index.php'
        which includes the current file at the end.
        -->
        <div id="right_column">
            <p><b>List Price:</b> $<?php echo $list_price; ?></p>
            <p><b>Discount:</b> <?php echo $discount_percent; ?>%</p>
            <p><b>Your Price:</b> $<?php echo $unit_price_f; ?>
                 (You save $<?php echo $discount_amount_f; ?>)</p>
<!-- code to add a product to the shopping cart, which is not currently configured -->
            <form action="<?php echo '../cart' ?>" method="post">
                <input type="hidden" name="action" value="add">
                <input type="hidden" name="product_id"
                       value="<?php echo $product_id; ?>">
                <b>Quantity:</b>
                <input id="quantity" type="text" name="quantity" 
                       value="1" size="2">
                <br><br>
                <input type="submit" value="Add to Cart">
            </form>
        </div>
    </section>
</main>
<?php include '../view/footer.php'; ?>