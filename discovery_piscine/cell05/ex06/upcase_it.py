""" upcase_it.py """
from sys import argv


def main():
    """ upcase_it.py """
    # รับพารามิเตอร์ได้ตัวเดียวเท่านั้น
    if len(argv) == 2:
        # แปลงเป็นตัวพิมพ์ใหญ่ทั้งหมด
        print(argv[1].upper())
    else:
        print('none')


main()
