""" count_it.py """
from sys import argv


def main():
    """ count_it.py """
    # ต้องมีพารามิเตอร์อย่างน้อย 1 ตัว
    if len(argv) >= 2:
        # จำนวนพารามิเตอร์ (ไม่นับชื่อไฟล์)
        print('parameters:', len(argv) - 1)
        # วนพิมพ์แต่ละคำพร้อมความยาวของคำนั้น
        for txt in argv[1:]:
            print(f'{txt}: {len(txt)}')
    else:
        print('none')


main()
