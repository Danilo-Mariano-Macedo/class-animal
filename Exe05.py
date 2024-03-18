# Crie uma classe base chamada "Animal" com um método " emitirSom". Em seguida, crie classes derivadas como 
# "Cachorro, " "Gato " e "Pássaro " que herdem de "Animal" e sobrescrevam o método " emitirSom " para cada 
# tipo de animal. Crie uma lista de animais e percorra-a, chamando o método " emitirSom " para cada animal.
# Demonstre como o polimorfismo permite que diferentes tipos de animais emitam seus sons de maneira uniforme.

class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return 'Auau'

class Gato(Animal):
    def emitir_som(self):
        return 'Miau'

class Passaro(Animal):
    def emitir_som(self):
        return 'Piupiu'

Malvadeza = Cachorro()
Bolofofo = Gato()
Canario = Passaro()    
    
print('Malvadeza faz', Malvadeza.emitir_som())
print('Bolofofo faz', Bolofofo.emitir_som())
print('Canario faz', Canario.emitir_som())
