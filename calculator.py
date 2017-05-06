# Create a simple calculator with a function add(numbers)
#  1. The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example “” or “1” or “1,2”
#  2. Start with the simplest test case of an empty string and move to 1 and two numbers
#  3. Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
#  4. Remember to refactor after each passing test

def testSuite():
    if (add("") == "") : print("Test add() successful") #Test with zero numbers
    return;
  

def add(str):
    input = str

    output=input
    print(output)
    return output;

testSuite()