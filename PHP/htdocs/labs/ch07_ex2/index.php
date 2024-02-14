<?php 
    //set default value of variables for initial page load
    if (!isset($years)) { $years = '5'; }
?>
<!DOCTYPE html>
<!--    Bryan Bibb, Feb 11, 2024, CPT283-W01-->
<!--    Lab Exercise 7-2: Enhance the Future Value Application-->
<!--    Purpose: Creates drop-down lists in the input form and processes data-->

<html>
<head>
    <title>Future Value Calculator</title>
    <link rel="stylesheet" href="main.css"/>
</head>

<body>
    <main>
<!-- print error message if display_results.php has generated one -->
    <h1>Future Value Calculator</h1>
    <?php if (!empty($error_message)) { ?>
        <p class="error"><?php echo $error_message; ?></p>
    <?php } // end if ?>
    <form action="display_results.php" method="post">

<!-- form to input investment amount in a 'select' drop-down. The values in the
     drop-down list are calculated with a for loop, $5000 increments between
     $10000 and $50000 -->
        <div id="data">
            <label>Investment Amount:</label>
            <select name="investment">
                <?php for ($v = 10000; $v <= 50000; $v += 5000) : ?>
                    <option value="<?php echo $v; ?>" >
                        <?php echo $v; ?>
                    </option>
                <?php endfor; ?>

            </select>

            <br>
<!-- form to input interest rate. The values in the select box are
      calculated with a for loop -->
            <label>Yearly Interest Rate:</label>
            <select name="interest_rate">
                <?php for ($v = 4; $v <= 12; $v += 0.5) : ?>
                    <option value="<?php echo $v; ?>">
                        <?php echo $v; ?>
                    </option>
                <?php endfor; ?>
            </select>

            <br>
<!-- 'years' text entry -->
            <label>Number of Years:</label>
            <input type="text" name="years"
                   value="<?php echo $years; ?>"/><br>
        </div>
<!-- submit button -->
        <div id="buttons">
            <label>&nbsp;</label>
            <input type="submit" value="Calculate"/><br>
        </div>

    </form>
    </main>
</body>
</html>