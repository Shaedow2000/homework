import sys

def numbers( min: int, max: int ) -> list[ int ]:
    numbers: list[ int ] = []
    
    for i in range( max - min ):
        numbers.append( min + i + 1 )

    return numbers

def sum( numbers: list[ int ] ) -> int:
    sum: int = 0

    for i in range( numbers.__len__() ):
        sum += numbers[ i ]

    return sum

def main() -> None:
    print( '[ Ctrl + C ] pour sortir...' )
    while True:
        min: str | int = input( '=> Entrer le nombre minimal: ' ).replace( ' ', '' )
        max: str | int = input( '=> Entrer le nombre maximal: ' ).replace( ' ', '' )
        
        if min.isdigit() and max.isdigit():
            numbs: list[ int ] = numbers( int( min ), int( max ) )
            somme: int = sum( numbs )
            
            print( f'>=> La somme est: { somme }' )
            break
        else:
            print( '-> Entrer un nombre...\n' )
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Sotie du program...' )
        sys.exit( 1 )
