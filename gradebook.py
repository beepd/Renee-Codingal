gradebook={
    "Aditi":[85,97,77],
    "Rohan":[85,91,89],
    "Meera":[70,65,72],
    "Kabir":[99.84,91]  
}
toppers_above_90=set()
averages={}
for name,marks in gradebook.items():
    avg=sum(marks)/len(marks)
    averages[name]=avg
    for m in marks >90:
        toppers_above_90.add(name)
toppers=max(averages,key=averages)
print("Averages",key=averages)
print("Scored above 90 in some subjects",toppers_above_90)
print("Class topper",toppers)