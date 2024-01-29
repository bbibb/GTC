<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The index page initializes the database, gets product
            data through queries, and displays it in a table. Other pages list categories and products,
            and allow the adding and deleting of categories and products in the database.
File:       index.html
Related:    add_category.php, add_product.php, category_list.php, database.php, database_error.php
            delete_category.php, delete_product.php, and error.php.
-->

<?php
// Initialize the database connection with a call to database.php
require_once('database.php');

// Filter the category_id input as a valid integer, and set category_ID = 1 as default value
if (!isset($category_id)) {
    $category_id = filter_input(INPUT_GET, 'category_id', 
            FILTER_VALIDATE_INT);
    if ($category_id == NULL || $category_id == FALSE) {
        $category_id = 1;
    }
}
// Get data for the selected categoryID in the categories table
// construct the query
$queryCategory = 'SELECT * FROM categories
                  WHERE categoryID = :category_id';
// open query, prepare data, execute statement, save to $category_name and close
$statement1 = $db->prepare($queryCategory);
$statement1->bindValue(':category_id', $category_id);
$statement1->execute();
$category = $statement1->fetch();
$category_name = $category['categoryName'];
$statement1->closeCursor();


// Get all categories and save to $categories array using same method as above
$query = 'SELECT * FROM categories
          ORDER BY categoryID';
$statement = $db->prepare($query);
$statement->execute();
$categories = $statement->fetchAll();
$statement->closeCursor();

// Get products for selected category using same method as above
$queryProducts = 'SELECT * FROM products
                  WHERE categoryID = :category_id
                  ORDER BY productID';
$statement3 = $db->prepare($queryProducts);
$statement3->bindValue(':category_id', $category_id);
$statement3->execute();
$products = $statement3->fetchAll();
$statement3->closeCursor();
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
    <h1>Product List</h1>

    <aside>
        <!-- display a list of categories by looping through the $categories array-->
        <h2>Categories</h2>
        <nav>
        <ul>
            <!-- For each row in the array, print the category name -->
            <?php foreach ($categories as $category) : ?>
            <li><a href=".?category_id=<?php echo $category['categoryID']; ?>">
                    <?php echo $category['categoryName']; ?>
                </a>
            </li>
            <?php endforeach; ?>
        </ul>
        </nav>          
    </aside>

    <section>
        <!-- display a table of products including productCode, productName, and listPrice-->
        <h2><?php echo $category_name; ?></h2>
        <table>
            <tr>
                <th>Code</th>
                <th>Name</th>
                <th class="right">Price</th>
                <th>&nbsp;</th>
            </tr>

            <!-- loop through the $products array to display data for each product -->
            <?php foreach ($products as $product) : ?>
            <tr>
                <td><?php echo $product['productCode']; ?></td>
                <td><?php echo $product['productName']; ?></td>
                <td class="right"><?php echo $product['listPrice']; ?></td>
                <!-- each product will have a delete button, passing the productID and categoryID
                to delete_product.php -->
                <td><form action="delete_product.php" method="post">
                    <input type="hidden" name="product_id"
                           value="<?php echo $product['productID']; ?>">
                    <input type="hidden" name="category_id"
                           value="<?php echo $product['categoryID']; ?>">
                    <input type="submit" value="Delete">
                </form></td>
            </tr>
            <?php endforeach; ?>
        </table>
        <!-- links to pages to add products and list categories -->
        <p><a href="add_product_form.php">Add Product</a></p>
        <p><a href="category_list.php">List Categories</a></p>        
    </section>
</main>
<footer>
    <p>&copy; <?php echo date("Y"); ?> My Guitar Shop, Inc.</p>
</footer>
</body>
</html>