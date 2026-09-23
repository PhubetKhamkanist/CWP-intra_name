""" parameters.py """
import sys


def main():
    """ parameters.py """
    # argv[0] คือชื่อไฟล์ จึงลบออก 1 ให้เหลือเฉพาะพารามิเตอร์
    print(f'Number of parameters: {len(sys.argv) - 1}')


main()
