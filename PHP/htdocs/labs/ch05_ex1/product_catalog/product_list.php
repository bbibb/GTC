<!--Bryan Bibb, CPT283-W01, Jan 26, 2024
Program:  Guitar Shop
Purpose:    A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
            inventory items and product categories.
File:       product_catalog/product_list.php
-->
<!--include site-wide header and footer HTML code -->
<?php include '../view/header.php'; ?>

<main>
    <aside>
        <h1>Categories</h1>
<!--        include categories_nav.php which provides a linked list of categories on the top -->
        <?php include '../view/categories_nav.php'; ?>
    </aside>
<!--    these variables are defined by 'product_catalog/index.php' which includes the current file. -->
    <section>
        <h1><?php echo $category_name; ?></h1>
        <ul class="nav">
            <!-- display links for products in selected category -->
            <?php foreach ($products as $product) : ?>
            <li>
                <a href="?action=view_product&amp;product_id=<?php 
                          echo $product['productID']; ?>">
                    <?php echo $product['productName']; ?>
                </a>
            </li>
            <?php endforeach; ?>
        </ul>
    </section>
</main>
<?php include '../view/footer.php'; ?>