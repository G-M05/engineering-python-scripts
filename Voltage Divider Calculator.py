#v=IR
#voltage divider can only be used on components in series
#voltage divider base eq vout = vin* R2/(R1+R2)
# assumes user inputs integer values

# Version 1

#        Vin = float(input("What is your vin? "))
#        R1 = float(input("What is your R1? "))
#        R2 = float(input("What is your R2? "))
#        ratio = R2/(R1+R2)
#        Vout = Vin * ratio

# Version 2

Vin = float(input("Vin(V) = "))
R1 = float(input("R1(Ohms) = "))
R2= float(input("R2(Ohms) = "))

Vout = Vin * (R2/(R1+R2))

print (f"Your Vout is {Vout: .2f}V")
