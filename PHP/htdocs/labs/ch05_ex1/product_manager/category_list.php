<!--Bryan Bibb, CPT283-W01, Jan 26, 2024
Program:  Guitar Shop
Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
          inventory items and product categories.
File:     product_manager/category_list.php
-->
<!--include site-wide header and footer HTML code-->
<?php include '../view/header.php'; ?>

<main>
    <hr>

    <h1>Category List</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>&nbsp;</th>
        </tr>
        <!--    these variables are defined by 'product_manager/index.php' which includes the current file. -->
        <!--    PHP code creates a list of categories by looping through the $categories array -->
        <?php foreach ($categories as $category) : ?>
        <tr>
            <td><?php echo $category['categoryName']; ?></td>
            <!-- form action and button to delete the category passed as categoryID to the db -->
            <td>
                <form action="index.php" method="post">
                <input type="hidden" name="action" value="delete_category" />
                <input type="hidden" name="category_id" value="<?php echo $category['categoryID']; ?>"/>
                <input type="submit" value="Delete"/>
                </form>
            </td>
        </tr>
        <?php endforeach; ?>
    </table>

<!--    form to add a category, calls add_category($name) with an Add button-->
    <h2>Add Category</h2>
    <form id="add_category_form" action="index.php" method="post">
        <input type="hidden" name="action" value="add_category" />
        <label>Name:</label>
        <input type="text" name="name" />
        <input type="submit" value="Add"/>
    </form>

<!--link to list products-->
    <p><a href="index.php?action=list_products">List Products</a></p>

</main>
<hr>
<?php include '../view/footer.php'; ?>