""" downcase_all.py """
from sys import argv


class Main():
    def __init__(txt):
        """ downcase_all.py """
        # ต้องมีพารามิเตอร์อย่างน้อย 1 ตัว
        if len(argv) >= 2:
            # แปลงทุกคำเป็นตัวพิมพ์เล็ก
            lst = [i.lower() for i in txt]
            # พิมพ์ทีละบรรทัด
            print(*lst, sep='\n')
        else:
            print('none')


# ดึง __init__ ออกมาใช้เป็นฟังก์ชันธรรมดา
downcase_it = Main.__init__

# ส่งพารามิเตอร์ทั้งหมดเข้าไป โดยตัดชื่อไฟล์ออก
downcase_it(argv[1:])
