<?php
//    Bryan Bibb, Feb 11, 2024, CPT283-W01
//     Lab Exercise 7-1: Get input and display output
//     Purpose: Form controls receive data from the user and passes to the display code. The data entered is
//              evaluated and passed through functions to saniitze and present properly.

// get the data from the form on index.php
// data is filtered as it is saved into the variable
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $password = filter_input(INPUT_POST, 'password');
    $phone = filter_input(INPUT_POST, 'phone');
// if radio button option is not selected, save value as 'unknown'
    $heard_from = filter_input(INPUT_POST, 'heard_from');
    if ($heard_from === NULL) {
        $heard_from = 'Unknown';
    }
// evaluate whether the checkbox is selected and save variable value accordingly
    $wants_updates = $_POST['wants_updates'];
    if (isset($wants_updates)) {
        $wants_updates = 'Yes';
    } else {
        $wants_updates = 'No';
    }

    $contact_via = filter_input(INPUT_POST, 'contact_via');
// The comments field gets three steps: filtering, removing stripping html codes, and entering line breaks
    $comments = filter_input(INPUT_POST, 'comments');
    $comments = htmlspecialchars($comments);  // NOTE: You must code htmlspecialchars before nl2br for this to work correctly
    $comments = nl2br($comments, FALSE);    
?>
<!DOCTYPE html>
<html>
<head>
    <title>Account Information</title>
    <link rel="stylesheet" href="main.css"/>
</head>
<body>
    <main>
        <h1>Account Information</h1>
<!-- Label and php echo command for each variable created by the form controls -->
        <label>Email Address:</label>
        <span><?php echo htmlspecialchars($email); ?></span><br>

        <label>Password:</label>
        <span><?php echo htmlspecialchars($password); ?></span><br>

        <label>Phone Number:</label>
        <span><?php echo htmlspecialchars($phone); ?></span><br>

        <label>Heard From:</label>
        <span><?php echo htmlspecialchars($heard_from); ?></span><br>

        <label>Send Updates:</label>
        <span><?php echo $wants_updates; ?></span><br>

        <label>Contact Via:</label>
        <span><?php echo htmlspecialchars($contact_via); ?></span><br><br>

        <span>Comments:</span><br>
        <span><?php echo $comments; ?></span><br>
        
        <p>&nbsp;</p>
    </main>
</body>
</html>