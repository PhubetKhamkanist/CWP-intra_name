""" test_checkmate.py - ชุดเทสสำหรับ ex00/checkmate.py

วิธีรัน (จากโฟลเดอร์ rush):
    python3 test/test_checkmate.py            # รันทุกกลุ่ม
    python3 test/test_checkmate.py pawn       # รันเฉพาะกลุ่ม
    python3 test/test_checkmate.py --list     # ดูชื่อกลุ่มทั้งหมด
"""
import io
import os
import sys
from contextlib import redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'ex00'))
from checkmate import checkmate  # noqa: E402

# แต่ละเคส: (ชื่อเคส, ผลที่ควรได้, กระดาน)
# กระดานเขียนแบบเดียวกับ main.py: ขึ้นต้น """\ และปิดท้ายแถวสุดท้ายด้วย \
CASES = {
    # ---------- 1. เทสกรณีการรุกตามปกติ ----------
    'normal': [
        ('โดนรุกจริง: Rook ยิงแนวนอนโดน King', 'Success', """\
R..K
....
....
....\
"""),
        ('ปลอดภัย: ไม่มีหมากตัวไหนยิงถึง King', 'Fail', """\
R...
..K.
....
...B\
"""),
        ('ปลอดภัย: มีแค่ King บนกระดาน', 'Fail', """\
....
.K..
....
....\
"""),
        ('ตัวอย่างใน main.py', 'Success', """\
R...
.K..
..P.
....\
"""),
    ],
    'blocked': [
        ('Rook ถูก P ขวาง', 'Fail', """\
RP.K
....
....
....\
"""),
        ('Rook ถูก B ขวาง (แนวตั้ง)', 'Fail', """\
K...
B...
....
R...\
"""),
        ('Bishop ถูก P ขวาง', 'Fail', """\
B...
.P..
..K.
....\
"""),
        ('Queen ถูก P ขวาง (แนวนอน)', 'Fail', """\
Q.PK
....
....
....\
"""),
        ('Queen ถูก P ขวาง (ทแยง)', 'Fail', """\
Q...
.P..
..K.
....\
"""),
        ('ตัวอักษรอื่นขวาง (X)', 'Fail', """\
R.XK
....
....
....\
"""),
        ('หมากขวางแต่ไม่ได้อยู่บนเส้น -> ยังโดน', 'Success', """\
R..K
.P..
....
....\
"""),
    ],

    # ---------- 2. เทสการเดินของหมากแต่ละประเภท ----------
    'pawn': [
        ('Pawn กินทแยงขึ้นซ้าย', 'Success', """\
....
.K..
..P.
....\
"""),
        ('Pawn กินทแยงขึ้นขวา', 'Success', """\
....
..K.
.P..
....\
"""),
        ('Pawn ไม่กินตรงขึ้นไป', 'Fail', """\
....
.K..
.P..
....\
"""),
        ('Pawn ไม่กินทแยงลง', 'Fail', """\
....
..P.
.K..
....\
"""),
        ('Pawn ไม่กินข้าง ๆ', 'Fail', """\
....
.KP.
....
....\
"""),
        ('Pawn กินได้แค่ 1 ช่อง (ห่าง 2 ไม่โดน)', 'Fail', """\
K...
....
..P.
....\
"""),
    ],
    'rook': [
        ('Rook ยิงขึ้น', 'Success', """\
..K.
....
....
..R.\
"""),
        ('Rook ยิงลง', 'Success', """\
..R.
....
....
..K.\
"""),
        ('Rook ยิงซ้าย', 'Success', """\
....
K..R
....
....\
"""),
        ('Rook ยิงขวา', 'Success', """\
....
R..K
....
....\
"""),
        ('Rook ไม่ยิงทแยง', 'Fail', """\
R...
.K..
....
....\
"""),
    ],
    'bishop': [
        ('Bishop ทแยงลงขวา', 'Success', """\
B...
....
....
...K\
"""),
        ('Bishop ทแยงขึ้นซ้าย', 'Success', """\
K...
....
....
...B\
"""),
        ('Bishop ทแยงลงซ้าย', 'Success', """\
...B
....
....
K...\
"""),
        ('Bishop ทแยงขึ้นขวา', 'Success', """\
...K
....
....
B...\
"""),
        ('Bishop ไม่ยิงแนวตรง', 'Fail', """\
B..K
....
....
....\
"""),
    ],
    'queen': [
        ('Queen แนวตั้ง', 'Success', """\
Q...
....
....
K...\
"""),
        ('Queen แนวนอน', 'Success', """\
....
....
K..Q
....\
"""),
        ('Queen ทแยง', 'Success', """\
...Q
....
.K..
....\
"""),
        ('Queen ไม่ยิงแบบม้า (L)', 'Fail', """\
Q...
..K.
....
....\
"""),
    ],

    # ---------- 3. เทสการจัดการข้อผิดพลาด ----------
    'shape': [
        ('กระดาน 3x4 (3 แถว 4 หลัก)', 'Fail', """\
R..K
....
....\
"""),
        ('กระดาน 4x5', 'Fail', """\
R...K
.....
.....
.....\
"""),
        ('แต่ละแถวยาวไม่เท่ากัน (3+4+4+5 = 16 ช่อง)', 'Fail', """\
R..
K...
....
.....\
"""),
        ('กระดาน 2x8 (รวมได้ 16 ช่อง เท่ากับ 4x4)', 'Fail', """\
R..K....
........\
"""),
        ('กระดานว่าง', 'Fail', ""),
        ('กระดาน 1x1 มีแค่ K', 'Fail', """\
K\
"""),
    ],
    'king': [
        ('ไม่มี King เลย', 'Fail', """\
R...
....
....
....\
"""),
        ('มี King 2 ตัว', 'Fail', """\
R..K
....
....
...K\
"""),
        ('มี King 3 ตัว', 'Fail', """\
K.K.
....
K...
Q...\
"""),
    ],
    'corner': [
        ('King มุมซ้ายบน โดน Queen มุมขวาล่าง', 'Success', """\
K...
....
....
...Q\
"""),
        ('King มุมขวาบน โดน Pawn', 'Success', """\
...K
..P.
....
....\
"""),
        ('Pawn แถวบนสุด (ไม่มีช่องให้กิน)', 'Fail', """\
P..K
....
....
....\
"""),
        ('Pawn ชิดขอบซ้าย', 'Fail', """\
....
....
K...
P...\
"""),
        ('Pawn ชิดขอบขวา', 'Success', """\
....
....
..K.
...P\
"""),
        ('Rook มุมขวาล่าง ยิงถึงมุมขวาบน', 'Success', """\
...K
....
....
...R\
"""),
        ('Bishop มุม ไม่โดน King ที่ขอบ', 'Fail', """\
B...
....
....
..K.\
"""),
        ('กระดาน 1x1', 'Fail', """\
K\
"""),
        ('กระดาน 2x2 Pawn กินมุม', 'Success', """\
K.
.P\
"""),
        ('กระดานใหญ่ 8x8', 'Success', """\
K.......
........
........
........
........
........
........
.......B\
"""),
    ],
}


