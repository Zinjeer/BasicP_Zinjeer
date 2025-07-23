username = input("Username :")
password = input("Password :")

if username == "admin" :
    if password == "admin123":
        print("You're admin")
    else:
        print("wrong")
elif username == "user":
    if password == "user123":
        print("You're usre")
    else:
        print("wrong")
else:
    print("Not found")


#----------------------------------------------------

x = input("word:(สัตว์ กด A สิ่งของ กด B)")
word = ""
D = "หมา"
C = "แมว"
E = "ช้าง"

F ="พัดลม"
S ="โซฟา"
P ="กระทะ"

if x=="A":
    input1 = input("เลือกตัวไหน (D=หมา C=แมว E=ช้าง)")
    if input1 == "D":
        word += "สัตว์คือหมา"
    else:
        word += "ไม่มีสัตว์ชนิดนี้"
    if input1 == "C":
        word += "สัตว์คือแมว"
    else:
        word += "ไม่มีสัตว์ชนิดนี้"
    if input1 == "E":
        word += "สัตว์คือช้าง"
    else:
        word += "ไม่มีสัตว์ชนิดนี้"
elif x == "B":
    input2 = input("เลือกชิ้นไหน(F=พัดลม S=โซฟา P=กระทะ)")
    if input2 == "F":
        word += "สิ่งของคือพัดลม"
    else:
        word += "ไม่มีของชนิดนี้"
    if input2 == "S":
        word += "สิ่งของคือโซฟา"
    else:
        word += "ไม่มีของชนิดนี้"
    if input2 == "P":
        word += "สิ่งของคือกระทะ"
    else:
        word += "ไม่มีของชนิดนี้"
else :
    print("ไม่มีข้อมูล")

print(word)



    



