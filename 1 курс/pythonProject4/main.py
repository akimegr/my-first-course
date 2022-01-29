a = input (" Use a : ")
a = int (a)

b = input ( " Use b : " )
b = int (b)

c = input (" (+ , - , * , /) : \t ")


if c == "+" :
    result = str (a) + " + " + str (b) + " = " + str (a+b)
    print ( " a + b = " + result )
elif c == "-" :
    result2 = str (a) + " - " + str (b) + " = " + str (a-b)
    print (" a - b = " + result2 )
elif c == "*" :
    result3 = str (a) + " * " + str (b) + " = " + str (a * b)
    print (" a * b = " + result3 )
elif c == "/" :
    result4 = str (a) + " / " + str (b) + " = " + str (a / b)
    print (" a / b = " + result4 )
else :
    print ("false")
