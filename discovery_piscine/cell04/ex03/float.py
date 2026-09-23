def main():

    num = input('Give me a number: ')
    float(num)             
    num = num.split('.')
    if len(num) == 1 or int(num[1]) == 0:
       print('This number is an integer.')
    else:
        print('This number is a decimal.')

main()
