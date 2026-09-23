""" methods_everywhere.py """
from sys import argv


class Main1():
    def __init__(txt):
        """ shrink """
        # ตัดให้เหลือแค่ 8 ตัวแรก
        print(txt[:8])


class Main2():
    def __init__(txt):
        """ enlarge """
        # ขาดอีกกี่ตัวถึงจะครบ 8 (ถ้าเกินแล้วให้เป็น 0)
        num = max(8 - len(txt), 0)
        # เติม Z ต่อท้ายให้ครบ 8 ตัว
        print(txt + 'Z' * num)


# ดึง __init__ ออกมาใช้เป็นฟังก์ชันธรรมดา
shrink = Main1.__init__
enlarge = Main2.__init__

# ต้องมีพารามิเตอร์อย่างน้อย 1 ตัว
if len(argv) > 1:
    for txt in argv[1:]:
        # ยาวตั้งแต่ 8 ตัวให้ตัดทิ้ง สั้นกว่านั้นให้เติม
        if len(txt) >= 8:
            shrink(txt)
        else:
            enlarge(txt)
else:
    print('none')
