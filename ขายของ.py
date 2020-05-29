a = []
num = 0
while True:
    b = input('* * * SIXTY SHOP * * *\n Fantech [f]\n Signo [s]\n Razer [r]\n NUBWO [k]\n ตระกร้าสินค้า [x]\n ออกจากร้าน [o]\n สั่งซื้อสินค้า [t]\n')
    b = b.lower()
    if b == 'f': #สร้างเงื่อนไขให้โปรแกรมรอรับค่าทางแป้นพิมพ์
        print("***** Fantech *****")
        print("A) MK852 MAX CORE Price 1090฿")
        print("B) HG175 BLACK Price 390฿")
        b=input("เลือกสินค้าที่ต้องการ: ")
        if b == "a":
            a.append("MK852 MAX CORE                      1090฿            20%")    #วิ่งเข้าหาตัวแปร
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n") #แจ้งลูกค้าหลังจากรับค่าทางแป้นพิมพ์
            num+= 872
        elif b == "b":
            a.append("HG175 BLACK                         390฿             20%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 312
        else: print("\n!@#$%^&* !!กรอกดีดี!! *&^%$#@!\n") #หากผิดหรือแตกต่างไปจากเงื่อนไขให้โปรแกรมฟ้องERRORแล้ววนกลับไปรับค่าใหม่
    if b == "s": #เงื่อนไขที่ 2
        print("****** Signo *****")
        print("A) MP-704 USB Condenser Microphone 850฿")
        print("B) KB-728 INVEGO Mechanical 1090฿")
        print("C) GM-907 CENTRO Macro Gaming Mouse 290฿")
        b=input("เลือกสินค้าที่ต้องการ: ")
        if b == "a" :
            a.append("MP-704 USB Condenser Microphone     850฿             15%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 722.5
        elif b == "b" :
           a.append("KB-728 INVEGO Mechanical            1090฿            15%")
           print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
           num+= 926.5
        elif b == "c" :
            a.append("GM-907 CENTRO Macro Gaming Mouse    290฿             15%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+=246.5
        else: print("\n!@#$%^&* !!กรอกดีดี!! *&^%$#@!\n")
    if b == "r":
        print("****** Razer *****")
        print("A) KEYCAP RAZAER PBT UPGRADE SET 1190฿")
        print("B) WRIST REST 1290฿")
        print("C) RAZER KRAKEN STORMTROOPER 3590฿")
        print("D) RAZER BASILISK V.2 2590฿")
        print("E) RAZER FIREFLY V.2 1990฿")
        b=input("สินค้าที่ต้องการเลือก: ")
        if b == "a":
            a.append("KEYCAP RAZAER PBT UPGRADE SET       1190฿            10%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 1071
        elif b == "b":
            a.append("WRIST REST                          1290฿            10%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 1161
        elif b == "c":
            a.append("RAZER KRAKEN STORMTROOPER           3590฿            10%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 3231
        elif b == "d":
            a.append("RAZER BASILISK V.2                  2590฿            10%")
            print("\n*  * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 2331
        elif b == "e":
            a.append("RAZER FIREFLY V.2                   1990฿            10%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 1791
        else: print("\n!@#$%^&* !!กรอกดีดี!! *&^%$#@!\n")
    if b== "k":
        print("*****NUBWO******")
        print("A) MOUSE  350฿")
        print("B) Microphone 250฿")
        print("C) Monitor 1500฿")
        b=input("สินค้าที่ต้องการเลือก: ")
        if b== "a":
            a.append("MOUSE                               300฿              0%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 300
        elif b== "b":
            a.append("Microphone                          250฿              0%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 250
        elif b== "c":
            a.append("Monitor                             1500฿             0%")
            print("\n* * * สินค้าไปที่ตระกร้าแล้ว * * *\n")
            num+= 1500
        else: print("\n!@#$%^&* !!กรอกดีดี!! *&^%$#@!\n")
    if b == "x": #เงื่อนไขสุดท้ายเมื่อลูกค้าขอดูบิล
        print("="*100) #ให้ปริ้นเครื่องหมาย = * 100
        print("              รุ่น                    ราคา             ส่วนลด  ") #สั่งปริ้นออกมาเพื่อนแสดงหัวใบบิล
        print("="*100)
        for list in a: #list คือตัวแปรรอรับค่าเฉยๆ ใช้ตัวอะไรก็ได้
            print(list) #แสดงค่า list หรือรายการที่สั่งซื้อที่เอาค่าไปเก็บไว้ที่ตัวแปล a
        print("รวมราคาสุทธิ")
        print(num)
        print("************thank you**********")
    if b == "t":
        print("Thank you for sub")
    if b== "o": #หากลูกค้ากด o ให้แสดงข้อความด้านล่าง
        print("*************thank you**********")
        print("*************GOOD LUCK***********")
        break
    
                        
                

