#apparently in this case the list is not bound at function execution, it is bound at function definition...
#By the documentation: default parameter values are executed from left to right when the function definition is executed
#Which basically means that default parameters get the same value every time the function gets executed without paramenters...
#This also means the object is static, bound to that parameter and it can be accessed from within the
#function at runtime, when the function gets executed and its value is permanently modified for the rest of the compiler session
#So, we don't get a new y every time the function gets executed without it being passed as a parameter
#the fuction just goes to where it was defined and says: Yelp, that's my y.
def make(x,y=[]):
    y.append(x)
    print(y)

for i in [5,8,20,2]:
    if i not in [10,20,30]:
        make(i)
    else:
        make(i,["A","B","C"])
