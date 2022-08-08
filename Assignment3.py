"""
1. Why are functions advantageous to have in your programs?

Ans: Functions are advantageous because of the following reasons:
a. Suppose, we have to do repetitive tasks using a code. Instead of writing the same code for multiple data, we can write a function which can take some
input, process on it and return an output. It decreases the need of writing duplicate codes.
b: It improves the reuasability of code as we do not have to write everything from scratch.
c: It increases the readability and also helps in debugging, thus making our program less prone to errors.


2. When does the code in a function run: when it's specified or when it's called?

Ans: The code in a function runs when we call the function, not when we specify / declare the function.

3. What statement creates a function?

Ans: def statement creates a function. The syntax is:
        def fun_name(parameter):
            body of function

4. What is the difference between a function and a function call?

Ans: A function is just a collection of statements and function definition.
     A function call is when the statements inside the function take up a value / get executed and return something as defined in the function.

5. How many global scopes are there in a Python program? How many local scopes?

Ans: There is only one global scope,i.e. outside of function. It can be accessed anywhere , i.e. inside or outside of a function.
     Local scopes are created whenever we are inside a function and it can be accessed inside that function only.

6. What happens to variables in a local scope when the function call returns?

Ans: All the local variables and memory space occupied by them are made free. The local scope is destroyed.

7. What is the concept of a return value? Is it possible to have a return value in an expression?

Ans: A return value is the value obtained by function, which is returned to the calling function.
     Yes, its possible to have a return value in an expression also.
     e.g. (5==6) returns False

8. If a function does not have a return statement, what is the return value of a call to that function?

Ans: 'None' is the return type of that function which does not explicitly have a return statement.

9. How do you make a function variable refer to the global variable?

Ans: A function variable can be made to refer to the global variable by writing the keyword 'global' just before the
     local variable.

10. What is the data type of None?

Ans: NoneType

11. What does the sentence import areallyourpetsnamederic do?

Ans: This statement imports a python module if a module named 'areallyourpetsnamederic' is available. A module is a file
     containing codes written by someone earlier which can be imported and used by the present user.

12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

Ans: spam.bacon()

13. What can you do to save a programme from crashing if it encounters an error?

Ans: Place that line in try block and place an 'except Exception as e' block.

14. What is the purpose of the try clause? What is the purpose of the except clause?

Ans: Try clause mainly contains that piece of code which can potentially run into errors if the data is not standard.
     Except clause contains that piece of code which handle those potential errors, and show the kind of errors without interruption of the whole program.
"""

