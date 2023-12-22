

## Topic 1

My favorite thing about learning Python first is that, although the syntax is fairly simple and easy to grasp, the language itself is very powerful and is widely used in the field. When we were learning how to program Alice in a previous class, it was fun and useful, but I felt that I would rather have been learning the actual code than creating those pseudo-code blocks. The Python that we learn right from the start in this course can be helpful in doing actual work. That makes it more interesting, as well as more useful as a starting point.

According to [this site](https://bootcamp.berkeley.edu/blog/most-in-demand-programming-languages/), Python is second only to JavaScript in the list of useful and in-demand scripting languages.

Reference visited 8/27/2023:

[https://bootcamp.berkeley.edu/blog/most-in-demand-programming-languages/](https://bootcamp.berkeley.edu/blog/most-in-demand-programming-languages/)

## Topic 2

A function is a block of code saved under a specific name that the coder can call easily and repeatedly without having to retype it. Python has "built in functions" that are part of the core language, such as the print() function that we have used in each lab. Coders can implement "user defined functions" on the fly within a program, or saved externally for importing into multiple programs. Functions are convenient because you do not need to retype those instructions in multiple places, thereby making your code base smaller and decreasing the likelihood of typos. 

Each function should be defined to do one thing. By breaking a larger program into smaller functions, the programmer can write code that is easier to read, and that is generally better organized in a logical, step-by-step fashion. You can pass single or multiple parameters to the same function, allowing you to reuse code in a range of contexts. Functions also make your program easier to maintain. If the instructions need to be changed, they can be edited in one spot, and that change will propogate to all instances in which that function is called.

"How to Define a Function in Python" [https://learnpython.com/blog/define-function-python/](https://learnpython.com/blog/define-function-python/)

"What is a function?" [https://pythonprinciples.com/blog/what-is-a-function/](https://pythonprinciples.com/blog/what-is-a-function/)

## Topic 3

Pseudocode is the first step in coding a complicated project. You start by breaking the program into specific steps or blocks, and then think about the inherent logic needed in each step. For example, in a program that performs calculations, what input do you need to get, how will you validate that data, what kinds of operations will need to be performed and in what order, and how will the data be returned to the user? Before you try to remember how to actually code those steps, such as the specific syntax for loops, fstrings, Boolean operations, etc., you put all of that logical information into a list of natural-language instructions. The end result is a human-readable list of steps that the program will need to complete, in order. It is very much like a recipe for cooking: even a person who does know the coding language should be able to read the pseudocode and get a sense of what the program is doing and how it operates.

Pseudocode helps you become a better programmer because the heart of programming is learning to think like a programmer, which means breaking programs and routines into small step-by-step instructions. The process of implementing those instructions in actual code is a secondary consideration. If you cannot think logically about how to break a program into tiny steps, then no amount of syntax knowledge will help you.

Therefore, it seems to me that coding involves two different mental states that are best kept separate, at least in the initial stages. The logical design step is first, and only then do you need to get into writing expressions properly, using the right syntax and punctuation, etc.. By bracketing out the actual coding/syntax mental process, pseudocode lets you focus more purely that crucial first step. As said in the link below, it is a bridge between your brain and the code.


[https://www.freecodecamp.org/news/what-is-pseudocode-in-programming/](https://www.freecodecamp.org/news/what-is-pseudocode-in-programming/)
## Topic 4

According to [StarttechUp](https://www.startechup.com/blog/5-steps-of-software-development/), the steps for creating a software project include 1) planning, 2) design, 3) development, 4) testing, and 5) deployment. Adequately planning a project must include prior attention to all of these factors. For the planning stage, you consider the market needs, the function/utility that your project will serve, risk assessment, how much it will cost, etc. But you should also plan for the other elements, by researching design decisions, putting together the development team and testing plan, and making decisions about deployment factors such as platform, server hosting, customer service and maintenance, and so on. My basic point is that a significant software project is at once a technical challenge as well as a creative process and a business venture. 

In order to manage all of these aspects, you may need what is known as "project management software," of which there are many options. [Tech Republic](https://www.techrepublic.com/article/software-development-project-management-tools/) lists several popular options including Jira, Monday.com, Confluence, and Basecamp. Costs vary greatly depending on the number of users and the complexity of the project. Slightly more focused tools for communication include Trello, Notion, and Slack. There are also [open source options](https://geekflare.com/open-source-project-management-software/) that can help you streamline the workflow, communicate with team members, and increase efficiency. Small to medium projects may fit well in an open source, self-hosted solution such as [OpenProject](https://www.openproject.org/) or [FocalBoard](https://www.focalboard.com/).

Finally, if I had to name the most important tool for planning a software application, I would suggest a nice notepad and pencil. Handwritten notes work well for plotting out initial ideas, creating a hierarchy for the applications features and functions, and writing pseudocode. 

Sources:

"The Five Steps of Any Software Development" [https://www.startechup.com/blog/5-steps-of-software-development/](https://www.startechup.com/blog/5-steps-of-software-development/)

"Top 7 software development project management tools for 2023: [https://www.techrepublic.com/article/software-development-project-management-tools/](https://www.techrepublic.com/article/software-development-project-management-tools/)

"12 Best Open Source Project Management Software [Self-hosted]" [https://geekflare.com/open-source-project-management-software/](https://geekflare.com/open-source-project-management-software/)

## Topic 5

I would say that logic errors are the hardest to fix. Syntax errors are the easiest because if you make one of those, the interpreter alerts you to that fact, and pinpoints (generally) the area in the code where the error occurs, and often what type of error there is. You know that you've fixed it immediately because then the code runs. Runtime errors are a bit harder because you may have to set a breakpoint and step through the code to see what is causing the code to fail. There may be an incorrect data type input or operation, for example, which is relatively simply to identify and correct.

On the other hand, if you are not paying careful attention, you may not even notice that you have coded a logic error. The code executes, and completes as expected, returning a value that might seem reasonable. It might even be that the incorrect returned value is used by other parts of the program and so gets lost in the shuffle so that it is very difficult to determine exactly where the error occurs, even when you realize there is an error. 

Logic errors are one reason that the programmer should develop a logical, step-by-step and thorough testing procedure. You must run through the algorithm by hand so that you know what the correct response should be, and then test the program to make sure no logical error has taken root. It is important to test all sorts of legal and illegal inputs so that you can discover any little bugs that might lie in the code.

This is a helpful discussion that supplements our own reading:

[https://education.launchcode.org/lchs/chapters/errors-and-debugging/index.html](https://education.launchcode.org/lchs/chapters/errors-and-debugging/index.html)
## Topic 6

A list is a data type of an object that stores other objects. The objects within a list can be different data types themselves, which is very handy. In addition to giving programmers an easy to way to store and retrieve data through indexing, lists have the advantage of being mutable, sliceable, nestable, and more.

One common use of a list would be the construction of a 'for loop'. Using the syntax "for i in {list}", the programmer can perform the same actions or evaluate the same expression across each item in the list. You can also use other functions to manipulate the list before you pass it into the loop, giving the programmer precise control over the data that is sent into the loop. The for loop in this case can change the data in the list, create new lists, or return values to the calling function, as needed by the programmer. An example might be taking a list of days of the month, and creating a to-do calendar with information for each day.

A second example would be the use of lists for arithmetic operations. You can use the len() with sum(), and other other arithmetic functions to manipulate integer or floating point data, in addition to max(), min(), and comparative expressions. A use for this would be to keep track of invoice data and perform arithmetic operations on the sums.

[https://realpython.com/python-list/](http://v/)
## Topic 7

The main advantage to using CSV data is that the information is saved in a standard text format that can be opened by multiple programs, and that will still be accessible even if the application used to create it becomes obsolete, or if binary file encoding standards change dramatically.

I am old enough to remember how much difficulty we had with competing binary file formats with Word Processors and Spreadsheets. In addition to Mac/PC issues, there were multiple business suites on Windows that each used their own proprietary binary standard. Companies were forced to reverse-engineer the binary file format to enable re-encoding for use in a different program, but this was a difficult and imperfect process, and file formats were always changing. The Open Source community championed an XML format called ODF, Open Document Format, and by 2007, Microsoft itself had switched to an XML file rather than its binary file format. This was a major improvement in the portability and longevity of our saved data. In any case, a CSV file will never become inaccessible as long as the file itself is not corrupt.

The main advantage of a binary file is that applications can easily include a wide variety of data types and other kinds of complex coding that are more difficult in a flat text-file format such as CSV. If the data set includes images, video, and other tricky data types, these are not (easily) stored in a CSV file. It would be possible to store those objects outside the CSV file and include links in the file to access them when needed. However, this requires keeping the various related files together, and CSV is not well-designed for this.

[https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)
## Topic 8

According to [this article](https://web.mit.edu/java_v1.0.2/www/tutorial/java/exceptions/definition.html) on the MIT site, exception handling has several tangible benefits. First, by having separate parts of the code that handle exceptions, it means that there can be fewer lines of code within the function dealing with data validation. Rather, the function code stays together, and then a block of Exception instructions can take over if there is an error. This leads to more efficient and readable code. Second, exception handling code can differentiate between types of errors and provide appropriate feedback to the user as well as useful information passed back to the calling function. Rather than just having a general experience of "my app just crashed," there is more granular information about what error occurred when, and in what function.

Also, I would say that this creates overall a more positive user experience. Often if I install a new application that crashes soon, especially without good information being reported as to why the crash occurred, I will immediately delete that app and look for a new one. If we want our apps to be successful we have to make sure that the code is solid and without errors, and we have to handle any unexpected difficulties gracefully.

[https://web.mit.edu/java_v1.0.2/www/tutorial/java/exceptions/definition.html](https://web.mit.edu/java_v1.0.2/www/tutorial/java/exceptions/definition.html)

## Topic 9

There are several very important concepts in this chapter that will be crucial in our programming. First, I was glad to learn how to add trailing zeros to floating point numbers. In the MPG program, for example, you could end up with an average cost of, say, $2.3, even if you were using round() to 2 decimal places. By using the methods in this chapter, you can make sure that result would print as $2.30. Similarly, keeping everything lined up with tabs is tricky, and it breaks easily when a string or numeric result is longer or shorter than you expected. By setting the width of a field, you can keep your columns of data tidy and easy to read. Finally, I was interested to learn about the different kinds of rounding, and that not every arithmetic system uses the same technique. In school I suppose we all learned the ROUND_HALF_UP method, where 1.05 rounds to 1.1. I did not know that technique is used mostly in financial calculations. The default method of ROUND_HALF_EVEN is totally new to me, and I would like to know more about why it is preferable to the UP or even DOWN method.

For anyone looking for a quick summary of the relevant information about numbers in Python in this chapter, I found this page to be very helpful:

[https://realpython.com/python-numbers/](https://realpython.com/python-numbers/)


## Topic 10

Each of these methods seems very important, but I am particularly interested to learn more about find() and replace() because much of the text-based work that I do hinges on processing text, identifying patterns and occurrences of terms, and creating output based on that search. There are applications that do this for a certain textual corpus (the one I use most with the Bible is called Accordance), and I know there are Python libraries such as Pandas for data analysis and spaCy for natural language processing. Those more complicated tools are rooted in part in the fundamental rules that Python uses for categorizing, searching, and analyzing strings. I am excited to build rudimentary scripts and apps that can process string data and output it in a way that will reveal patterns and semantic relationships. But of course that more complicated work must begin with the basics!

[https://spacy.io/](https://spacy.io/)

[https://pypi.org/project/pandas/](https://pypi.org/project/pandas/)

## Topic 11

When we began to discuss "objects" in Python with their included attributes and methods, I felt well-prepared to dive into object-oriented programming because of our prior work in CPT113 with Alice. In the Alice program, each of the items that you work with is an object, and each object has both attributes and methods associated with it. We learned how to set and change attributes in these objects, and apply instructions to them to make the program elements actually do things. However, I have had to do a good bit of reading to nail down the specifics. 

(Below is my understanding, written out here in order to help myself get it straight. Feel free to ignore, but let me know if you see an error.)

--------------------------------------------------------------------------------------------------------------------------------------------------------

Objects in Python are similar to sprites in Alice, in that an object contains attributes and methods (both accessed with "dot" syntax). A "class" in Python is like a template that defines which attributes and methods are included in that class, and you use a "constructor" to create an object, that is, an "instance" of that class. So, if the "class" is "student," an object in the "student" class might be "bryan." Attributes included in that class might be student.age, student.email, student.major, and so on. Methods included in the class might be student.email() or student.enroll(), and so on. The object bryan would have attributes, eg., bryan.age = 51, or you could call bryan.email() to send an email to me with the "instance method" email().

The data types we have been working with are actually built-in classes. The module "datetime" will let you create objects of different classes: datetime.date, datetime.time, and (confusingly) datetime.datetime (which is module_datetime.class_datetime). Each of those types/classes has attributes and methods. The attributes of that class are accessed through parenthetical syntax: 

datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

So, that would be _module_datetime.class_datetime(attributes)_.

Methods are just special kinds of attributes that let you do things with data stored in the object. Instance methods work with specific objects, and class methods work at the class level. datetime.today() is a method that creates an object containing the current datetime. You can include attributes in the parentheses when you call the class method to give the object you create those attributes, depending on how the class method is defined.

So, overall, an object oriented approach to programming is not that complicated. An object is little bundle of information and potential actions. Your program creates and works with these objects to do what you want. But object-oriented programming gets its full power from the idea of a "class," or a blueprint for creating objects. Instead of working with the built-in classes/data types, we can create our own classes that construct objects with just the collection of attributes and methods needed for our program. That lets you re-use the class over and over without duplicating code, and puts a custom set of capabilities right at your fingertips.

Helpful reads:

[https://www.learnpython.org/en/Classes_and_Objects](https://www.learnpython.org/en/Classes_and_Objects)

[https://pynative.com/python-classes-and-objects/](https://pynative.com/python-classes-and-objects/)

[https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)

[https://docs.python.org/3/library/datetime.html#datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)

[https://realpython.com/instance-class-and-static-methods-demystified/](https://realpython.com/instance-class-and-static-methods-demystified/)

## Topic 12

don't see how it would be possible to make any useful program without using a list or dictionary. The concepts are not that difficult if you think about them as different kinds of containers. A **list** is like a box that holds other objects. The objects inside that box can come in or out, though the objects themselves do not change. A **dictionary** is like a box that has objects inside, but each of them has a label attached to it. You can find an object by checking the labels rather than having to sift through the objects themselves. And inside that dictionary box you can have _other_ boxes, each holding objects with their own labels. That would be a "dictionary of dictionaries," which seems to me to be particularly powerful as way to organize data. It reminds me of a relational database, with keys/labels for the columns and the objects themselves as the records. I would use a list for simple things, but rather than using "lists of lists" with complex indexing, I think it would be simpler to implement dictionaries.


## Topic 13
The author who wrote the book, "[Think Like a Programmer](https://archive.org/details/think-like-a-programmer)," says this:

“The biggest mistake I see new programmers make is focusing on learning syntax instead of learning how to solve problems.” — V. Anton Spraul

My biggest take-away from the course is the importance of thinking critically about the problem that needs to be solved and breaking down in small units, arranged in logical order. The labs in general gave us the structure already, so they were more about mastering the syntax and methods. However, I have loved the process of planning and developing the final project because it made us 'think like a programmer' in breaking the project requirements down into small steps that can be chained together. One aspect of this is creating functions and having them call each other in a logical way, but even more important and challenging is the idea of writing generic bits of code in that function that can be used over and over with different data inputs.

I'm just getting started in programming, but I enjoy how creating programs is essentially a logic puzzle. I have always appreciated "mind game" type puzzles that require you to think logically and step-by-step, and in some ways developing a python program feels like playing a game game. I fully realize that it would be a lot less like a game if I were doing it professionally with lots of pressure to perform, etc., but for now at least the homework feels more like fun than work.

[https://archive.org/details/think-like-a-programmer](https://archive.org/details/think-like-a-programmer)

[https://www.codecademy.com/resources/blog/how-to-think-like-a-programmer/](https://www.codecademy.com/resources/blog/how-to-think-like-a-programmer/)