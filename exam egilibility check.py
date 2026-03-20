medical_cause=input("Do you have a medical cause? (Y/N):").strip().upper()
if medical_cause=="Y":
    print("You are alowed")
else:
    atten=int(input("Enter the attendence of the student:"))
if atten >=75:
    print("Allowed")
else:
    print("Not allowed")
    
