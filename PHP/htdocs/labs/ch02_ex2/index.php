<!--
Lab 02-2 Enhance the Future Value application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Future Value Calculator
Purpose:    Page receives user input for an investment amount, interest rate, and period of growth.
            Then, it calculates and returns the final value of the investment after the period ends.
File:       display_results.php
Related:    display_results.php
-->

<?php
    // initialize variables for initial page load, if they are not already set
    if (!isset($investment)) { $investment = ''; } 
    if (!isset($interest_rate)) { $interest_rate = ''; } 
    if (!isset($years)) { $years = ''; } 
?>

<!DOCTYPE html>
<html>
<head>
    <title>Future Value Calculator</title>
    <link rel="stylesheet" href="main.css">
</head>

<body>
    <main>
    <h1>Future Value Calculator</h1>
    <!-- If the error_message variable has been triggered and set, echo the message -->
    <?php if (!empty($error_message)) { ?>
        <p class="error"><?php echo $error_message; ?></p>
    <?php } ?>

    <!-- Take user input of investment, interest rate, and years, and pass to the display_results script -->
    <form action="display_results.php" method="post">

        <!-- For each input, strip html formatting codes and set variable values -->
        <div id="data">
            <label>Investment Amount:</label>
            <input type="text" name="investment"
                   value="<?php echo htmlspecialchars($investment); ?>">
            <br>

            <label>Yearly Interest Rate:</label>
            <input type="text" name="interest_rate"
                   value="<?php echo htmlspecialchars($interest_rate); ?>">
            <br>

            <label>Number of Years:</label>
            <input type="text" name="years"
                   value="<?php echo htmlspecialchars($years); ?>">
            <br>
        </div>

        <!-- Button to submit the data for processing -->
        <div id="buttons">
            <label>&nbsp;</label>
            <input type="submit" value="Calculate"><br>
        </div>
    </form>
    </main>

</body>
</html>