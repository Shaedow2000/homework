import sys

def reverse_num( n: int ) -> int:
    l: list[ str ] = list( str( n ) )
    l.reverse()
    num: str = ''.join( l )

    return int( num )

def main() -> None:
    print( '[ Ctrl + C ] to exit...' )

    while True:
        nombre: str | int = input( '=> Entrer un nombre: ' ).replace( ' ', '' )

        if nombre.isdigit():
            print( reverse_num( int( nombre ) ) )
            break
        else:
            print( '-> Entrer un nombre...\n' )
            continue

if __name__ == '__main__':
    try: 
        main()
    except KeyboardInterrupt:
        print( '\n--> Sortie...' )
        sys.exit( 1 )


