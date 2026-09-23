""" append_it.py """
from sys import argv


def main():
    """ append_it.py """
    # ต้องมีพารามิเตอร์อย่างน้อย 1 ตัว
    if len(argv) >= 2:
        for txt in argv[1:]:
            # ข้ามคำที่ลงท้ายด้วย ism อยู่แล้ว
            if not txt.endswith('ism'):
                # ตัด e ท้ายคำออกก่อน แล้วต่อท้ายด้วย ism
                print(txt.rstrip('e') + 'ism')
    else:
        print('none')


main()
