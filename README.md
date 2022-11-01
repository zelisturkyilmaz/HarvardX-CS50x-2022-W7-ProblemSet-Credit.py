# CS50's Introduction to Computer Science
## HarvardX - CS50x
### Week 7 Problem Set - Credit.py
<hr>


### Assignment and Requirements:
Write and execute the program that prompts the user for a credit card number and then reports whether it is a valid via using Luhn’s Algorithm and whether it is American Express, MasterCard, or Visa card number, per the definitions of each’s format.
\
Here’s how the program might work when prompted:
```Python
$ python credit.py
Number: 4003600000000014
VISA
```

```get_long``` itself will reject hyphens (and more) :

```Python
$ python credit.py
Number: 4003-6000-0000-0014
Number: foo
Number: 4003600000000014
VISA
```

Catch inputs that are not credit card numbers (e.g., a phone number), even if numeric:

```Python
$ python credit.py
Number: 6176292929
INVALID
```

#### Luhn’s Algorithm:
Most cards use an algorithm invented by Hans Peter Luhn of IBM. According to Luhn’s algorithm, you can determine if a credit card number is (syntactically) valid as follows:

1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
2. Add the sum to the sum of the digits that weren’t multiplied by 2.
3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid.


#### Credit Cards:

American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers. 

All American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55 (they also have some other potential starting numbers which we won’t concern ourselves with for this problem); and all Visa numbers start with 4.

#### Compiling And Execution:

To run a program we wrote in Python, we’ll only need to run:

```Python
$ python credit.py
```
```python``` is the name of a program called an interpreter, which reads in our source code and translates it to code that our CPU can understand, line by line.
