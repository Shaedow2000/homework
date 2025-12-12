import sys

def is_pair( n: int ) -> bool:
    if n%2 == 0:
        return True 
    else:
        return False

def main() -> None:
    while True:
        a: str = input( 'Entrer un nombre: ' )

        if a.isdigit():
            if is_pair( int( a ) ):
                print( f'>> { a } est pair.' )
                break
            else:
                print( f'>> { a } est impair.' )
                break
        elif a.replace( ' ', '' ) == '':
            continue
        else:
            print( f'!> { a } n\'est pas un nombre. ' )
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Program arreter...' )
        sys.exit( 1 )
