

money = float(input("insert the money..."))


cost = money

numeroViajes = cost / 50



if numeroViajes < 1: 
    print('no puedes viajar con esta cantidad')
if numeroViajes ==1:
        
    print ('puedes costear ' + str(int(numeroViajes)) + ' viaje')

else :
   print('puedes costear ' + str(int(numeroViajes)) + ' viajes')
