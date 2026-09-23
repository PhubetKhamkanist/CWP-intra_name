""" free_range.py """
from sys import argv


def main():
    """ free_range.py """
    # ต้องมี 2 พารามิเตอร์: เลขเริ่มต้นและเลขสิ้นสุด
    if len(argv) == 3:
        start = int(argv[1])
        end = int(argv[2])
        if start > end:
            # เริ่มมากกว่าจบ ให้สร้างช่วงจากน้อยไปมากแล้วกลับลำดับ
            print(list(range(end, start + 1))[::-1])
        else:
            # +1 เพราะ range ไม่รวมตัวสุดท้าย
            print(list(range(start, end + 1)))
    else:
        print('none')


main()
