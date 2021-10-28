

def run():
    LIMITE = 1000  #el resultado no podra superar este valor 
    contador_rama=0
    contador = 0 
    potencia_2 = 2**contador
    
    while potencia_2 < LIMITE:
        contador = contador + 1 
        potencia_2 = 2**contador
    
        print ('2 elevado a ' + str(contador) + ' ea igual a -> ' + str(potencia_2))
    
    
    
    
if __name__ == "__main__":
        run()
    