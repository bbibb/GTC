<!--
Lab 04-1 Enhance the Product Manager application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Product Manager
Purpose:    This application integrates with the MySQL database to store and return information
            about the guitar shop inventory. The database.php page links to the database with
            credentials. Other pages list categories and products, and allow the adding and
            deleting of categories and products in the database.
File:       database.php
Related:    index.html, database_error.php
-->

<?php
    // set values for the database, username, and password
    $dsn = 'mysql:host=127.0.0.1:3308;dbname=cpt283bibb_my_guitar_shop1_test';
    $username = 'bryanb';
    $password = "aside-FLARE-grandam";
    // try...catch block attempts to connect to the database, and returns an error if it cannot
    try {
        $db = new PDO($dsn, $username, $password);
    // save the specific error message generated to a variable, and pass to database_error.php
    } catch (PDOException $e) {
        $error_message = $e->getMessage();
        include('database_error.php');
        exit();
    }
?>