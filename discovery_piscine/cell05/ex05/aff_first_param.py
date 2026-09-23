""" aff_first_param.py """
from sys import argv


def main():
    """ aff_first_param.py """
    # argv นับชื่อไฟล์ด้วย ตั้งแต่ 2 ขึ้นไปแปลว่ามีพารามิเตอร์อย่างน้อย 1 ตัว
    if len(argv) >= 2:
        # พิมพ์พารามิเตอร์ตัวแรก
        print(argv[1])
    else:
        print('none')


main()
