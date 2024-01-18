
**Variables**
$characterName

used in echo command:
	"Printing the $characterName with a variable."

**Data Types**
$string = "plain text"
$int = 5
$float = 5.0
$boolean = true|false
null = no value

**String data type**

strtolower(*string*) - makes string all lowercase
strtoupper(*string*)
strlen(*string*) - how many characters are in the string
$string\[0\] - prints first character in the string
	"String"\[2\]  -- r
	$phrase = "abcde"
	$phrase\[1\] = X
	echo $phrase --> "aXcde"
**In PHP strings are mutable!**

echo str_replace("search", "replace", "subject")
echo substr("subject", offset, length)''


**Numbers**
echo 40;  integer
echo -40;
echo 40.45;  float

echo 5 + 9;  14
echo 10 % 3;  1
echo 4 + 5 * 10;  54
echo (4 + 5) * 10;  90

$num = 10;
echo $num;  10
num++ [adds one]
echo $num;  11
echo += 25;  36
\*=

abs(-100) -> 100
pow(2, 4) -> 16
sqrt(16) -> 4
max(2, 10) -> 10
min(2, 1) -> 2
round(3.2) -> 3
ceil(3.3) -> 4 always rounds up
floor(3.9) -> 3 always round down


**user input**
forms

<form action="site.php" method="get">




