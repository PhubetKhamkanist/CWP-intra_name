""" play_with_arrays.py """


def main():
    """ play_with_arrays.py """
    # ลิสต์ตั้งต้นตามโจทย์
    lst = [2, 8, 9, 48, 8, 22, -12, 2]
    # บวก 2 ทุกตัว แล้วเก็บเฉพาะตัวที่ผลลัพธ์มากกว่า 5
    new_lst = [i + 2 for i in lst if i + 2 > 5]
    print(lst)
    # แปลงเป็น set เพื่อตัดค่าที่ซ้ำกันออก
    print(set(new_lst))


main()
