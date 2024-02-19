<?php
// Bryan Bibb, Feb 16, 2024, CPT283-W01
// Program: Score calculator
// Purpose: Adds together a number of test scores and calculates the average.


//set default values to be used when page first loads
$scores = [];
$scores[0] = 70;
$scores[1] = 80;
$scores[2] = 90;

// initialize variables with empty and 0 values
$scores_string = '';
$score_total = 0;
$score_average = 0;
$max_rolls = 0;
$average_rolls = 0;

$score_total_f = '';
$score_average_f = '';

//take action based on variable in POST array
$action = filter_input(INPUT_POST, 'action');
// two types of actions based on $action value, routed with switch statement
switch ($action) {
    // calculate total and average of test scores (at least 3 values)
    case 'process_scores':
        $scores = $_POST['scores'];

        // validate the scores: needs three
        $is_valid = TRUE;
        for ($i = 0; $i < count($scores); $i++) {
            if (empty($scores[$i]) || !is_numeric($scores[$i])) {
                $scores_string = 'You must enter three valid numbers for scores.';
                $is_valid = FALSE;
                break;
            }
        }
        if (!$is_valid) {
            break;
        }
        if (empty($scores[0]) ||
            empty($scores[1]) ||
            empty($scores[2]) ||
            !is_numeric($scores[0]) ||
            !is_numeric($scores[1]) ||
            !is_numeric($scores[2])) {
                $scores_string = 'You must enter three valid numbers for scores.';
                break;
        }

        // process the scores
        // Calculate the score total
        $score_total = 0;
        $scores_string = '';
        // add each score to the running total
        foreach ($scores as $s) {
            $scores_string .= $s . '|';
            $score_total += $s;
        }
        // output string contains each score separated by |
        $scores_string = substr($scores_string, 0, strlen($scores_string)-1);

        // calculate the average
        $score_average = $score_total / count($scores);
        
        // format the total and average
        $score_total_f = number_format($score_total, 2);
        $score_average_f = number_format($score_average, 2);

        break;
    case 'process_rolls':
        // receive the number desired to roll
        $number_to_roll = filter_input(INPUT_POST, 'number_to_roll', 
                FILTER_VALIDATE_INT);

        // initialized variables
        $total = 0;
        $count = 0;
        $max_rolls = -INF;

        //  'while' loop converted to a 'for' loop
        // iterates through 10000 rolls and adds up the value
        for ($count=0; $count < 10000; $count++) {
            $rolls = 1;
            while (mt_rand(1, 6) != $number_to_roll) {
                $rolls++;
            }
            // then calculates the total
            $total += $rolls;
            $max_rolls = max($rolls, $max_rolls);
        }
        $average_rolls = $total / $count;

        break;
}
include 'loop_tester.php';
?>