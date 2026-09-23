""" greetings_for_all.py """
from sys import argv


class Main():
    def __init__(*name):
        """ greetings_for_all.py """
        # ทำงานเฉพาะตอนรันไฟล์แบบไม่ใส่พารามิเตอร์
        if len(argv) == 1:
            # แปลง tuple ที่รับมาเป็นลิสต์
            name = list(name)
            if name == []:
                # เรียกมาแบบไม่ส่งชื่อ
                print('Hello, noble stranger.')
            elif isinstance(name[0], int):
                # ส่งตัวเลขมาแทนชื่อ
                print('Error! It was not a name.')
            else:
                print(f'Hello, {name[0]}.')
        else:
            print('none')


# ดึง __init__ ออกมาใช้เป็นฟังก์ชันธรรมดา
greetings = Main.__init__

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
