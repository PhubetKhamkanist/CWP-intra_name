""" scope_that.py """
from sys import argv


class Main():
    def __init__(num):
        """ add_one """
        # คืนค่าที่บวกหนึ่งแล้ว โดยไม่แก้ตัวแปรเดิม
        return num + 1


# ดึง __init__ ออกมาใช้เป็นฟังก์ชันธรรมดา
add_one = Main.__init__

# ทำงานเฉพาะตอนรันไฟล์แบบไม่ใส่พารามิเตอร์
if len(argv) == 1:
    numed = 5
    result = add_one(numed)
    # ค่าเดิมไม่เปลี่ยน เพราะ int ถูกส่งเข้าฟังก์ชันแบบคัดลอกค่า
    print(numed)
    # ค่าใหม่ที่ฟังก์ชันคืนกลับมา
    print(result)
else:
    print('none')
