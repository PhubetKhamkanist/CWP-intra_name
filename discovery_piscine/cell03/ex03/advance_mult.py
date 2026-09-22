def main():
    i = 0
    while i <= 10:
        x = 0
        print(f'Table de {i}:', end='')
        while x <= 10:
            print(f' {i*x}', end='')
            x += 1
        print()
        i += 1

main()
