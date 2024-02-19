<?php
// Bryan Bibb, Feb 16, 2024, CPT283-W01
// Program: Lab 8-1 Invoice Total application
// Purpose: Calculates the percentage discount and final invoice amount based on the
//          type of customer and the monetary value of the invoice.

$customer_type = filter_input(INPUT_POST, 'type');
$invoice_subtotal = filter_input(INPUT_POST, 'subtotal');

// switch statement checks to see which type of customer. Under each type, it looks to see
// the value of the invoice, and then sets the proper discount amount.
switch ($customer_type) {
    case 'r':
    case 'R':
        if ($invoice_subtotal < 100) {
            $discount_percent = .0;
        } else if ($invoice_subtotal >= 100 && $invoice_subtotal < 250) {
            $discount_percent = .10;
        } else if ($invoice_subtotal >= 250 && $invoice_subtotal < 500) {
            $discount_percent = .25;
        } else if ($invoice_subtotal >= 500) {
            $discount_percent = .30;
        }
        break;
    case 'c':
    case 'C':
        $discount_percent = .20;
        break;
    case 't':
    case 'T':
        if ($invoice_subtotal < 500) {
            $discount_percent = .40;
        } else if ($invoice_subtotal >= 500) {
            $discount_percent = .50;
        }
        break;
    default:
        $discount_percent = .1;
        break;
}

// First version to calculate with if/else structure rather than switch
/*
if ($customer_type == 'R' || $customer_type == 'r') {
    if ($invoice_subtotal < 100) {
        $discount_percent = .0;
    } else if ($invoice_subtotal >= 100 && $invoice_subtotal < 250) {
        $discount_percent = .10;
    } else if ($invoice_subtotal >= 250 && $invoice_subtotal < 500) {
        $discount_percent = .25;
    } else if ($invoice_subtotal >= 500) {
        $discount_percent = .30;
    }
} else if ($customer_type == 'C' || $customer_type == 'c') {
    $discount_percent = .20;
} else if ($customer_type == 'T' || $customer_type == 't') {
    if ($invoice_subtotal < 500) {
        $discount_percent = .40;
    } else if ($invoice_subtotal >= 500) {
        $discount_percent = .50;
    }
} else {
    $discount_percent = .10;
}
*/

// Program logic calculates the discount amount and subtracts it from the total.
$discount_amount = $invoice_subtotal * $discount_percent;
$invoice_total = $invoice_subtotal - $discount_amount;

// format the numbers correctly
$percent = number_format(($discount_percent * 100));
$discount = number_format($discount_amount, 2);
$total = number_format($invoice_total, 2);

// invoice_total.php formats the output
include 'invoice_total.php';

?>