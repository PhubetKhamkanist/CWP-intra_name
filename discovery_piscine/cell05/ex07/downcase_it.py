""" downcase_it.py """
from sys import argv


def main():
    """ downcase_it.py """
    # รับพารามิเตอร์ได้ตัวเดียวเท่านั้น
    if len(argv) == 2:
        # แปลงเป็นตัวพิมพ์เล็กทั้งหมด
        print(argv[1].lower())
    else:
        print('none')


main()
