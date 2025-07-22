km = int(input("กรอกระยะทาง"))

if(km>=0 and km<=4):
    print("ส่งฟรี")
if(km>=5 and km<=50):
    print("10 บาท")
if(km>=51 and km<=100):
    print("15บาท")
if(km>=101 and km<=300):
    print("25บาท")
if(km>=301 and km<=500):
    print("35บาท")
if(km>500):
    print("45บาท")