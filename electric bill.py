units=int(input("Please enter Number of Units you consumed "))
if units <50:
    amount=units*2.60
    surcharge=25
elif (units <= 100):
    amount= 130+ ((units-50)*3.5)
elif (units <= 200):
    amount= 130+162.50+((units-50)*5.25)
else:
    amount=130+162.50+526+((units-200)*8.45)
total=amount+surcharge
print("/nElectricityBill=%.2f"%total)