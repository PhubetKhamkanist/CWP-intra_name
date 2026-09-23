""" aff_rev_params.py """
from sys import argv


def main():
    """ aff_rev_params.py """
    # ต้องมีพารามิเตอร์ตั้งแต่ 2 ตัวขึ้นไป (argv รวมชื่อไฟล์แล้วเป็น 3)
    if len(argv) > 2:
        # ตัดชื่อไฟล์ออก กลับลำดับ แล้วพิมพ์ทีละบรรทัด
        print(*argv[1:][::-1], sep='\n')
    else:
        print('none')


main()
