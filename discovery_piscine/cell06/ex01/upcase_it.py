""" upcase_it.py """


class Main():
    def __init__(txt):
        """ upcase_it.py """
        # คืนค่าข้อความเป็นตัวพิมพ์ใหญ่ทั้งหมด
        return txt.upper()


# ดึง __init__ ออกมาใช้เป็นฟังก์ชันธรรมดา
upcase_it = Main.__init__

print(upcase_it('hello'))
