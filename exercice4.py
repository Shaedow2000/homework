import sys

def greatest_number( num1: int, num2: int, num3: int ) -> int:
    return max([ num1, num2, num3 ])

def main() -> None:
    while True:
        a: str | int = input( '> nombre A: ' ).replace( ' ', '' )
        b: str | int = input( '> nombre B: ' ).replace( ' ', '' )
        c: str | int = input( '> nombre C: ' ).replace( ' ', '' )

        if a.isdigit() and b.isdigit() and c.isdigit():
            a = int( a )
            b = int( b )
            c = int( c )
            g: int = greatest_number( a, b, c )

            print( f'Le plus grand nombre est le nombre: { 'A' if g == a else 'B' if g == b else 'C' } = { g }' )
            break
        else:
            print( f'Entrer des nombres entiers.' )
            continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Sortie du program...' )
        sys.exit( 1 )
