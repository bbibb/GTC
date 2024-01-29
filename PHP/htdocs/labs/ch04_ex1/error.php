<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The error.php page contains code that is included within
            other pages as necessary.
File:       error.php
Related:    add_category.php, add_product.php
-->
<!DOCTYPE html>
<html>

<!-- the head section -->
<head>
    <title>My Guitar Shop</title>
    <link rel="stylesheet" href="main.css" />
</head>

<!-- the body section -->
<body>
    <header><h1>My Guitar Shop</h1></header>
    <!-- echo the error variable that is passed from calling function -->
    <main>
        <h2 class="top">Error</h2>
        <p><?php echo $error; ?></p>
    </main>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> My Guitar Shop, Inc.</p>
    </footer>
</body>
</html>