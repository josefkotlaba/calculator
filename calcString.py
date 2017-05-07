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
        calcString.test(self, "\"//[oo]\\n1,2\\n3o4\"",[1,2,3,4],"//[oo]\n1,2\n3oo4")
        #calcString.test(self, "\"//[[]\\n1,2\\n3[4\"",[0,0,0,0,1,2,3,4],"//[[]\n1,2\n3[4")
        calcString.test(self, "\"//[a][b]\\n1a2b3,4\\n5\"",[1,2,3,4,5],"//[a][b]\n1a2b3,4\n5")

        if (calcString.tests==calcString.succesfulTests) : print("ALL CALCSTRING TESTS SUCCESFUL!")
        return;



    def convertInput(self):
        #self.stringToConvert=self.stringToConvert.replace("\n", ",")           #Replaces all commas with new lines
        convertString = self.stringToConvert
        delimiters=["\n",",","//"]                          #List of default delimiters
        #self.output=self.stringToConvert.split('\n')       #Splits input string into list of strings delimited by new lines

        newlineDelimitedString = convertString.split('\n')
        if (newlineDelimitedString[0].startswith("//[") and newlineDelimitedString[0].endswith("]")):    #If a first line starts with //[ and ends with ]
            convertString=convertString.split("\n",1)[1]
            delimiterLine=newlineDelimitedString[0]
            for delimIndex in (0,newlineDelimitedString[0].count("[")):
                    newDelimiter = ""
                    newDelimiterStartIndex = delimiterLine.find("[")
                    newDelimiterEndIndex = delimiterLine.find("]")
                    newDelimiter = delimiterLine[newDelimiterStartIndex+1:newDelimiterEndIndex]                #get the part between brackets
                    delimiters.append(newDelimiter)                #add it to delimiter list 
                    delimiterLine = delimiterLine[0:newDelimiterStartIndex]+delimiterLine[newDelimiterEndIndex+1:] #and remove the delimiter from the delimiter string

        

        for index in range(len(delimiters)):
            convertString = convertString.replace(delimiters[index],",") #replace all delimiters with commas

        self.output = convertString.split(',')
        
        for index in range(len(self.output)):
            if (self.output[index] == ''): self.output[index]='0'    #If there is an empty string in the list, it gets converted to 0

        #self.output.remove(0)
        for index in range(len(self.output)):
            if self.output[index] in ['[',']',']['] : self.output[index] = '0'
            self.output[index]=int(self.output[index])  #Converts strings to ints
        
        return self.output

test1 = calcString("")
test1.testSuite()