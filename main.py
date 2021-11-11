import persistencia_json as pj

lista_coches= []
while True:
    marca= input('marca coche:')
    if marca == 'fin':
        break
    modelo = input('modelo:')
    combustible= input('Combustible:')
    cilindrada= input('Cilindrada:')
    #CREAMOS UN DICCIONARIO
    linea= {}
    linea['Marca coche'] = marca
    linea['Modelo'] = modelo
    linea['Combustible'] = combustible
    linea['Cilindrada'] = cilindrada
    #AÑADIMOS DICCIONARIO A LA LISTA
    lista_coches.append(linea)

print('Lista de coche:\n',lista_coches)
pj.store(lista_coches,'coches.txt')
lista_coches=[]
print('\nlista:\n', lista_coches)
lista_coches = pj.retrieve('coches.txt')
print('\nlista:\n', lista_coches)