# Create a simple calculator with a function add(numbers)
#  1. The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example “” or “1” or “1,2”
#  2. Start with the simplest test case of an empty string and move to 1 and two numbers
#  3. Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
#  4. Remember to refactor after each passing test
#
#  Allow the add​ function to handle an unknown amount of numbers
#  Allow the add​ function to handle new lines between numbers (instead of commas).
#  Allow the add​ function to handle new lines between numbers (as well as commas).
#  Support different delimiters
#    - to change a delimiter, the beginning of the string will contain a separate line that looks like this:
#      “//[[delimiter]]\n[numbers...]”
#       for example “//[;]\n1;2” should return three where the default delimiter is ‘;’ .
#    - the first line is optional. all existing scenarios should still be supported
#   Calling add​ with a negative number will raise a ValueError “negatives not allowed” - and the negative that was passed.
#   If there are multiple negatives, show all of them in the exception message

class Calculator:
    'Main class for the calculator'
    succesfulTests=0
    tests=0
from calcString import calcString

def test(description,output,str):       #Test function
    Calculator.tests+=1
    if (add(str) == output) :
        print("Test with "+description+" successful")
        Calculator.succesfulTests+=1
        return
    else:
        print("Test with "+description+" failed!")
        return

def testSuite():                #run this to perform functional tests
    test("zero numbers",0,"")
    test("one number",1,"1")
    test("two numbers, newline",7,"3\n4")
    test("two numbers, comma",7,"3,4")
    test("double digits",31,"16\n15")
    test("double digits",31,"16,15")
    test("three numbers",6,"1\n2\n3")
    test("three numbers",6,"1\n2,3")
    test("multiple numbers",2165,"41,25,33,156,1,1888,,12,4,5")
    test("multiple numbers, newline delimiter",2165,"41\n25\n33\n156\n1\n1888\n\n12\n4\n5")
    test("multiple numbers, multiple delimiters",2165,"41,25\n33,156\n1,1888\n\n12,4\n5")
    test("multiple numbers, custom delimiter",2165,"//[a]\n41a25\n33,156\n1,1888\n\n12a4\n5")
    test("multiple numbers, [ delimiter",2165,"//[[]\n41[25\n33,156\n1,1888\n\n12[4\n5")
    test("multiple numbers, ] delimiter",2165,"//[]]\n41]25\n33,156\n1,1888\n\n12]4\n5")
    test("multiple numbers, [] delimiter",2165,"//[[]]\n41[]25\n33,156\n1,1888\n\n12[]4\n5")
    #test("negatives",0,"-1,-2,3") #this one throws ValueError on purpose
        
    if (Calculator.tests==Calculator.succesfulTests) : print("ALL CALCULATOR TESTS SUCCESFUL!")
    return;


    

def add(str):
    testString=calcString(str)          
    intList=testString.convertInput()    #Converts input to list of ints
    output = 0
    for index in range(len(intList)):
      output=output+int(intList[index])  #Adds the ints
    getNegatives(intList)
    
    return output;

def getNegatives(numList):
    negatives = []
    for index in range(len(numList)):
        if numList[index] < 0 : negatives.append(numList[index])
    if (negatives == []):
        return negatives
    else:
        raise ValueError("Negatives not allowed: ",negatives)

testSuite()
test = calcString("test")
test.testSuite()