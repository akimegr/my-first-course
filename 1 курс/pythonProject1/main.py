print (" hello , friend! ")
name = input (" What is name? :  ")

print ("Good , " + name + ", my name is Egor ")

question = input ( "You want calculate ? yes or no??? : " )

while question == "yes" :
else :
    print g
    question == "yes"
    print (" Go! ")

except question == "no" :

    print (" :( ")



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