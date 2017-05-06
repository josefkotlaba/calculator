# Create a simple calculator with a function add(numbers)
#  1. The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example “” or “1” or “1,2”
#  2. Start with the simplest test case of an empty string and move to 1 and two numbers
#  3. Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
#  4. Remember to refactor after each passing test
#
#  Allow the add​ function to handle an unknown amount of numbers
#  Allow the add​ function to handle new lines between numbers (instead of commas).
#  Allow the add​ function to handle new lines between numbers (as well as commas).

from calcString import calcString

def testSuite():
    succesfulTests=0
    tests=0

    tests+=1
    if (test("zero numbers",0,"") == "Success") : succesfulTests+=1

    tests+=1
    if (test("one number",1,"1") == "Success") : succesfulTests+=1

    tests+=1
    if (test("two numbers",7,"3\n4") == "Success") : succesfulTests+=1

    tests+=1
    if (test("two numbers",7,"3,4") == "Success") : succesfulTests+=1

    tests+=1
    if (test("double digits",31,"16\n15") == "Success") : succesfulTests+=1

    tests+=1
    if (test("double digits",31,"16,15") == "Success") : succesfulTests+=1

    tests+=1
    if (test("three numbers",6,"1\n2\n3") == "Success") : succesfulTests+=1

    tests+=1
    if (test("three numbers",6,"1\n2,3") == "Success") : succesfulTests+=1

    tests+=1
    if (test("multiple numbers",2165,"41,25\n33,156\n1,1888\n\n12,4\n5") == "Success") : succesfulTests+=1
        
    if (tests==succesfulTests) : print("ALL CALCULATOR TESTS SUCCESFUL!")
    return;

def test(description,output,str):
    if (add(str) == output) :
        print("Test with "+description+" successful")
        return("Success")
    else:
        print("Test with "+description+" failed!")
        return("Fail")
    

def add(str):
    testString=calcString(str)          
    result=testString.convertInput()    #Converts input to 
    output = 0
    for index in range(len(result)):
      output=output+int(result[index])
    return output;

testSuite()
test = calcString("test")
test.testSuite()