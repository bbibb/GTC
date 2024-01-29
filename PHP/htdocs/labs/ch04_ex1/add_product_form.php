<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The add_product_form.php page takes the user input for
            the new product and passes it to add_product.php.
File:       add_product_form.php
Related:    add_product.php, database.php, error.php
-->


<?php
// Select from the categories database all data, ordered by CategoryID, and set as $categories
require('database.php');
$query = 'SELECT *
          FROM categories
          ORDER BY categoryID';
// Open the query, execute the statement, save the data, and close
$statement = $db->prepare($query);
$statement->execute();
$categories = $statement->fetchAll();
$statement->closeCursor();
?>

<!DOCTYPE html>
<html>

<!-- the head section -->
<head>
    <title>My Guitar Shop</title>
    <link rel="stylesheet" href="main.css">
</head>

<!-- the body section -->
<body>
    <header><h1>Product Manager</h1></header>

    <main>
        <!-- Create the form for receiving user input of new product data -->
        <h1>Add Product</h1>
        <!-- Information is passed to add_product.php -->
        <form action="add_product.php" method="post"
              id="add_product_form">

            <!-- Start by listing each category row from the $categories array in a box-->
            <label>Category:</label>
            <select name="category_id">
            <?php foreach ($categories as $category) : ?>
                <option value="<?php echo $category['categoryID']; ?>">
                    <?php echo $category['categoryName']; ?>
                </option>
            <?php endforeach; ?>
            </select><br>
            <!-- Text input boxes for each piece of data -->
            <label>Code:</label>
            <input type="text" name="code"><br>

            <label>Name:</label>
            <input type="text" name="name"><br>

            <label>List Price:</label>
            <input type="text" name="price"><br>

            <!-- submit button -->
            <label>&nbsp;</label>
            <input type="submit" value="Add Product"><br>
        </form>
        <p><a href="index.php">View Product List</a></p>
    </main>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> My Guitar Shop, Inc.</p>
    </footer>
</body>
</html>