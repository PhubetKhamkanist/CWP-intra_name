# Rush 01 - Checkmate

`ex00/checkmate.py` รับกระดานหมากรุกเป็นข้อความ แล้วพิมพ์ `Success` ถ้า King ถูกรุก หรือ `Fail` ถ้าไม่ถูกรุก / กระดานผิดรูป

| หมาก | การโจมตี |
|---|---|
| `P` Pawn | ทแยงขึ้น 1 ช่อง (ซ้ายบน, ขวาบน) |
| `R` Rook | แนวตรง 4 ทิศ จนชนขอบหรือชนหมาก |
| `B` Bishop | แนวทแยง 4 ทิศ จนชนขอบหรือชนหมาก |
| `Q` Queen | Rook + Bishop |
| `K` King | ต้องมี 1 ตัวพอดี |
| `.` หรือตัวอื่น | `.` คือช่องว่าง ตัวอักษรอื่นถือเป็นสิ่งกีดขวาง |

## โครงสร้างโฟลเดอร์

```
rush/
├── ex00/
│   ├── checkmate.py      # ไฟล์ที่ส่ง
│   └── main.py           # ไฟล์ที่ผู้ตรวจจะแก้กระดานเพื่อทดสอบ
└── test/
    ├── test_checkmate.py # ชุดเทสอัตโนมัติ (50 เคส)
    └── show_attack.py    # วาดแผนที่ช่องที่ถูกโจมตีให้ดูด้วยตา
```

ต้องมี `numpy`: `pip3 install numpy`

## รันโปรแกรม

```bash
cd ex00
python3 main.py
```

## รันเทสอัตโนมัติ

รันจากโฟลเดอร์ `rush`

```bash
python3 test/test_checkmate.py            # รันทุกกลุ่ม
python3 test/test_checkmate.py --list     # ดูชื่อกลุ่มทั้งหมด
python3 test/test_checkmate.py pawn rook  # รันหลายกลุ่มพร้อมกัน
```

แต่ละบรรทัดจะขึ้น `[OK]` หรือ `[KO]` ถ้า KO จะพิมพ์กระดานของเคสนั้นให้ดูด้วย บรรทัดสุดท้ายสรุปว่าผ่านกี่เคส

### 1. การรุกตามปกติ

| คำสั่ง | สิ่งที่ทดสอบ |
|---|---|
| `python3 test/test_checkmate.py normal` | โดนรุกจริง (Success) / ปลอดภัย (Fail) |
| `python3 test/test_checkmate.py blocked` | มีหมากหรือตัวอักษรอื่นขวางเส้นทางของ R, B, Q (Fail) |

### 2. การเดินของหมากแต่ละประเภท

| คำสั่ง | สิ่งที่ทดสอบ |
|---|---|
| `python3 test/test_checkmate.py pawn` | กินทแยงขึ้นซ้าย/ขวา, ไม่กินตรง, ไม่กินถอยหลัง, ไม่กินข้าง |
| `python3 test/test_checkmate.py rook` | ยิงขึ้น/ลง/ซ้าย/ขวา, ไม่ยิงทแยง |
| `python3 test/test_checkmate.py bishop` | ยิงทแยงครบ 4 ทิศ, ไม่ยิงแนวตรง |
| `python3 test/test_checkmate.py queen` | ยิงทั้งแนวตรงและทแยง, ไม่ยิงแบบม้า |

### 3. การจัดการข้อผิดพลาด / Edge cases

| คำสั่ง | สิ่งที่ทดสอบ |
|---|---|
| `python3 test/test_checkmate.py shape` | กระดาน 3x4, 4x5, แถวยาวไม่เท่ากัน, 2x8, กระดานว่าง, 1x1 |
| `python3 test/test_checkmate.py king` | ไม่มี King, มี King 2 ตัว, 3 ตัว |
| `python3 test/test_checkmate.py corner` | หมาก/King อยู่ขอบหรือมุมกระดาน ต้องไม่ index หลุดขอบ |

ทุกเคสต้องได้ `Success` หรือ `Fail` เท่านั้น ถ้าโปรแกรมพัง ชุดเทสจะแสดง `CRASH (...)`

## ดูแผนที่การโจมตีด้วยตา

`test/show_attack.py` วาดกระดานคู่กับช่องที่ถูกโจมตี ทั้งแบบรวมทุกหมาก และแยกดูทีละตัว

```bash
python3 test/show_attack.py              # ใช้กระดานในตัวแปร BOARD บนสุดของไฟล์ (แก้ได้)
python3 test/show_attack.py board.txt    # อ่านกระดานจากไฟล์
python3 test/show_attack.py -            # วางกระดานเองใน terminal แล้วกด Ctrl+D
python3 test/show_attack.py --demo       # ดูท่าเดินของ P, R, B, Q บนกระดานโล่ง และแบบมีหมากขวาง
```

ตัวอย่างผลลัพธ์:

```
Board          All attacks
   0 1 2 3        0 1 2 3
 0 R . . .      0 R X X X
 1 . K . .      1 X # . X
 2 . . P .      2 X . P .
 3 . . . .      3 X . . .

แยกดูทีละตัว (ตัวพิมพ์เล็ก = หมากอื่น, * = หมากอื่นที่โดนยิงถึง)

R at (0,0)    P at (2,2)
   0 1 2 3       0 1 2 3
 0 R X X X     0 r . . .
 1 X k . .     1 . # . X
 2 X . p .     2 . . P .
 3 X . . .     3 . . . .

X = ช่องที่ถูกโจมตี   # = King ถูกโจมตี
King ที่ (1,1) ถูกโจมตีโดย P(2,2) -> Success
```

| สัญลักษณ์ | ความหมาย |
|---|---|
| `X` | ช่องว่างที่ถูกโจมตี |
| `#` | King ถูกโจมตี |
| `*` | หมากตัวอื่นที่ถูกยิงถึง (เส้นทางหยุดตรงนี้) |
| ตัวพิมพ์เล็ก | หมากตัวอื่นที่ไม่ได้กำลังดูอยู่ |

## เทสด้วยมือตอน Defense

ผู้ตรวจจะแก้ตัวแปร `board` ใน `ex00/main.py` แล้วรัน `python3 main.py` กระดานตัวอย่างสำหรับแต่ละกรณี:

```python
# Success - Pawn กินทแยงขึ้น
board = """\
R...
.K..
..P.
....\
"""

# Fail - Rook ถูก Pawn ขวาง
board = """\
RP.K
....
....
....\
"""

# Success - Bishop ทแยงมุมถึงมุม
board = """\
B...
....
....
...K\
"""

# Success - Queen แนวตั้ง
board = """\
Q...
....
....
K...\
"""

# Fail - กระดานไม่ใช่จัตุรัส (3x4)
board = """\
R..K
....
....\
"""

# Fail - ไม่มี King
board = """\
R...
....
....
....\
"""

# Fail - King 2 ตัว
board = """\
R..K
....
....
...K\
"""
```
