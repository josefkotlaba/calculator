# Create a simple calculator with a function add(numbers)
#  1. The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example “” or “1” or “1,2”
#  2. Start with the simplest test case of an empty string and move to 1 and two numbers
#  3. Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
#  4. Remember to refactor after each passing test

def testSuite():
    succesfulTests=0
    tests=1
    
    if (add() == 0) :
        print("Test with zero numbers successful")
        succesfulTests=+1
    else:
        print("Test with zero numbers failed!")

    tests=+1
    if (add(1) == 1) :
        print("Test with one number successful")
        succesfulTests=+1
    else:
        print("Test with one number failed!")

    test("two numbers",1,3,4)
    test("double digits",15,16,31)
    
    if (tests==succesfulTests) : print("ALL TESTS SUCCESFUL!")
    return;

def test(description,num1=0,num2=0,output=0):
    tests=+1
    if (add(num1,num2) == output) :
        print("Test with "+description+" successful")
        succesfulTests=+1
    else:
        print("Test with "+description+" failed!")
    return;

def add(num1=0,num2=0):
    output=num1+num2
    return output;

testSuite()