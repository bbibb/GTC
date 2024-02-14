<!DOCTYPE hyml>
<html>
<!-- Bryan Bibb, CPT283-W01, Feb 1, 2024
     Program: Project Lab 2, database_error.php displays a formatted error message in case
              the database cannot be accessed properly.-->
    <head>
        <title>Vehicle Log</title>
        <link rel="stylesheet" href="/css/styles.css"
    </head>

    <body>
    <main>
        <h1>Database Error</h1>
        <p>There was an error connecting to the database.</p>
        <p>Check configuration settings and the status of the database server.</p>
<!-- $error_message is defined in config.php which includes this file -->
        <p>Error message: <?php echo $error_message; ?></p>
    </main>
    </body>
</html>