def main():
    """ isneg.py """
    num = float(input())
    result = 'positive and negative'

    if num < 0:
        result = 'negative'
    elif num > 0:
        result = 'positive'
    else:
        result = 'This number is both positive and negative.zero'

    print(result)

main()