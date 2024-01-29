<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The database_error.php page is called by database.php
            and returns the error message.
File:       database_error.php
Related:    database.php
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
    <!-- Generic error message along with the specific error message returned by database.php-->
    <main>
        <h1>Database Error</h1>
        <p>There was an error connecting to the database.</p>
        <p>The database must be installed as described in the appendix.</p>
        <p>MySQL must be running as described in chapter 1.</p>
        <p>Error message: <?php echo $error_message; ?></p>
        <p>&nbsp;</p>
    </main>

    <footer>
        <!-- echo the formatted date -->
        <p>&copy; <?php echo date("Y"); ?> My Guitar Shop, Inc.</p>
    </footer>
</body>
</html>