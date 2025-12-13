import sys
import os
from math import sqrt

class Equation:
    def linear( self, a: float, b: float ) -> int | float:
        return -( b / a )

    def quadratic( self, a: float, b: float, c: float ) -> list[ float ]:
        dp: float = ( -b + sqrt( ( b**2 ) - 4*a*c ) )
        dn: float = ( -b - sqrt( ( b**2 ) - 4*a*c ) )
        return  [ 
            ( dp / ( 2*a ) ),
            ( dn / ( 2*a ) )
        ]

def is_float( number: str ) -> bool:
    try:
        float( number )
        return True
    except ValueError:
        return False

def main() -> None:
    msg: str = '\t=> 1: Eqation linear | 2: Equation Quadratic | c: clear screen | q: quit\n'
    print( msg ) 

    equation: Equation = Equation()

    while True:
        choix: str | int = input( '--> Entrer votre choix: ' ).replace( ' ', '' ).lower()

        if not choix.isdigit() and ( choix == 'q' or choix == 'c' or choix == '' ):
            if choix == 'q':
                print( '\n--> Sortie du program...' )
                break
            elif choix == 'c':
                os.system( 'cls' if os.name == 'nt' else 'clear' )
                print( msg )
                continue
            else:
                continue
        elif choix == '1':
            print( '>> L\'equation linear: ax + b = 0' )
            a: str | float = input( '==> Entrer le nombre "a": ' )
            b: str | float = input( '==> Entrer le nombre "b": ' )

            if is_float( a ) and is_float( b ):
                a = float( a )
                b = float( b )
                x: float = equation.linear( a, b )

                print( f'>=> Solution: x = { x }\n' )
                continue
            else:
                print( 'Entrer des nombres...' )
                continue
        elif choix == '2':
            print( 'L\'equation Quadratic: ax^2 + bx + c = 0 ' )
            a: str | float = input( '==> Entrer le nombre "a": ' )
            b: str | float = input( '==> Entrer le nombre "b": ' )
            c: str | float = input( '==> Entrer le nombre "c": ' )

            if is_float( a ) and is_float( b ) and is_float( c ):
                a = float( a )
                b = float( b )
                c = float( c )
                solutions: list[ float ] = equation.quadratic( a, b, c )

                print( f'>=> Solutions: {{ x1 = { solutions[ 0 ] } | x2 = { solutions[ 1 ] } }}\n' )
                continue
            else:
                print( 'Entrer des nombres...' )
                continue
        else:
            print( 'Entrer l\'un des choix donne ( 1, 2, c ou q ) ' )
            continue

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n--> Sortie du program...' )
        sys.exit( 1 )
    
