""" parameter_matching.py """
from sys import argv


def main():
    """ parameter_matching.py """
    # รับพารามิเตอร์ได้ตัวเดียวเท่านั้น
    if len(argv) == 2:
        # ให้ผู้ใช้ทายว่าพารามิเตอร์ที่ส่งมาคืออะไร
        txt = input('What was the parameter? ')
        # เทียบคำตอบกับพารามิเตอร์จริง
        if txt == argv[1]:
            print('Good job!')
        else:
            print('Nope, sorry...')
    else:
        print('none')


main()
