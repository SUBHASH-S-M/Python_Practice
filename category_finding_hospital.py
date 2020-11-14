#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    s=[]
    for i in "P","E","O":
        
        s.append((medical_speciality.get(i),
        patient_medical_speciality_list.count(i)))
    def takeSecond(elem):
        return elem[1]
    s.sort(reverse=True,key=takeSecond)
    return(s[0][0])
#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)