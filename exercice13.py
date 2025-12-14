import sys

def Fibonacci( n: int ) -> int:
    a: int = 0
    b: int = 1 

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range( 1, n ):
            c = a + b
            a = b
            b = c

        return b

def main() -> None:
    print( '[ Ctrl + C ] to exit...' )

    while True:
        n: str | int = input( '-> Entrer le nombre de sequence Fibonacci: ' ).replace( ' ', '' )
        
        if n.isdigit():
            print( f'==> Le nombre { n } de la sequence de Fibonacci est: { Fibonacci( int( n ) ) }.\n' )
            break
        else:
            print( '--> Entrer un nombre entier positif...\n' )
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Sortie du program...' )
        sys.exit( 1 )
