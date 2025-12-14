import sys

def is_pair( n: int ) -> bool:
    if n%2 == 0:
        return True 
    else:
        return False

def main() -> None:
    while True:
        a: str = input( 'Entrer un nombre: ' )
        symbole: str = ''

        if '-' in a:
            a = a.replace( '-', '' )
            symbole = '-'
        elif '+' in a:
            a = a.replace( '+', '' )
            symbole = '+'

        n: str = a if symbole == '+' else f'-{ a }'
        
        if a.isdigit():
            if is_pair( int( a ) ):
                print( f'>> { n } est pair.' )
                break
            else:
                print( f'>> { n } est impair.' )
                break
        elif a.replace( ' ', '' ) == '':
            continue
        else:
            print( f'!> { n } n\'est pas un nombre. ' )
            continue



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Program arreter...' )
        sys.exit( 1 )
