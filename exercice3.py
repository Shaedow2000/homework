import sys

class Comparaison:
    def is_equal( self, number1: int, number2: int ):
        if number1 == number2:
            print( f'Le premier nombre ({ number1 }) est egale au dexieme nombre ({ number2 }).' )
        else:
            print( f'Le premier nombre ({ number1 }) n\'egale pas le dexieme nombre ({ number2 }).' )

    def is_greater( self, number1: int, number2: int ):
        if number1 > number2:
            print( f'Le premier nombre ({ number1 }) est plus grand que dexieme nombre ({ number2 }).' )
        elif number2 > number1:
            print( f'Le deuxieme nombre ({ number2 }) est plus grand que premier nombre ({ number1 }).' )
        else:
            self.is_equal( number1, number2 )

    def is_smaller( self, number1: int, number2: int ):
        if number1 < number2:
            print( f'Le premier nombre ({ number1 }) est plus petit que dexieme nombre ({ number2 }).' )
        elif number2 < number1:
            print( f'Le deuxieme nombre ({ number2 }) est plus petit que premier nombre ({ number1 }).' )
        else:
            print( 'bro' )
            self.is_equal( number1, number2 )


def main() -> None:
    print( '>>> Pour sortir du program [ Ctrl + C ]' )
    while True:
        a: str | int = input( '> Entrer un nombre: ' ).replace( ' ', '' )
        b: str | int = input( '> Entrer un autre nombre: ' ).replace( ' ', '' )
        print( '> Faire in comparaison de >  1: egalite | 2: qui est le plus grand | 3: qui est le plus petit.' )
        choix: str = input( '> Choisir ( 1 | 2 | 3 ): ' ).replace( ' ', '' )
        
        if not a.isdigit() and not b.isdigit() and ( choix != '1' or choix != '2' or choix != '3' ):
            print( '>> Entrer un nombre, et choisir comme choix ( 1, 2 ou 3 ).' )
            continue
        elif a == '' or b == '' or choix == '':
            print( '>> Entrer un nombre, et choisir comme choix ( 1, 2 ou 3 ).' )
            continue
        else:
            comparaison: Comparaison = Comparaison()
            a = int( a )
            b = int( b )

            if choix == '1':
                comparaison.is_equal( a, b )
                break
            elif choix == '2':
                comparaison.is_greater( a, b )
                break
            elif choix == '3':
                comparaison.is_smaller( a, b )
                break
            else:
                print( '>> Entre l\'un des choix donner ( 1, 2 ou 3 ).' )
                continue


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print( '\n-> Sortie du program.' )
        sys.exit( 1 )
