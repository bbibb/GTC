<!--
Lab 02-2 Enhance the Future Value application
Bryan Bibb, 1/20/2024, CPT283-W01
Program:    Future Value Calculator
Purpose:    Page receives user input for an investment amount, interest rate, and period of growth.
            Then, it calculates and returns the final value of the investment after the period ends.
File:       display_results.php
Related:    index.html
-->

<?php
    // get the data from the form and validate the numerical values, saving to three variables
    $investment = filter_input(INPUT_POST, 'investment',
        FILTER_VALIDATE_FLOAT);
    $interest_rate = filter_input(INPUT_POST, 'interest_rate',
        FILTER_VALIDATE_FLOAT);
    $years = filter_input(INPUT_POST, 'years',
        FILTER_VALIDATE_INT);

    // set default error message of empty string, in case validation fails
    $error_message = '';
    
    // validate investment amount as a number greater than zero
    if ($investment === FALSE ) {
        $error_message .= 'Investment must be a valid number.<br>'; 
    } else if ( $investment <= 0 ) {
        $error_message .= 'Investment must be greater than zero.<br>'; 
    }

    
    // validate interest rate as a number between 0 and 15
    if ( $interest_rate === FALSE )  {
        $error_message .= 'Interest rate must be a valid number.<br>'; 
    } else if ( $interest_rate <= 0 OR $interest_rate > 15) {
        $error_message .= 'Interest rate must be above 0 and less than 15 percent.<br>';
    } 
    
    // validate years as a positive integer between 0 and 31
    if ( $years === FALSE ) {
        $error_message .= 'Years must be a valid whole number.<br>';
    } else if ( $years <= 0 ) {
        $error_message .= 'Years must be greater than zero.<br>';
    } else if ( $years > 30 ) {
        $error_message .= 'Years must be less than 31.<br>';
    } 

    // if the (empty) error message exists, go to the index page
    if ($error_message != '') {
        include('index.php');
        exit(); }

    // calculate the future value by looping through each year of the investment term, multiplying
    // the interest rate times the investment value for each year, and then adding that amount
    // to the running total.
    $future_value = $investment;
    for ($i = 1; $i <= $years; $i++) {
        $future_value += $future_value * $interest_rate * .01; 
    }

    // apply currency and percent formatting
    $investment_f = '$'.number_format($investment, 2);
    $yearly_rate_f = $interest_rate.'%';
    $future_value_f = '$'.number_format($future_value, 2);
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

        <!-- Echo formatted values for each variable -->
        <label>Investment Amount:</label>
        <span><?php echo $investment_f; ?></span><br>

        <label>Yearly Interest Rate:</label>
        <span><?php echo $yearly_rate_f; ?></span><br>

        <label>Number of Years:</label>
        <span><?php echo $years; ?></span><br>

        <label>Future Value:</label>
        <span><?php echo $future_value_f; ?></span><br>

        <!-- Format and echo the date with date() method
        <?php   $date = date('m/d/y');
        echo 'This calculation was done on ' . $date . '.';
        ?>

    </main>
</body>
</html>
