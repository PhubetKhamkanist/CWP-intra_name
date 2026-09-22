def main():
    num_1 = float(input('Enter the first number:\n'))
    num_2 = float(input('Enter the second number:\n'))
    result = 'positive and negative'

    num_mult = num_1 * num_2

    if num_mult < 0:
        result = 'negative'
    elif num_mult > 0:
        result = 'positive'

    print(f'{num_1} x {num_2} = {num_mult}')
    print(f'The result is {result}.')

main()
