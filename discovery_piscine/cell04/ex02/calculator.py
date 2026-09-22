def main():
    """ calculator.py """
    try:
        num_1 = int(input('Give me the first number: '))
        num_2 = int(input('Give me the second number: '))
        
        operator = ['+', '-', '/', '*']
        
        print('Thank you!')
        for i in range(4):
            ans = f'{num_1} {operator[i]} {num_2}'
            print(f'{num_1} {operator[i]} {num_2} = {int(eval(ans))}')
    except ZeroDivisionError:
        print('Zero Division Error')
        ans = f'{num_1} {operator[3]} {num_2}'
        print(f'{num_1} {operator[3]} {num_2} = {int(eval(ans))}')
    except:
        print('Mai Aow STR!!!')
main()
