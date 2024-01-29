<?php
// Bryan Bibb, CPT283-W01, Jan 26, 2024
// Program:  Guitar Shop
// Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
//           inventory items and product categories.
// File:     model/database.php
//
// this file opens the connection with the database using server location and credentials hard coded into
// the file. If the connection fails, an $error_message is generated and passed to '../errors/database_error.php'.
    $dsn = 'mysql:host=127.0.0.1:3308;dbname=cpt283bibb_my_guitar_shop1_test';
    $username = 'bryanb';
    $password = 'aside-FLARE-grandam';

    try {
        $db = new PDO($dsn, $username, $password);
    } catch (PDOException $e) {
        $error_message = $e->getMessage();
        include('../errors/database_error.php');
        exit();
    }
?>