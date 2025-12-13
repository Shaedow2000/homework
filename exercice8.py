import sys

def numbers( min: int, max: int ) -> list[ int ]:
    numbers: list[ int ] = []
    
    for i in range( max - min ):
        numbers.append( min + i + 1 )

    return numbers

def is_pair( n: int ) -> bool:
    return n%2 == 0

def pair_numbers( numbers: list[ int ] ) -> list[ int ]:
    pair: list[ int ] = []

    for i in range( len( numbers ) ):
        if is_pair( numbers[ i ] ):
            pair.append( numbers[ i ] )
        else:
            continue

    return pair

def is_number( n: str ) -> bool:
    n = n.replace( ' ', '' )

    if n[ 0 ] in [ '+', '-' ]:
        if n[ 1: ].isdigit():
            return True
        else:
            return False
    else:
        if n.isdigit():
            return True
        else:
            return False

def sum( numbers: list[ int ] ) -> int:
    sum: int = 0

    for i in range( numbers.__len__() ):
        sum += abs( numbers[ i ] )

    return sum


def main() -> None:
    print( '[ Ctrl + C ] to exit.' )
    
    while True:
        min: str | int = input( '=> Entrer le nombre minimal: ' )
        max: str | int = input( '=> Entrer le nombre maximal: ' )
        
        if is_number( min ) and is_number( max ):
            numbs: list[ int ] = numbers( int( min ), int( max ) )
            pairs_n: list[ int ] = pair_numbers( numbs )
            somme: int = sum( pairs_n )

            print( somme )
            break
        else:
            print( '>-> Entrer un nombre...' )
            continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Sortie du program...' )
        sys.exit( 1 )
