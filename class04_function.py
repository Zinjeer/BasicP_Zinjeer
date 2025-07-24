#def hello(name):
#    print("ค่าที่รับเข้ามาแสดงจาก function : ",name)

#name = input("ค่าที่รับ")
#hello(name)

#def sum (a,b):
#    result = a + b
#    return result

#num1 = int(input("กรอกเลขตัว1:"))
#num2 = int(input("กรอกตัวเลข2:"))

#result = sum(num1,num2)
#print(result)

#def add(num1,num2):
#    result = num1 + num2
#    return result

#def main():
#    num1 = int(input("กรอกเลขตัวที่1 :"))
#    num2 = int(input("กรอกเลขตัวที่2 :"))
#    result = add(num1,num2)
#    print("ผลลัพธ์จากการบวกคือ:",result)

#main()

def add(num1,num2):
    result = num1 + num2
    return result
 
def minus(num1,num2):
    result = num1 - num2
    return result
 
def mutiple(num1,num2):
    result = num1 * num2
    return result
 
def divide(num1,num2):
    result = num1 / num2
    return result
 
def is_even(num):
    result = num % 2
    if (result==0):
        return("เป็นเลขคู่")
    else:
        return("เป็นเลขคี่")
 
def main():
    num1 = int(input("กรอกเลขตัวที่ 1: "))
    num2 = int(input("กรอกเลขตัวที่ 2: "))
    print(" + - * / เอาอันไหนน้อง")
    print("[1] +")
    print("[2] -")
    print("[3] *")
    print("[4] /")
    operation = input("เลือกสักอัน: ")
    # ตรงนี้ให้น้องๆเขียน condition (if-else) ว่าถ้ามันตรงกับเลขนั้นในเมนูจะให้ใช้ฟังก์ชั่นอะไร
    if (operation == "1"):
        result = add(num1,num2)
        print("ผลบวกคือ:",result)
    if (operation == "2"):
        result = minus(num1,num2)
        print("ผลลบคือ:",result)
    if (operation == "3"):
        result = mutiple(num1,num2)
        print("ผลคูณคือ:",result)
    if (operation == "4"):
        result = divide(num1,num2)
        print("ผลหารคือ:",result)
    
    
 
    # เรียก is_even เพื่อเช็กว่าผลลัพที่ได้มันเป็นเลขคู่มั้ย
    print("เป็นเลขคู่หรือไม่ ",is_even(result))
 
main()