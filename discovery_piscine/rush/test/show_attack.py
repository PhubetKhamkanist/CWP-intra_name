""" show_attack.py - เครื่องมือช่วยดูภาพ ไม่ใช่ไฟล์ที่ต้องส่ง

วาดกระดานคู่กับแผนที่ช่องที่ถูกโจมตี เพื่อให้เห็นด้วยตาว่า
ex00/checkmate.py ตัดสิน Success / Fail จากอะไร
กติกาที่ใช้ในไฟล์นี้ลอกมาจาก ex00/checkmate.py ทุกข้อ
"""
import numpy as np

# ทิศทางการเดิน เก็บเป็นคู่ (แถว, หลัก)
STRAIGHT = [(-1, 0), (1, 0), (0, -1), (0, 1)]           # แนวตรง 4 ทิศ ของเรือ
DIAGONAL = [(1, 1), (-1, -1), (1, -1), (-1, 1)]         # แนวทแยง 4 ทิศ ของโคน


def build_attack_map(board):
    """สร้างตาราง True/False ว่าช่องไหนถูกโจมตีบ้าง"""
    # ---------- ขั้นที่ 1: แปลงข้อความเป็นตาราง ----------
    data = np.array([i for i in board.replace('\n', '')])
    n = int(np.sqrt(len(data)))
    # ---------- ขั้นที่ 2: กระดานต้องเป็นจัตุรัส ----------
    if len(data) != n * n:
        return None, None, None
    data = data.reshape(n, n)

    # ---------- ขั้นที่ 3: ต้องมี King ตัวเดียว ----------
    king = np.argwhere(data == 'K')
    if len(king) != 1:
        return data, None, None
    king = king[0]

    # ---------- ขั้นที่ 4: เริ่มจากแผนที่เปล่า ----------
    attack = np.zeros((n, n), dtype=bool)

    # ---------- ขั้นที่ 5: Pawn กินทแยงขึ้น 2 ช่อง ----------
    for r, c in np.argwhere(data == 'P'):
        if r != 0:                       # ไม่ได้อยู่แถวบนสุด
            if c != 0:                   # ไม่ทะลุขอบซ้าย
                attack[r-1, c-1] = True
            if c != n-1:                 # ไม่ทะลุขอบขวา
                attack[r-1, c+1] = True

    # ---------- ขั้นที่ 6-8: หมากที่ยิงเป็นเส้น ----------
    # เรือเดินแนวตรง โคนเดินแนวทแยง ควีนเดินได้ทั้งสองแบบ
    for piece, dirs in (('R', STRAIGHT), ('B', DIAGONAL), ('Q', STRAIGHT + DIAGONAL)):
        for r, c in np.argwhere(data == piece):
            for dr, dc in dirs:
                i = 1
                while True:
                    rr, cc = r + dr*i, c + dc*i
                    # ชนขอบกระดาน หยุดโดยไม่ทำเครื่องหมาย
                    if rr < 0 or rr > n-1 or cc < 0 or cc > n-1:
                        break
                    attack[rr, cc] = True
                    # เจอหมากขวาง กินได้ตัวเดียวแล้วหยุด
                    if data[rr, cc] != '.':
                        break
                    i += 1

    return data, attack, king


def show(title, board):
    """พิมพ์กระดานคู่กับแผนที่การโจมตี"""
    print(f'\n{title}')
    data, attack, king = build_attack_map(board)

    if data is None:
        print('  กระดานไม่ใช่สี่เหลี่ยมจัตุรัส -> Fail')
        return
    if attack is None:
        print('  หา King ไม่เจอ หรือมีมากกว่าหนึ่งตัว -> Fail')
        return

    n = len(data)
    head = '    ' + ' '.join(str(c) for c in range(n))
    print(f'{head}        {head.strip()}')
    print(f'    {"-"*(2*n-1)}        {"-"*(2*n-1)}')

    for r in range(n):
        left = ' '.join(data[r])
        # ช่องว่างที่ถูกโจมตีแสดงเป็น X ช่องที่ปลอดภัยแสดงเป็น .
        # ช่องที่มีหมากยืนอยู่ยังแสดงตัวหมากไว้ให้เทียบตำแหน่งได้
        # ยกเว้น King ที่ถูกโจมตี จะแสดงเป็น # เพื่อให้เห็นชัด
        cells = []
        for c in range(n):
            if (r, c) == (king[0], king[1]):
                cells.append('#' if attack[r][c] else 'K')
            elif data[r][c] != '.':
                cells.append(data[r][c])
            else:
                cells.append('X' if attack[r][c] else '.')
        print(f'  {r}| {left}      {r}| {" ".join(cells)}')

    print('     กระดาน' + ' ' * (2*n - 3) + 'ช่องที่ถูกโจมตี')
    print('     X = ช่องว่างที่ถูกโจมตี   # = King ถูกโจมตี')

    kr, kc = king
    hit = attack[kr, kc]
    print(f'\n  King อยู่ช่อง (แถว {kr}, หลัก {kc}) : '
          f'{"ถูกโจมตี" if hit else "ปลอดภัย"} -> {"Success" if hit else "Fail"}')


if __name__ == '__main__':
    # ตัวอย่างที่ 1 - กระดานเดียวกับใน ex00/main.py
    show('ตัวอย่างที่ 1 : เบี้ยกินทแยงขึ้นมาโดน King', """\
R...
.K..
..P.
....\
""")

    # ตัวอย่างที่ 2 - เรือยิงไม่ถึงเพราะมีเบี้ยขวางอยู่
    show('ตัวอย่างที่ 2 : เรือถูกเบี้ยของตัวเองบังไว้', """\
RP.K
....
....
....\
""")

    # ตัวอย่างที่ 3 - กระดานใหญ่ขึ้น มีควีนกับโคน
    show('ตัวอย่างที่ 3 : ควีนกับโคนคุมกระดาน 5x5', """\
Q....
.....
..B..
.....
....K\
""")
