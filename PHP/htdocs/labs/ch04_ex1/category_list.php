<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The add_category.php page takes the user input category
            name and inserts it into the MySQL database.
File:       category_list.php
Related:    add_category.php, delete_category.php, database.php, index.php
-->

<?php
require_once('database.php');

// Get all categories from the categories table
$query = 'SELECT * FROM categories
          ORDER BY categoryID';
// Open the query, retrieve data, save to an array, and close
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
    <link rel="stylesheet" href="main.css" />
</head>

<!-- the body section -->
<body>
<header><h1>Product Manager</h1></header>
<main>
    <!--  table to display category data in $categories with HTML heading -->
    <h1>Category List</h1>
    <table>
        <tr>
            <th>Name</th>
            <th>&nbsp;</th>
        </tr>
        
        <!-- PHP section for listing the categories in the table, with a delete button for each-->
        <?php foreach ($categories as $category) : ?>
            <tr>
                <!-- PHP script to send the categoryName to the delete_category.php page
                    Each category will have a delete button beside it. -->
                <td><?php echo $category['categoryName']; ?></td>
                 <td><form action="delete_category.php" method="post">
                        <input type="hidden" name="category_id"
                               value="<?php echo $category['categoryID']; ?>">
                        <input type="submit" value="Delete">
                    </form></td>
            </tr>
        <?php endforeach; ?>
    </table>
<br>
    <h2>Add Category</h2>
    
    <!-- code to call add_category with the user input category name -->
    <form action="add_category.php" method="post"
          id="add_category_form"
        <label>Name:</label>
        <input type="text" name="name" />
        <!-- submit button -->
        <input id="add_category_button" type="submit" value="Add"/>
    </form>
    <br>
    <p><a href="index.php">List Products</a></p>

    </main>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> My Guitar Shop, Inc.</p>
    </footer>
</body>
</html>