#sum = 0
#n = 3

#for i in range(n):
#    sum += i+1

#print(sum)

#for i in range(10):
#    if (i % 2) == 0:
#       print("Even number:",i)

#x = int(input("อยากได้แม่สูตรคูณไหน:"))

#for i in range(13):
#    print(x,"*",i,"=",x*i)

#i = 0
#while i < 5:
#    print("hello")
#    i += 1
#    if i == 4:
#        break

start = True
while start:
    print("เลือกข้อที่ต้องการเล่น")
    print("ข้อที่[1] โจทย์แรก")
    print("ข้อที่[2] โจทย์สอง")
    x =int(input("กรุณากรอกตัวเลข :"))
    if(x==1):
        print("ทำโจทยNที่1")
    elif(x==2):
        print("ทำโจทย์ที่2")
    start = False

    