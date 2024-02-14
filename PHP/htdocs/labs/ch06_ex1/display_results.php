<?php
//Bryan Bibb, Feb 1, 2024, CPT283-W01
//Program:    Future Value
//Purpose:    Program calculates the value of an initial investment over a certain number of
//            years at a given interest rate, based on user input values. This lab uses 'echo'
//            statements to observe the looping function to debug its internal logic error.

    // get the data from the form for investment amount, interest rate, and term length
    $investment = filter_input(INPUT_POST, 'investment', 
            FILTER_VALIDATE_FLOAT);
    $interest_rate = filter_input(INPUT_POST, 'interest_rate', 
            FILTER_VALIDATE_FLOAT);
    $years = filter_input(INPUT_POST, 'years', 
            FILTER_VALIDATE_INT);

    // set default error message of empty string
    $error_message = '';
    
    // validate investment value as greater than zero
    if ($investment === FALSE ) {
        $error_message .= 'Investment must be a valid number.<br>'; 
    } else if ( $investment <= 0 ) {
        $error_message .= 'Investment must be greater than zero.<br>'; 
    } 
    
    // validate interest rate as greater than zero
    if ( $interest_rate === FALSE )  {
        $error_message .= 'Interest rate must be a valid number.<br>'; 
    } else if ( $interest_rate <= 0 ) {
        $error_message .= 'Interest rate must be greater than zero.<br>'; 
    } 
    
    // validate years as a value between 0 and 31, exclusive
    if ( $years === FALSE ) {
        $error_message .= 'Years must be a valid whole number.<br>';
    } else if ( $years <= 0 ) {
        $error_message .= 'Years must be greater than zero.<br>';
    } else if ( $years > 30 ) {
        $error_message .= 'Years must be less than 31.<br>';
    } 

    // if an error message exists, go to the index page
    if ($error_message != '') {
        include('index.php');
        exit();
    }

    // calculate the future value
    $future_value = $investment;
    // echo statements for debugging
    echo '$future_value = ' . $future_value . '<br>';
    echo '$interest_rate = ' . $interest_rate . '<br>';
    echo '$years = ' . $years . '<br><br>';
    echo 'Start of for loop to calculate future value <br><br>';
    // loop once for each year in the number of years submitted
    for ($i = 1; $i <= $years; $i++) {
        // each time through, multiply the current value * the interest rate,
        // then add that to the current value.
        // the echo statements show that the investment is growing much too
        // rapidly, and so the raw $interest_rate needs to be multiplied by 0.01.
        $future_value += $future_value * $interest_rate;
        // in each loop, print the number of that loop and the new value
        echo '$i = ' . $i . '<br>';
        echo '$future_value = ' . $future_value . '<br>';
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
    <link rel="stylesheet" href="main.css"/>
</head>
<body>
    <main>
        <h1>Future Value Calculator</h1>

        <label>Investment Amount:</label>
        <span><?php echo $investment_f; ?></span><br>

        <label>Yearly Interest Rate:</label>
        <span><?php echo $yearly_rate_f; ?></span><br>

        <label>Number of Years:</label>
        <span><?php echo $years; ?></span><br>

        <label>Future Value:</label>
        <span><?php echo $future_value_f; ?></span><br>
    </main>
</body>
</html>