## Learning log 05-11-2026

- Functions: print("")
- Arguments: input to a function that influences its behavior
- str: string >>> sequence of text
- \n: new line
- escaping: print "Hello, \"friend\"": hello, "friend"
- f-string: format string

## Learning log 06-11-2026
- integer: int
- %: modulus, remainder of dividing one number on another
- prioritize readability in your own code is a very good habit. Simplicity tends to be a good habit too.
- float: number with a decimal point
- "[]": square brackets mean you're about to see something optional
- hello(): this is how every function looks like
- "** 2": raises the thing on the left to the power on the right
- "pow(n,2)": does exactly the same function as "** 2"

## Problem set 0:
# Indoor
- learn .lower() and the input argument
- check50: checks my code, but doesn't submit it
- submit50 drops the code in a different repository (me50)
- Being inside the directory is required before running check50 & submit50
- GitHub doesn't allow password, a personal token is required

# Playback
- replace(old, new): returns a new string, doesn't change the original (strings are immutable), so the result must be stored or printed.

# Faces
- "return" gives back a value for the caller and doesn't print anything
- When calling main(), you don't use ":"

# Einstein
- Getting familiar with structuring code using the "main()" function convention.
- input() always returns a string, so it must be converted with int().

# Tip Calculator
- Variables define inside a function are local, and a function only receives data through its parameters.
- i used dollars inside a function that only had d.

## Problem set 1:
# Deep Thought
- .strip() removes spaces on both ends and .lower() ignores capitalization, so the input is normalized before comparing.
- Checking a value against several accepted answers keeps the program simple.

# Home Federal Savings Bank
- .startswith(text) checks the beginning of a string; .endswith(text) checks the end.
- Order of if/elif matters: the first condition that is true wins, so the most specific case goes first.

# File Extensions
- Normalize the input first (.strip().lower()), then check how the file name ends with .endswith().
- endswith() also accepts a tuple, so ('.jpg', '.jpeg') checks both endings in one condition.

# Math Interpreter
- float() accepts decimals, int() doesn't; use float() when the result can have a decimal part.
- Splitting the input gives a list, so I check len() before using its items.
- Code inside the else block must be indented; the calculation belongs inside it.
- "5 + a" gives a ValueError on purpose for now; try/except comes in lecture 3.

# Meal Time
- A function should use its parameter, not a variable than only exists in main().
- if __name__ == "__main__": runs main() only when the file is run directly, not when it is imported.
