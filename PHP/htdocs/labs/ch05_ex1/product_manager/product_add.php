<!--Bryan Bibb, CPT283-W01, Jan 26, 2024
Program:  Guitar Shop
Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
          inventory items and product categories.
File:     product_manager/product_add.php
-->
<!--include site-wide header and footer HTML code-->
<?php include '../view/header.php'; ?>

<!--form to add a product-->
<main>
    <h1>Add Product</h1>
    <form action="index.php" method="post" id="add_product_form">
        <input type="hidden" name="action" value="add_product">

<!-- list the current categories for selection -->
        <label>Category:</label>
        <select name="category_id">
        <?php foreach ( $categories as $category ) : ?>
            <option value="<?php echo $category['categoryID']; ?>">
                <?php echo $category['categoryName']; ?>
            </option>
        <?php endforeach; ?>
        </select>
        <br>

<!-- input boxes for adding new information to the product -->
        <label>Code:</label>
        <input type="text" name="code" />
        <br>

        <label>Name:</label>
        <input type="text" name="name" />
        <br>

        <label>List Price:</label>
        <input type="text" name="price" />
        <br>

        <label>&nbsp;</label>
        <input type="submit" value="Add Product" />
        <br>
    </form>
<!--link to list all products-->
    <p class="last_paragraph">
        <a href="?action=list_products">View Product List</a>
    </p>

</main>
<?php include '../view/footer.php'; ?>