def run(board):
    """เรียก checkmate แล้วดักข้อความที่พิมพ์ออกมา ถ้าพังให้คืนชื่อ Error"""
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            checkmate(board)
    except Exception as e:  # pylint: disable=broad-except
        return f'CRASH ({type(e).__name__}: {e})'
    return buf.getvalue().strip()


def main():
    args = sys.argv[1:]
    if args and args[0] == '--list':
        for name, cases in CASES.items():
            print(f'{name:8} ({len(cases)} เคส)')
        return 0

    groups = args or list(CASES)
    unknown = [g for g in groups if g not in CASES]
    if unknown:
        print(f'ไม่รู้จักกลุ่ม: {", ".join(unknown)}  (ดูด้วย --list)')
        return 2

    passed = total = 0
    for group in groups:
        print(f'\n===== {group} =====')
        for title, expected, board in CASES[group]:
            got = run(board)
            ok = got == expected
            passed += ok
            total += 1
            print(f'  [{"OK" if ok else "KO"}] {title}: '
                  f'ได้ {got}' + ('' if ok else f'  (ควรได้ {expected})'))
            if not ok:
                for line in board.split('\n'):
                    print(f'        {line}')

    print(f'\nผ่าน {passed}/{total}')
    return 0 if passed == total else 1


if __name__ == '__main__':
    sys.exit(main())
