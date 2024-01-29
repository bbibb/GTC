<!--Bryan Bibb, CPT283-W01, Jan 26, 2024
Program:  Guitar Shop
Purpose:  A database of inventory for My Guitar Shop. Includes ability to view, edit, add, and delete
          inventory items and product categories.
File:     database_error.php
-->
<!--site-wide header HTML code -->
<?php include '../view/header.php'; ?>

<!--database connection error message-->
<div id="main">
    <h1>Database Error</h1>
    <p class="first_paragraph">There was an error connecting to the database.</p>
    <p>The database must be installed as described in the appendix.</p>
    <p>MySQL must be running as described in chapter 1.</p>
    # $error_message variable from '../model/database.php'
    <p class="last_paragraph">Error message: <?php echo $error_message; ?></p>
</div><!-- end main -->

<!--site-wide footer HTML code -->
<?php include '../view/footer.php'; ?>