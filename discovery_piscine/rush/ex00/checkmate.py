""" checkmate.py """
import numpy as np


def checkmate(board):
    """ checkmate.py """
    # ครอบทั้งฟังก์ชันด้วย try เพื่อไม่ให้โปรแกรมพังตามที่โจทย์กำหนด
    try:
        # ---------- ขั้นที่ 1: แปลงข้อความกระดานให้เป็นตาราง 2 มิติ ----------
        # ตัด \n ออก แล้วแตกข้อความเป็นตัวอักษรทีละตัว
        data = [i for i in board.replace('\n', '')]
        data = np.array(data)
        # เดาความกว้างของกระดานจากรากที่สองของจำนวนช่องทั้งหมด
        n = int(np.sqrt(len(data)))

        # ---------- ขั้นที่ 2: ตรวจว่ากระดานเป็นสี่เหลี่ยมจัตุรัสจริง ----------
        # ถ้าจำนวนช่องไม่เท่ากับ n*n แปลว่ากระดานไม่ใช่จัตุรัส
        if len(data) != n * n:
            print("Fail")
            return

        # จัดตัวอักษรทั้งหมดให้เป็นตาราง n แถว n หลัก
        data = data.reshape(n, n)

        # ---------- ขั้นที่ 3: หาตำแหน่ง King ----------
        # argwhere คืนพิกัด [แถว, หลัก] ของทุกช่องที่เป็น 'K'
        king_pos = np.argwhere(data == 'K')
        # โจทย์บอกว่ามี King ได้ตัวเดียว ถ้าไม่ใช่ถือว่ากระดานผิด
        if len(king_pos) != 1:
            print("Fail")
            return

        king_pos = king_pos[0]

        # ---------- ขั้นที่ 4: เตรียมแผนที่ช่องที่ถูกโจมตี ----------
        # ตารางขนาดเท่ากระดาน เริ่มต้นเป็น False ทุกช่อง
        # ถ้าหมากตัวไหนโจมตีถึงช่องใด จะเปลี่ยนช่องนั้นเป็น True
        attack_map = np.zeros((n, n), dtype=bool)

        # ---------- ขั้นที่ 5: ระยะโจมตีของ Pawn (P) ----------
        # เบี้ยกินทแยงขึ้นข้างหน้า 2 ช่อง (แถวบน ซ้ายหนึ่งและขวาหนึ่ง)
        all_p_pos = np.argwhere(data == 'P')
        for p_pos in all_p_pos:
            # ถ้าเบี้ยอยู่แถวบนสุดแล้ว ก็ไม่มีช่องให้โจมตีต่อ
            if p_pos[0] != 0:
                # กันไม่ให้ทะลุขอบซ้าย
                if p_pos[1] != 0:
                    #[บนก่อนแล้วไปซ้าย]
                    attack_map[p_pos[0]-1, p_pos[1]-1] = True
                # กันไม่ให้ทะลุขอบขวา
                if p_pos[1] != n-1:
                    #[บนก่อนแล้วไปขวา]
                    attack_map[p_pos[0]-1, p_pos[1]+1] = True

        # ---------- ขั้นที่ 6: ระยะโจมตีของ Rook (R) ----------
        # เรือยิงเป็นเส้นตรง 4 ทิศ จนกว่าจะชนขอบกระดานหรือชนหมากตัวอื่น
        all_r_pos = np.argwhere(data == 'R')
        for r_pos in all_r_pos:
            # i คือระยะห่างจากตัวเรือ เริ่มที่ 1 แล้วขยายออกไปเรื่อย ๆ
            i = 1
            # ตัวแปรสี่ตัวนี้บอกว่าแต่ละทิศยังเดินต่อได้อยู่ไหม
            up_con = True
            down_con = True
            lf_con = True
            rt_con = True

            # วนจนกว่าทุกทิศจะถูกปิดหมด
            while up_con or down_con or lf_con or rt_con:
                # ทิศขึ้น
                if up_con:
                    # ชนขอบบน หยุดโดยไม่ทำเครื่องหมาย
                    if r_pos[0]-i < 0:
                        up_con = False
                    # เจอหมากตัวอื่น กินได้ 1 ตัวแล้วหยุด
                    elif data[r_pos[0]-i, r_pos[1]] != '.':
                        attack_map[r_pos[0]-i, r_pos[1]] = True
                        up_con = False
                    # ช่องว่าง ทำเครื่องหมายแล้วเดินต่อ
                    else:
                        attack_map[r_pos[0]-i, r_pos[1]] = True

                # ทิศลง (ตรรกะเดียวกับทิศขึ้น)
                if down_con:
                    if r_pos[0]+i > n-1:
                        down_con = False
                    elif data[r_pos[0]+i, r_pos[1]] != '.':
                        attack_map[r_pos[0]+i, r_pos[1]] = True
                        down_con = False
                    else:
                        attack_map[r_pos[0]+i, r_pos[1]] = True

                # ทิศซ้าย
                if lf_con:
                    if r_pos[1]-i < 0:
                        lf_con = False
                    elif data[r_pos[0], r_pos[1]-i] != '.':
                        attack_map[r_pos[0], r_pos[1]-i] = True
                        lf_con = False
                    else:
                        attack_map[r_pos[0], r_pos[1]-i] = True

                # ทิศขวา
                if rt_con:
                    if r_pos[1]+i > n-1:
                        rt_con = False
                    elif data[r_pos[0], r_pos[1]+i] != '.':
                        attack_map[r_pos[0], r_pos[1]+i] = True
                        rt_con = False
                    else:
                        attack_map[r_pos[0], r_pos[1]+i] = True

                # ขยายระยะออกไปอีกหนึ่งช่อง
                i += 1

        # ---------- ขั้นที่ 7: ระยะโจมตีของ Bishop (B) ----------
        # โคนยิงทแยง 4 ทิศ หลักการหยุดเหมือนเรือทุกอย่าง ต่างแค่ทิศทาง
        all_b_pos = np.argwhere(data == 'B')
        for b_pos in all_b_pos:
            i = 1
            pp_con = True  # ทแยงลงขวา  (แถว+, หลัก+)
            nn_con = True  # ทแยงขึ้นซ้าย (แถว-, หลัก-)
            pn_con = True  # ทแยงลงซ้าย  (แถว+, หลัก-)
            np_con = True  # ทแยงขึ้นขวา (แถว-, หลัก+)

            while pp_con or nn_con or pn_con or np_con:
                # ทแยงลงขวา
                if pp_con:
                    if b_pos[0]+i > n-1 or b_pos[1]+i > n-1:
                        pp_con = False
                    elif data[b_pos[0]+i, b_pos[1]+i] != '.':
                        attack_map[b_pos[0]+i, b_pos[1]+i] = True
                        pp_con = False
                    else:
                        attack_map[b_pos[0]+i, b_pos[1]+i] = True

                # ทแยงขึ้นซ้าย
                if nn_con:
                    if b_pos[0]-i < 0 or b_pos[1]-i < 0:
                        nn_con = False
                    elif data[b_pos[0]-i, b_pos[1]-i] != '.':
                        attack_map[b_pos[0]-i, b_pos[1]-i] = True
                        nn_con = False
                    else:
                        attack_map[b_pos[0]-i, b_pos[1]-i] = True

                # ทแยงลงซ้าย
                if pn_con:
                    if b_pos[0]+i > n-1 or b_pos[1]-i < 0:
                        pn_con = False
                    elif data[b_pos[0]+i, b_pos[1]-i] != '.':
                        attack_map[b_pos[0]+i, b_pos[1]-i] = True
                        pn_con = False
                    else:
                        attack_map[b_pos[0]+i, b_pos[1]-i] = True

                # ทแยงขึ้นขวา
                if np_con:
                    if b_pos[0]-i < 0 or b_pos[1]+i > n-1:
                        np_con = False
                    elif data[b_pos[0]-i, b_pos[1]+i] != '.':
                        attack_map[b_pos[0]-i, b_pos[1]+i] = True
                        np_con = False
                    else:
                        attack_map[b_pos[0]-i, b_pos[1]+i] = True

                i += 1

        # ---------- ขั้นที่ 8: ระยะโจมตีของ Queen (Q) ----------
        # ควีน = เรือ + โคน จึงรันสองรอบ รอบแรกแนวตรง รอบสองแนวทแยง
        all_q_pos = np.argwhere(data == 'Q')
        for q_pos in all_q_pos:
            # --- รอบที่ 1: เดินแบบเรือ ---
            i = 1
            up_con = True
            down_con = True
            lf_con = True
            rt_con = True

            while up_con or down_con or lf_con or rt_con:
                # ทิศขึ้น
                if up_con:
                    if q_pos[0]-i < 0:
                        up_con = False
                    elif data[q_pos[0]-i, q_pos[1]] != '.':
                        attack_map[q_pos[0]-i, q_pos[1]] = True
                        up_con = False
                    else:
                        attack_map[q_pos[0]-i, q_pos[1]] = True

                # ทิศลง
                if down_con:
                    if q_pos[0]+i > n-1:
                        down_con = False
                    elif data[q_pos[0]+i, q_pos[1]] != '.':
                        attack_map[q_pos[0]+i, q_pos[1]] = True
                        down_con = False
                    else:
                        attack_map[q_pos[0]+i, q_pos[1]] = True

                # ทิศซ้าย
                if lf_con:
                    if q_pos[1]-i < 0:
                        lf_con = False
                    elif data[q_pos[0], q_pos[1]-i] != '.':
                        attack_map[q_pos[0], q_pos[1]-i] = True
                        lf_con = False
                    else:
                        attack_map[q_pos[0], q_pos[1]-i] = True

                # ทิศขวา
                if rt_con:
                    if q_pos[1]+i > n-1:
                        rt_con = False
                    elif data[q_pos[0], q_pos[1]+i] != '.':
                        attack_map[q_pos[0], q_pos[1]+i] = True
                        rt_con = False
                    else:
                        attack_map[q_pos[0], q_pos[1]+i] = True

                i += 1

            # --- รอบที่ 2: เดินแบบโคน ---
            i = 1
            pp_con = True
            nn_con = True
            pn_con = True
            np_con = True

            while pp_con or nn_con or pn_con or np_con:
                # ทแยงลงขวา
                if pp_con:
                    if q_pos[0]+i > n-1 or q_pos[1]+i > n-1:
                        pp_con = False
                    elif data[q_pos[0]+i, q_pos[1]+i] != '.':
                        attack_map[q_pos[0]+i, q_pos[1]+i] = True
                        pp_con = False
                    else:
                        attack_map[q_pos[0]+i, q_pos[1]+i] = True

                # ทแยงขึ้นซ้าย
                if nn_con:
                    if q_pos[0]-i < 0 or q_pos[1]-i < 0:
                        nn_con = False
                    elif data[q_pos[0]-i, q_pos[1]-i] != '.':
                        attack_map[q_pos[0]-i, q_pos[1]-i] = True
                        nn_con = False
                    else:
                        attack_map[q_pos[0]-i, q_pos[1]-i] = True

                # ทแยงลงซ้าย
                if pn_con:
                    if q_pos[0]+i > n-1 or q_pos[1]-i < 0:
                        pn_con = False
                    elif data[q_pos[0]+i, q_pos[1]-i] != '.':
                        attack_map[q_pos[0]+i, q_pos[1]-i] = True
                        pn_con = False
                    else:
                        attack_map[q_pos[0]+i, q_pos[1]-i] = True

                # ทแยงขึ้นขวา
                if np_con:
                    if q_pos[0]-i < 0 or q_pos[1]+i > n-1:
                        np_con = False
                    elif data[q_pos[0]-i, q_pos[1]+i] != '.':
                        attack_map[q_pos[0]-i, q_pos[1]+i] = True
                        np_con = False
                    else:
                        attack_map[q_pos[0]-i, q_pos[1]+i] = True

                i += 1

        # ---------- ขั้นที่ 9: สรุปผล ----------
        # ดูว่าช่องที่ King ยืนอยู่ ถูกทำเครื่องหมายว่าโดนโจมตีหรือเปล่า
        if attack_map[king_pos[0], king_pos[1]]:
            print("Success")
        else:
            print("Fail")

    # กระดานที่แปลงเป็นตารางไม่ได้ หรือพิกัดหลุดขอบ ให้ตอบ Fail แทนการพัง
    except (ValueError, IndexError):
        print("Fail")
