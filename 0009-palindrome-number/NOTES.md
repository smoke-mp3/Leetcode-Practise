## How I wrote the code and what it taught me

### My Logic
1. I used `str(x)`,built-in function to convert the number into a string and saved it in a variable called `convstring`.
2. I reversed the text using Python string slicing `[::-1]`, the double colons allowed the text to be read from start to end and -1 reversed it and then I stored it in the variable `reverse`.
3. Lastly, I used `return reverse == convstring` to verify if its a palindrome or not

### Key Lessons Learned
* **String Slicing:** Adding `[::-1]` to the end of a string tells Python to read it backward one character at a time.
* **String vs Number** You can find a palindrome without converting it into string and requires simple maths, on the other hand in string it requires simple functions.
* **Return vs Print:** Leetcode expects a `return` value rather than a `print()` statement.
