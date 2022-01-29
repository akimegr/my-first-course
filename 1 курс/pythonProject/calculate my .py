print (" hello , friend! /n ")
name = input (" What is name? :  ")

print ("Good , " + name + " My name is Egor ")

question = input ( "You want calculate ? yes or no??? : " )
if question == "yes" :
    print (" Go! ")
elif question == "no" :
    print (" :( ")
else :
    print (" go back ")

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