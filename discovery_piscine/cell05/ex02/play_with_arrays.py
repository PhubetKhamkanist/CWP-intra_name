""" play_with_arrays.py """
def main():
    """ play_with_arrays.py """
    lst = [2, 8, 9, 48, 8, 22, -12, 2]
    new_lst = [i+2 for i in lst if i+2 > 5]
    print(lst)
    print(new_lst)

main()
