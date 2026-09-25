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

# แต่ละเคส: (ชื่อเคส, กระดาน, ผลที่ควรได้)
CASES = {
    # ---------- 1. เทสกรณีการรุกตามปกติ ----------
    'normal': [
        ('โดนรุกจริง: Rook ยิงแนวนอนโดน King', "R..K\n....\n....\n....", 'Success'),
        ('ปลอดภัย: ไม่มีหมากตัวไหนยิงถึง King', "R...\n..K.\n....\n...B", 'Fail'),
        ('ปลอดภัย: มีแค่ King บนกระดาน', "....\n.K..\n....\n....", 'Fail'),
        ('ตัวอย่างใน main.py', "R...\n.K..\n..P.\n....", 'Success'),
    ],
    'blocked': [
        ('Rook ถูก P ขวาง', "RP.K\n....\n....\n....", 'Fail'),
        ('Rook ถูก B ขวาง (แนวตั้ง)', "K...\nB...\n....\nR...", 'Fail'),
        ('Bishop ถูก P ขวาง', "B...\n.P..\n..K.\n....", 'Fail'),
        ('Queen ถูก P ขวาง (แนวนอน)', "Q.PK\n....\n....\n....", 'Fail'),
        ('Queen ถูก P ขวาง (ทแยง)', "Q...\n.P..\n..K.\n....", 'Fail'),
        ('ตัวอักษรอื่นขวาง (X)', "R.XK\n....\n....\n....", 'Fail'),
        ('หมากขวางแต่ไม่ได้อยู่บนเส้น -> ยังโดน', "R..K\n.P..\n....\n....", 'Success'),
    ],

    # ---------- 2. เทสการเดินของหมากแต่ละประเภท ----------
    'pawn': [
        ('Pawn กินทแยงขึ้นซ้าย', "....\n.K..\n..P.\n....", 'Success'),
        ('Pawn กินทแยงขึ้นขวา', "....\n..K.\n.P..\n....", 'Success'),
        ('Pawn ไม่กินตรงขึ้นไป', "....\n.K..\n.P..\n....", 'Fail'),
        ('Pawn ไม่กินทแยงลง', "....\n..P.\n.K..\n....", 'Fail'),
        ('Pawn ไม่กินข้าง ๆ', "....\n.KP.\n....\n....", 'Fail'),
        ('Pawn กินได้แค่ 1 ช่อง (ห่าง 2 ไม่โดน)', "K...\n....\n..P.\n....", 'Fail'),
    ],
    'rook': [
        ('Rook ยิงขึ้น', "..K.\n....\n....\n..R.", 'Success'),
        ('Rook ยิงลง', "..R.\n....\n....\n..K.", 'Success'),
        ('Rook ยิงซ้าย', "....\nK..R\n....\n....", 'Success'),
        ('Rook ยิงขวา', "....\nR..K\n....\n....", 'Success'),
        ('Rook ไม่ยิงทแยง', "R...\n.K..\n....\n....", 'Fail'),
    ],
    'bishop': [
        ('Bishop ทแยงลงขวา', "B...\n....\n....\n...K", 'Success'),
        ('Bishop ทแยงขึ้นซ้าย', "K...\n....\n....\n...B", 'Success'),
        ('Bishop ทแยงลงซ้าย', "...B\n....\n....\nK...", 'Success'),
        ('Bishop ทแยงขึ้นขวา', "...K\n....\n....\nB...", 'Success'),
        ('Bishop ไม่ยิงแนวตรง', "B..K\n....\n....\n....", 'Fail'),
    ],
    'queen': [
        ('Queen แนวตั้ง', "Q...\n....\n....\nK...", 'Success'),
        ('Queen แนวนอน', "....\n....\nK..Q\n....", 'Success'),
        ('Queen ทแยง', "...Q\n....\n.K..\n....", 'Success'),
        ('Queen ไม่ยิงแบบม้า (L)', "Q...\n..K.\n....\n....", 'Fail'),
    ],

    # ---------- 3. เทสการจัดการข้อผิดพลาด ----------
    'shape': [
        ('กระดาน 3x4 (3 แถว 4 หลัก)', "R..K\n....\n....", 'Fail'),
        ('กระดาน 4x5', "R...K\n.....\n.....\n.....", 'Fail'),
        ('แต่ละแถวยาวไม่เท่ากัน (3+4+4+5 = 16 ช่อง)', "R..\nK...\n....\n.....", 'Fail'),
        ('กระดาน 2x8 (รวมได้ 16 ช่อง เท่ากับ 4x4)', "R..K....\n........", 'Fail'),
        ('กระดานว่าง', "", 'Fail'),
        ('กระดาน 1x1 มีแค่ K', "K", 'Fail'),
    ],
    'king': [
        ('ไม่มี King เลย', "R...\n....\n....\n....", 'Fail'),
        ('มี King 2 ตัว', "R..K\n....\n....\n...K", 'Fail'),
        ('มี King 3 ตัว', "K.K.\n....\nK...\nQ...", 'Fail'),
    ],
    'corner': [
        ('King มุมซ้ายบน โดน Queen มุมขวาล่าง', "K...\n....\n....\n...Q", 'Success'),
        ('King มุมขวาบน โดน Pawn', "...K\n..P.\n....\n....", 'Success'),
        ('Pawn แถวบนสุด (ไม่มีช่องให้กิน)', "P..K\n....\n....\n....", 'Fail'),
        ('Pawn ชิดขอบซ้าย', "....\n....\nK...\nP...", 'Fail'),
        ('Pawn ชิดขอบขวา', "....\n....\n..K.\n...P", 'Success'),
        ('Rook มุมขวาล่าง ยิงถึงมุมขวาบน', "...K\n....\n....\n...R", 'Success'),
        ('Bishop มุม ไม่โดน King ที่ขอบ', "B...\n....\n....\n..K.", 'Fail'),
        ('กระดาน 1x1', "K", 'Fail'),
        ('กระดาน 2x2 Pawn กินมุม', "K.\n.P", 'Success'),
        ('กระดานใหญ่ 8x8', "K.......\n........\n........\n........\n"
                          "........\n........\n........\n.......B", 'Success'),
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
        for title, board, expected in CASES[group]:
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
