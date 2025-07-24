#x = ["Sun","Tik","Ton","Vava","Gap"]

#print(x)

#x[0] = "Vava"

#print(x)

#x.append("Ton")

#print(x[2])

#x.pop(0)
#print(x)


#for i in range(len(x)):
#    print(x[i])

#for speaker in x:
#    print(speaker)

#score = [99,10,23,50]
#sum = 0
#for i in range(len(score)):
#    print(sum)
#    sum += score[i]

#print("total:",sum)

#num = [1,2,3,4,5,6,7,8,9,10]

#for number in num :
#    if (number %2 ==0):
#        print("Even:",number)
#    else:
#        print("Odd:",number)

#x = {"name": "Sun", "sid": 681305}

#x["score"]=100

#print(x["name"],x["sid"])

#students = [
#    {"name" : "Sun", "sid" : 671305 ,"score" : "100"},
#    {"name" : "Tik", "sid" : 671305 ,"score" : "1000"},
#]
#for student in students:
#    print(student["name"],students["score"])

students = [
    {"name" : "A", "ID" : "123", "score":"60"},
    {"name" : "B", "ID" : "1234", "score":"70"},
    {"name" : "C", "ID" : "12345", "score":"80"}
]

for student in students:
    if (student["score"] >= 90):
        student["score"]="A"
    elif (student["score"]>= 80):
        student["score"]="B"
    if (student["score"]>= 70):
        student["score"]="C"
    else :
        student["score"]="F" 
print(student)