a: int = int( input( 'Entrer un nombre: ' ) )

def is_pair( n: int ) -> bool:
    if a%2 == 0:
        return True 
    else:
        return False

print( f'{ a } est pair.' if is_pair( a ) else f'{ a } est impair.' )
