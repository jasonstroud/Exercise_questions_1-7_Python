# Exercise_questions_1-7_Python
Programming exercises written in Java and Python

QUESTION 1 – FORMATTED OUTPUT

Create a program that displays the output given below. You will need to make use of the Escape Sequence characters to format the text correctly.
Hints: The backslash (\) and the double quotes (“) are both special characters. To make them appear in a string as normal characters, both need a backslash in front of them. For example, “\\” gives a single backslash as a normal character, whereas “\”” gives a double quote character.
Note: You are required to use formatted output to line up the columns. To line up the columns, do not manually insert whitespace characters, do not use the tab combination \t. Use printf and formatting template to achieve column width instead.
The following is a sample run output:

![image](https://user-images.githubusercontent.com/72170460/160956434-b77d68c9-351a-438e-a194-326ffb627304.png)

QUESTION 2 – ARITHMETIC CALCULATION

Write a program that asks for two numbers from the user (data type: double) as rectangle height and width. Calculate rectangle area and perimeter, and display the results using printf and formatting template (round up results to 2 decimal points).
Formula for calculating rectangle area and perimeter are as follows:
area=height*width
perimeter=(height+width)*2
The following is a sample run output:

![image](https://user-images.githubusercontent.com/72170460/160956566-68218e99-fcda-45eb-b7a1-f947046cfa52.png)

QUESTION 3 – SELECTION

Write a program that asks the user for a number as a month. If the user input number falls outside 1 – 12, display an error message. Otherwise, display a season’s message based on the following:

**Month**               **Season**
12, 1-2 inclusive         Summer
3-5 inclusive             Autumn
6-8 inclusive             Winter
9-11 inclusive            Spring

The following are three sample run outputs:

Sample run #1:
Enter a number for month (1-12): 2
Wonderful summer

Sample run #2:
Enter a number for month (1-12): 5
Colourful autumn

Sample run #3:
Enter a number for month (1-12): 20
20 is an invalid season number


QUESTION 4 – USER INPUT VALIDATION

Write a program that asks from the user for the letter of a play card. The user input must be either J, Q, K, or A. Your solution should allow user to type in either upper or lower case. Perform user input validation, i.e, if user input is not one of the four specified letters, your program must prompt for re-entry until a valid input is received. Once a valid letter is received, a selection statement should be used to display the corresponding card name based on the following:

Card letter: J, Q, K, A
Card name: Jack, Queen, King, Ace

**A sample run is as follows:**
Enter card letter (j/q/k/a): b
Invalid, try again.
Enter card letter (j/q/k/a): p
Invalid, try again.
Enter card letter (j/q/k/a): a
It’s an Ace


QUESTION 5 – COUNT THE INTERSECTION OF TWO ARRAYS

Write a program that asks the user to enter two lines of comma-separated decimal numbers and counts how many numbers are overlapping between the two lines. See sample run below.

Your program first reads each input line as a single string, split the line into an array of numeric strings, and convert to either an array or list of double numbers, as illustrated in steps below:

Step 1
Read a line as a single string
“1.3,4.5,7.0,6.5,11,48”

Step 2
Split the line into a string array
“1.3”, “4.5”, “7.0”, “6.5”, “11”, “48”

Step 3
Convert each numeric string to a double or float value, and add each double/float value to either an array or list
1.3, 4.5, 7.0, 6.5, 11, 48

Once you’ve got the two double arrays/lists, use two nested for-each loops (one inside another) to iterate through the two double arrays/lists, compare each element from the first array/list to each of the second array/list, increment a counter variable every time an overlapping number is found.
Note:
• you do not have to input-check whether the user has typed all numeric values. But you should not assume that the two lines contain the same number of items.
• When comparing the numbers, 7 and 7.0 are considered equal.
• You can assume each line contains only unique numbers, e.g., there are no duplicate numbers in each line.

**A sample run is as follows:**
Enter first line: 1.3,4.5,7.0,6.5,11,48
Enter second line: 2.5,4.1,7,6.5,11.0
Number of overlapping values: 3


QUESTION 6 – GUESSING GAME

Write a program that asks the user to guess a computer generated secret number. The program asks the user to enter a line of comma-separated integer numbers. Your program should read from the user a line of comma-separated integer numbers (note, the line of numbers should be read in as a single string), split the line into an array of numeric strings, and convert the string array to either an array or a list of integers. If one of the user entered numbers matches the pre-generated secret number, the user won, otherwise the user lost the game. In the case of using winning, your program should also tell the user the position of the winning number, as shown in the two sample runs below.

The following two sample runs illustrate the two cases (game lost and won):

Sample run 1
Enter comma-separated numbers to guess my secret number (1-10): 1,3,4,6,9
My secret number is 8
You lost

Sample run 2
Enter comma-separated numbers to guess my secret number (1-10): 2,3,5,7,8,9,10
My secret number is 7
You won
The 4th attempt in your numbers is my secret number


QUESTION 7 – INPUT DATA PROCESSING

StockSmithTech is a stock broker company that collects stock data and conducts stock screening and processes stock for their customers. Write a program to simulate the data collecting process by requesting a series of stock prices to be entered by the user.

1. The program first asks from the user for how many stocks to process. The user input must be greater than zero, or the user must be prompted for re-entry until valid input is received.
2. The received integer number is then used as array capacity to create an array of stock prices (data type: double). The program then uses a loop to read the values from the user and save in the array. Hint: You’ll have to use the array length to control the iteration of the loop. Note, you could choose to use list instead of array to implement your solution.
3. Your program should calculate and display the average stock price, the maximum, and how many stocks are currently between price 1.5 and 5.5, including 1.5 and 5.5.
4. Your program should also allow the user to query price by stock number. Ask the user for a stock number, perform user input checking (i.e., stock number must be between 1 and the total number of stocks). Use the user entered stock number to retrieve price from the array( or list).

Note, do not assume from the sample run below that there are only 4 stocks – your solution must be general and able to handle any number of stocks entered by the user.

**Sample run output as follows:**

--Collecting data--
How many stocks: 4
Enter price for stock #1: $5.8
Enter price for stock #2: $1.02
Enter price for stock #3: $2.05
Enter price for stock #4: $7.19

--Display statistics--
Average price: $4.02
Maximum price: $7.19
Stocks priced between $1.5 and $5.5: 1

--Query stock price--
Enter stock number (1-4): 5
Stock doesn’t exist. Enter again.
Enter stock number (1-4): 0
Stock doesn’t exist. Enter again.
Enter stock number (1-4): 4
Price for stock #4: $7.19
