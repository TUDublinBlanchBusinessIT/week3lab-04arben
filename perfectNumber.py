#Arben_Ozcikrikci
#17/02/2025
#perfectNumber.py

#A perfect number is one for which all the divisors of the number add up to the
#number itself. For example the divisors of 28 are 1,2,4,7,14 which added together gives 28
#write a function below called perfectNumber(x) which checks to see if x is a perfect number
#The function should return True if the number is perfect and False if it is not

#from divisors import divisors

from divisors import divisors
def isperfectNumber(n):
    if sum(divisors(n)) == n:
        return True
        return False
print(isperfectNumber(8128))
if (isperfectNumber(8128)): print("8128 is a perfect number")
    
#define the function header called perfectNumber expecting one argument


    #set a result variable to False by default


    #if the sum of all the divisors of the number is equal to the test number

        #set the result variable to be True
 

    #return the result variable


#uncomment the following line to test the perfectNumber function it should return True


