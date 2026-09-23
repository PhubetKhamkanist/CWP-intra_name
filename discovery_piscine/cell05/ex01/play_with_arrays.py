""" play_with_arrays.py """


def main():
    """ play_with_arrays.py """
    # ลิสต์ตั้งต้นตามโจทย์
    lst = [2, 8, 9, 48, 8, 22, -12, 2]
    # สร้างลิสต์ใหม่โดยบวก 2 เข้าไปทุกตัว (ลิสต์เดิมไม่ถูกแก้)
    new_lst = [i + 2 for i in lst]
    print('Original array:', lst)
    print('New array:', new_lst)


main()
