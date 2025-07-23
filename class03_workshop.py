mon = 100
weapon1 = 60
weapon2 = 40
weapon3 = 20

start = True
while start:
    print("เลือกวิธีที่ต้องการเล่น")
    print("1=สู้ต่อ")
    print("2=พอแค่นี้")
    x = int(input("กรุณากรอกตัวเลข :"))
    if(x==1):
        y = int(input("ตีมอนเตอร์กี่ครั้ง"))
        print("มอนเตอร์เหลือเลือด",mon,"exp")
        print("เลือกอาวุธ")
        z = int(input("weapon1(กด11) = 60 weapon2(กด22) = 40 weapon3(33) = 20"))
        for i in range (y):
            if z == "11" :
                print("มอนเตอร์เหลือเลือด",mon-weapon1,"exp")
            if z == "22" :
                print("มอนเตอร์เหลือเลือด",mon-weapon2,"exp")
            if z == "33" :
                print("มอนเตอร์เหลือเลือด",mon-weapon3,"exp")
        if (mon < 0):
            print("มอนเตอร์ตาย Game over")
        elif(mon != 0):
            print("คุณตาย")
    else:
        print("Game over")
        break
start=False