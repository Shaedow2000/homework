import sys

def pgcd( a: int, b: int ) -> int:
    q: int = a % b
    while q != 0:
        a = b
        b = q
        q = a % b
    
    return b

def main() -> None:
    print( '[ Ctrl + C ] pour sortir...' )
    while True:
        a: str | int = input( '=> a: ' )
        b: str | int = input( '=> b: ' )

        if a.isdigit() and b.isdigit():
            a = int( a )
            b = int( b )
            print( f'--> Le PGCD est: pgcd( { a }; { b } ) = { pgcd( a, b ) }' )
            break
        else:
            print( '--> Entrer un nombre...' )
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Sotie du program...' )
        sys.exit( 1 )   
