<?php
/**
 * This example shows settings to use when sending via Google's Gmail servers.
 * This uses traditional id & password authentication - look at the gmail_xoauth.phps
 * example to see how to use XOAUTH2.
 * The IMAP section shows how to save this message to the 'Sent Mail' folder using IMAP commands.
 */
//Import PHPMailer classes into the global namespace


require("/PHPMailer-master/src/PHPMailer.php");
require("/PHPMailer-master/src/SMTP.php");
require("/PHPMailer-master/src/Exception.php");
//Create a new PHPMailer instance

function send_email($body)
{
$mail = new PHPMailer\PHPMailer\PHPMailer();
//Tell PHPMailer to use SMTP
$mail->isSMTP();
//Enable SMTP debugging
// 0 = off (for production use)
// 1 = client messages
// 2 = client and server messages
$mail->SMTPDebug = 1;
//Set the hostname of the mail server
$mail->Host = 'smtp.googlemail.com';
// use
// $mail->Host = gethostbyname('smtp.gmail.com');
// if your network does not support SMTP over IPv6
//Set the SMTP port number - 587 for authenticated TLS, a.k.a. RFC4409 SMTP submission
$mail->Port = 465;
//Set the encryption system to use - ssl (deprecated) or tls
$mail->SMTPSecure = 'ssl';
//Whether to use SMTP authentication
$mail->SMTPAuth = true;
//Username to use for SMTP authentication - use full email address for gmail
$mail->Username = "fortestingcodes@gmail.com";
//Password to use for SMTP authentication
$mail->Password = "srinuiidt25";
//Set who the message is to be sent from
$mail->setFrom('info@integrity.com', 'IntegrityCorp');
//Set an alternative reply-to address
$mail->addReplyTo('replyto@integrity.com', 'IntegrityHelp');
//Set who the message is to be sent to
$mail->addAddress('nelaturi.tilak8@gmail.com', 'John Doe');
//Set the subject line
$mail->Subject = 'File integrity check.';
//Read an HTML message body from an external file, convert referenced images to embedded,
//convert HTML into a basic plain-text alternative body
//$mail->msgHTML(file_get_contents('contents.html'), __DIR__);
$mail->Body=$body;//Replace the plain text body with one created manually

$mail->AltBody = $body;
//Attach an image file
//$mail->addAttachment('images/phpmailer_mini.png');
//send the message, check for errors
if (!$mail->send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
} else {
    echo "Message sent!";
   
}
}
