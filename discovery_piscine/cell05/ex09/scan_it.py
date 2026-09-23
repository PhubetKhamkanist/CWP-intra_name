""" scan_it.py """
from sys import argv


def main():
    """ scan_it.py """
    # ต้องมี 2 พารามิเตอร์: คำที่ค้นหา และข้อความที่ใช้ค้น
    if len(argv) == 3:
        # แยกข้อความด้วยช่องว่าง แล้วนับว่าเจอคำที่ค้นหากี่ครั้ง
        num = argv[2].split(' ').count(argv[1])
        if num > 0:
            print(num)
        else:
            print('none')
    else:
        print('none')


main()
