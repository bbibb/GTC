<!--Bryan Bibb, CPT283-W01, Jan 26, 2024
Program:  Guitar Shop
Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
          inventory items and product categories.
File:     product_manager/product_list.php
-->
<!--include site-wide header and footer HTML code-->
<?php include '../view/header.php'; ?>

<main>
    <h1>Product List</h1>

    <aside>
        <!-- display a list of categories with links at the top -->
        <h2>Categories</h2>
        <?php include '../view/categories_nav.php'; ?>
    </aside>

    <section>
        <!-- display a table of products of category_name sent from 'product_manager/index.php' line 39-->
        <h2><?php echo $category_name; ?></h2>
        <table>
            <tr>
                <th>Code</th>
                <th>Name</th>
                <th class="right">Price</th>
                <th>&nbsp;</th>
            </tr>
<!--loop through the $products array to show the code, name, and price of each -->
            <?php foreach ($products as $product) : ?>
            <tr>
                <td><?php echo $product['productCode']; ?></td>
                <td><?php echo $product['productName']; ?></td>
                <td class="right"><?php echo $product['listPrice']; ?></td>
<!--code for a delete button that triggers the delete_product() function with given product and category id-->
                <td><form action="." method="post">
                    <input type="hidden" name="action"
                           value="delete_product">
                    <input type="hidden" name="product_id"
                           value="<?php echo $product['productID']; ?>">
                    <input type="hidden" name="category_id"
                           value="<?php echo $product['categoryID']; ?>">
                    <input type="submit" value="Delete">
                </form></td>
            </tr>
            <?php endforeach; ?>
        </table>
<!--links to add a product and list categories -->
        <p><a href="index.php?action=show_add_form">Add Product</a></p>
        <p class="last_paragraph"><a href="?action=list_categories">List Categories</a></p>        
    </section>
</main>

<?php include '../view/footer.php'; ?>