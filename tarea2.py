
print("the function of the app, is for seeker pars numbers or impars numbers")
print ("this number is par?")

seeker = int(input("write a number"))

seeker = seeker %2

if seeker == 0:
    print("this number is par")

else:
    print('this number is impar')