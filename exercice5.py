import sys

def sort( num1: int, num2: int, num3: int ) -> list[ int ]:
    nums: list[ int ] = [ num1, num2, num3 ]
    nums.sort()

    return nums

def main() -> None:
    while True:
        a: str | int = input( 'Entrer A: ' ).replace( ' ', '' )
        b: str | int = input( 'Entrer B: ' ).replace( ' ', '' )
        c: str | int = input( 'Entrer C: ' ).replace( ' ', '' )

        if a.isdigit() and b.isdigit() and c.isdigit():
            sorted: list[ int ] = sort( int( a ), int( b ), int( c ) )
            print( f'{ sorted[ 0 ]  } <= { sorted[ 1 ] } <= { sorted[ 2 ] }' )
            break
        else:
            print( 'Entrer des nombres entiers.\n' )
            continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Sortie du program...' )
        sys.exit( 1 )
