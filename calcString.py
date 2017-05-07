class calcString:
    'Input string for the add function. Transforms input string and returns list of numbers'
    succesfulTests=0
    tests=0

    def __init__(self, input):
        self.stringToConvert = input
        self.output = []

    def test(self,description,output,str):       #Test function
        calcString.tests+=1
        self.stringToConvert=str
        if (calcString.convertInput(self) == output) :
            print("Test with "+description+" successful")
            calcString.succesfulTests+=1
            return
        else:
            print("Test with "+description+" failed!")
            return
        
    def testSuite(self):    
        calcString.test(self, "\"\"",[0],"")
        calcString.test(self, "\"1\"",[1],"1")
        calcString.test(self, "\"1\\n2\"",[1,2],"1\n2")
        calcString.test(self, "\"1,\\n2\"",[1,0,2],"1,\n2")
        calcString.test(self, "\"//[oo]\\n1,2\\n3o4\"",[0,0,0,1,2,3,4],"//[oo]\n1,2\n3oo4")
        calcString.test(self, "\"//[[]\\n1,2\\n3[4\"",[0,0,0,0,1,2,3,4],"//[[]\n1,2\n3[4")
        calcString.test(self, "empty string",[0],"")
        calcString.test(self, "empty string",[0],"")
        calcString.test(self, "empty string",[0],"")

        if (calcString.tests==calcString.succesfulTests) : print("ALL CALCSTRING TESTS SUCCESFUL!")
        return;



    def convertInput(self):
        #self.stringToConvert=self.stringToConvert.replace("\n", ",")           #Replaces all commas with new lines
        convertString = self.stringToConvert
        delimiters=["\n",",","//"]                            #List of available delimiters
        #self.output=self.stringToConvert.split('\n')     #Splits input string into list of strings delimited by new lines

        newlineDelimitedString = convertString.split('\n')
        if newlineDelimitedString[0].startswith("//[") :    #If a first line starts with //
             newDelimiter=newlineDelimitedString[0]
             newDelimiter=newDelimiter[3:-1]                #get the part between brackets
             delimiters.append(newDelimiter)                #and add it to delimiter list 

        for index in range(len(delimiters)):
            convertString = convertString.replace(delimiters[index],",") #replace all delimiters with commas

        self.output = convertString.split(',')
        
        for index in range(len(self.output)):
            if (self.output[index] == ''): self.output[index]='0'    #If there is an empty string in the list, it gets converted to 0

        for index in range(len(self.output)):
            if self.output[index] in ['[',']'] : self.output[index] = '0'
            self.output[index]=int(self.output[index])  #Converts strings to ints

        return self.output

test1 = calcString("")
test1.testSuite()