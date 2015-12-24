import string
"""
#  Name: Spalynx
#  Ver : 0.1
#  Date: 12/23/15
"""
class SPCypher:
    __FILE = ""
    __A = 3;
    __B = 3;
    
    def __init__(self, file = ""):
        self.__FILE = file

    def toCypher(self, convert):
        """Converts a string to the Cypher"""
        converted = ""; temp = 0;
        for it in convert:
            #Entire section changes ascii values to 0-25
            if (it == ' ' or ord(it) < 65): #removes whitespace and punct
                #in turn, places a space, and continues
                converted += " "
                continue
            elif (ord(it) <= 90 and ord(it) >= 65): #turns capitals to lowers
                temp = ord(it) - 65
            else: #for lowercase
                temp = ord(it) - 97

            #implements y = (ax+b)%M
            temp = (self.__A*temp - self.__B) % 26
            temp += 97

            #adds generated character
            converted += chr(temp)
        return converted

    def setA(self, A = 3):
        self.__A = A;
    def setB(self, B = 6):
        self.__B = B;

    def getA():
        return __A;
    def getB():
        return __B;
        

def main():
    """Basic IO for testing"""
    sp = SPCypher();
    conv = input("ToConvert:  ")
    print("Converted: ", sp.toCypher(conv))

if __name__ == '__main__':
    print ("%s: Running library as main." % __file__); main();
