a = input (" Figuar a : ")
a = int (a)

b = input (" Figuar b : ")
b = int (b)

c = input (" введите + , - , * , / , ** ")

if c == "+" :
    result = str (a) + "+" + str (b) + "=" + str (a+b)
    print (' ваш результат : ' + result )

elif c == "-" :
    result = str(a) + "-" + str(b) + "=" + str(a - b)
    print(' ваш результат : ' + result)
elif c == "*" :
    result = str(a) + "*" + str(b) + "=" + str(a * b)
    print(' ваш результат : ' + result )
elif c == "/" :
    result = str(a) + "/" + str(b) + "=" + str(a / b)
    print(' ваш результат : ' + result )
elif c == "**" :
    result = str(a) + "**" + str(b) + "=" + str(a ** b)
    print(' ваш результат : ' + result )
else :
    print (" false ")