# El ciclo for ejecuta un bloque de codigo repetidamente hasta
# que la condicion en el ciclofor no sea valida


mascotas = ['gatos', 'perros', 'loros', 'peces', 'perros', 'perros']

for i in mascotas: 
    print (i)

contador_gatos = 0
contador_perros = 0
contador_peces = 0

for i in mascotas:
    if i == "gatos":
        contador_gatos = contador_gatos + 1
    elif i == 'perros':
        contador_perros = contador_perros + 1
    elif i == "peces":
        contador_peces = contador_peces + 1


print("El numero de Gato es:", contador_gatos)
print("El número de perros es:", contador_perros)
print("El número de peces es:", contador_peces)

# for i in mascotas:
#     if i == "gatos":
#         contador_gatos = contador_gatos + 1 
# for i in mascotas:
#     if i == "perros":
#         contador_perros = contador_perros + 1
# for i in mascotas:
#     if i == "peces":
#         contador_peces = contador_peces + 1