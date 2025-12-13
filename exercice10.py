import sys 

def numbers( min: int, max: int ) -> list[ int ]:
    numbers: list[ int ] = []
    
    for i in range( max - min ):
        numbers.append( min + i + 1 )

    return numbers

def sum( numbers: list[ int ] ) -> float:
    sum: float = 0

    for i in range( numbers.__len__() ):
        sum += 1/numbers[ i ]

    return sum


def main() -> None:
    print( '[ Ctrl + C ] to exit...' )

    while True:
        min: int = 0
        max: str | int = input( '=> Entrer le nombre maximal: ' ).replace( ' ', '' )
        
        if max.isdigit():
            numbs: list[ int ] = numbers( int( min ), int( max ) )
            somme: float = sum( numbs )
            
            print( f'>=> La somme est: { somme }' )
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
