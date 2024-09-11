from fractions import Fraction

class RationalNumber:
    
    def generaterationalnumber(numerator,denominator):
        if(not isinstance(numerator,int)):
            raise TypeError("The numerator value has to be an integer")
        if(not isinstance(denominator,int)):
            raise TypeError("The denomenator value has to be an integer")
        else:
            rationalnumber = Fraction(numerator,denominator)
            print(rationalnumber)
