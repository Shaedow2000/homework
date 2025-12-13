import sys

def main() -> None:
    print( '[ Ctrl + C ] to quit.' )

    while True:
        x: str | int = input( '=> le nombre x: ' )
        n: str | int = input( '=> la puissance: ' )

        if x.isdigit() and n.isdigit():
            x = int( x )
            n = int( n )
            print( pow( x, n ) )
            break
        else:
            print( '-> Entrer un nombre...' )
            continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Sortie du program...' )
        sys.exit( 1 )
