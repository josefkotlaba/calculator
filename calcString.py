class calcString:
    'Input string for the add function. Transforms input string and returns list of numbers'
    

    def __init__(self, input):
        self.stringToConvert = input
        self.output = []
        
    def testSuite(self):
        succesfulTests=0
        tests=0

        tests+=1
        self.stringToConvert=""
        if (calcString.convertInput(self) == [0]): succesfulTests+=1; print("Test \"\" succesful")

        tests+=1
        self.stringToConvert="1"
        if (calcString.convertInput(self) == [1]): succesfulTests+=1; print("Test \"1\" succesful")

        tests+=1
        self.stringToConvert="1\n2"
        if (calcString.convertInput(self) == [1,2]): succesfulTests+=1; print("Test \"1\n2\" succesful")

        tests+=1
        self.stringToConvert="1\n\n2"
        if (calcString.convertInput(self) == [1,0,2]): succesfulTests+=1; print("Test \"1\n\n2\" succesful")

        if (tests==succesfulTests) : print("ALL CALCSTRING TESTS SUCCESFUL!")
        return;

    def convertInput(self):
        self.output=self.stringToConvert.split('\n')     #Splits input string into list of strings delimited by a comma
        for index in range(len(self.output)):
            if (self.output[index] == ''): self.output[index]='0'    #If there is an emlty string in the list, it gets converted to 0

        for index in range(len(self.output)):
            self.output[index]=int(self.output[index])  #Converts strings to ints

        return self.output

#test1 = calcString("")
#test1.testSuite()