""" string_are_arrays.py """
from sys import argv


def main():
    """ string_are_arrays.py """
    # ต้องมีพารามิเตอร์ 1 ตัว และต้องมีตัว z อยู่ในนั้น
    if len(argv) == 2 and 'z' in argv[1]:
        # พิมพ์ z ออกมาเท่ากับจำนวน z ที่นับได้
        print('z' * argv[1].count('z'))
    else:
        print('none')


main()
