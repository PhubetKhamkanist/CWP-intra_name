""" show_attack.py - เครื่องมือช่วยดูภาพ ไม่ใช่ไฟล์ที่ต้องส่ง

วาดกระดานคู่กับแผนที่ช่องที่ถูกโจมตี แยกให้ดูทีละหมาก
เพื่อให้เห็นด้วยตาว่า ex00/checkmate.py ตัดสิน Success / Fail จากอะไร
กติกาที่ใช้ในไฟล์นี้ลอกมาจาก ex00/checkmate.py ทุกข้อ

วิธีใช้ (จากโฟลเดอร์ rush):
    python3 test/show_attack.py              # ใช้กระดานในตัวแปร BOARD ข้างล่าง
    python3 test/show_attack.py board.txt    # อ่านกระดานจากไฟล์
    python3 test/show_attack.py -            # วางกระดานเอง จบด้วย Ctrl+D
    python3 test/show_attack.py --demo       # ดูท่าเดินของหมากแต่ละตัว
"""
import sys
import numpy as np

# ---------- แก้กระดานตรงนี้ได้เลย ----------
BOARD = """\
R...
.K..
..P.
....\
"""

# ทิศทางการเดิน เก็บเป็นคู่ (แถว, หลัก)
STRAIGHT = [(-1, 0), (1, 0), (0, -1), (0, 1)]           # แนวตรง 4 ทิศ ของเรือ
DIAGONAL = [(1, 1), (-1, -1), (1, -1), (-1, 1)]         # แนวทแยง 4 ทิศ ของโคน
SLIDE = {'R': STRAIGHT, 'B': DIAGONAL, 'Q': STRAIGHT + DIAGONAL}
PIECES = 'PRBQ'


def parse(board):
    """แปลงข้อความเป็นตาราง n x n ถ้าไม่ใช่จัตุรัสคืน None"""
    rows = board.strip('\n').split('\n')
    n = len(rows)
    if n == 0 or any(len(row) != n for row in rows):
        return None
    return np.array([list(row) for row in rows])


def piece_attack(data, r, c):
    """แผนที่ช่องที่หมากตัวที่อยู่ (r, c) โจมตีได้ เฉพาะตัวนั้นตัวเดียว"""
    n = len(data)
    attack = np.zeros((n, n), dtype=bool)
    piece = data[r, c]

    # Pawn กินทแยงขึ้น 2 ช่อง
    if piece == 'P':
        if r != 0:                       # ไม่ได้อยู่แถวบนสุด
            if c != 0:                   # ไม่ทะลุขอบซ้าย
                attack[r-1, c-1] = True
            if c != n-1:                 # ไม่ทะลุขอบขวา
                attack[r-1, c+1] = True

    # หมากที่ยิงเป็นเส้น: เรือแนวตรง โคนแนวทแยง ควีนได้ทั้งสองแบบ
    for dr, dc in SLIDE.get(piece, []):
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

    return attack


def draw(data, attack, focus=None):
    """วาดกระดานเป็นบรรทัด ๆ
    X = ช่องว่างที่ถูกโจมตี, # = King ถูกโจมตี, * = หมากตัวอื่นที่โดนยิงถึง
    focus คือตำแหน่งหมากที่กำลังดูอยู่ หมากตัวอื่นที่ไม่เกี่ยวจะเป็นตัวพิมพ์เล็ก
    """
    n = len(data)
    lines = ['   ' + ' '.join(str(c % 10) for c in range(n))]
    for r in range(n):
        cells = []
        for c in range(n):
            ch = data[r, c]
            if ch == '.':
                ch = 'X' if attack[r, c] else '.'
            elif ch == 'K' and attack[r, c]:
                ch = '#'
            elif focus is not None and (r, c) != focus:
                ch = '*' if attack[r, c] else ch.lower()
            cells.append(ch)
        lines.append(f'{r % 10:>2} ' + ' '.join(cells))
    return lines


def side_by_side(blocks, gap=4):
    """พิมพ์หลายกระดานเรียงกันในแนวนอน blocks = [(หัวข้อ, บรรทัด), ...]"""
    width = max(len(line) for _, lines in blocks for line in lines)
    width = max(width, max(len(title) for title, _ in blocks))
    per_row = max(1, 80 // (width + gap))
    for start in range(0, len(blocks), per_row):
        chunk = blocks[start:start + per_row]
        print((' ' * gap).join(t.ljust(width) for t, _ in chunk).rstrip())
        for i in range(len(chunk[0][1])):
            print((' ' * gap).join(l[i].ljust(width) for _, l in chunk).rstrip())
        print()


def show(title, board):
    """พิมพ์กระดาน แผนที่รวม และแผนที่ของหมากแต่ละตัว"""
    print(f'\n===== {title} =====\n')
    data = parse(board)
    if data is None:
        print('  กระดานไม่ใช่สี่เหลี่ยมจัตุรัส -> Fail')
        return

    n = len(data)
    pieces = [(r, c) for r in range(n) for c in range(n) if data[r, c] in PIECES]
    total = np.zeros((n, n), dtype=bool)
    for r, c in pieces:
        total |= piece_attack(data, r, c)

    # กระดานจริง + แผนที่รวมของทุกหมาก
    side_by_side([('Board', draw(data, np.zeros((n, n), dtype=bool))),
                  ('All attacks', draw(data, total))])

    # แยกดูทีละตัว
    if pieces:
        print('แยกดูทีละตัว (ตัวพิมพ์เล็ก = หมากอื่น, * = หมากอื่นที่โดนยิงถึง)\n')
        side_by_side([(f'{data[r, c]} at ({r},{c})',
                       draw(data, piece_attack(data, r, c), focus=(r, c)))
                      for r, c in pieces])

    print('X = ช่องที่ถูกโจมตี   # = King ถูกโจมตี')
    king = np.argwhere(data == 'K')
    if len(king) != 1:
        print(f'มี King {len(king)} ตัว (ต้องมี 1 ตัว) -> Fail')
        return
    kr, kc = king[0]
    who = [f'{data[r, c]}({r},{c})' for r, c in pieces
           if piece_attack(data, r, c)[kr, kc]]
    if who:
        print(f'King ที่ ({kr},{kc}) ถูกโจมตีโดย {", ".join(who)} -> Success')
    else:
        print(f'King ที่ ({kr},{kc}) ปลอดภัย -> Fail')


def demo():
    """ท่าเดินของหมากแต่ละตัว วางกลางกระดาน 7x7 แบบโล่ง ๆ และแบบมีหมากขวาง"""
    empty = ['.......'] * 7
    for piece in PIECES:
        rows = [list(r) for r in empty]
        rows[3][3] = piece
        clear = np.array(rows)
        rows[1][1] = rows[1][3] = rows[3][5] = 'P'
        blocked = np.array(rows)
        print(f'\n===== {piece} =====\n')
        side_by_side([('open board', draw(clear, piece_attack(clear, 3, 3))),
                      ('with blockers', draw(blocked, piece_attack(blocked, 3, 3),
                                             focus=(3, 3)))])


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    if arg == '--demo':
        demo()
    elif arg == '-':
        show('stdin', sys.stdin.read())
    elif arg:
        with open(arg, encoding='utf-8') as f:
            show(arg, f.read())
    else:
        show('BOARD', BOARD)


if __name__ == '__main__':
    main()
