student_data={
    "idl": {"name": "sara", "class":"V", "subject_intergation":"english","math","science"},
    "id2": {"name": "David", "class":"V", "subject_intergation":"english","math","science"},
    "id3": {"name": "Sara", "class":"V", "subject_intergation":"english","math","science" "},
    id4:   {"name": "surya", "class":"V", "subject_intergation":"english","math","science" "},
    }
result={}
seen_keys=[]
for studend_id, details in student_data.items():
    unique_key:(details:["name"],details["class"],detils[sunject_intergation])
    if unique_keys not in seen_keys:
        seen_keys.append(unique key)
        result=student_id[details]
for k,v in result.items():
    print(k, ":", v)