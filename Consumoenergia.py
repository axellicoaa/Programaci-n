
consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84}
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Manta': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
        'Puerto Ayora': { 'consumos': (50, 50),'tarifa': 10}
 },
}

planta="Sopladora"
result= consumo_energia[planta]
total= 0
for index, r in enumerate(result.values()):
    if index >4 and index < 10:
        total+= ["consumos"][2]
print(total)






# def total_consumo_por_planta_ciudad(planta, ciudad):
#     if planta not in consumo_energia.keys():
#         return 'La planta ' + planta + ' no existe'

#     if ciudad not in consumo_energia[planta].keys():
#         return 'La planta ' + planta + ' no proveé energía a la ciudad de ' + ciudad

#     total_consumo = sum(consumo_energia[planta][ciudad]['consumos'])
#     return total_consumo


# informacion = {
#     'Costa': ('Guayaquil', 'Manta'),
#     'Sierra': ('Quito', 'Ambato', 'Loja'),
#     'Oriente': ('Tena', 'Nueva Loja')
# }
# def total_consumo_por_planta_ciudad(planta, ciudad):
#     if planta not in consumo_energia.keys():
#         return 'La planta ' + planta + ' no existe'

#     if ciudad not in consumo_energia[planta].keys():
#         return 'La planta ' + planta + ' no proveé energía a la ciudad de ' + ciudad

#     total_consumo = sum(consumo_energia[planta][ciudad]['consumos'])
#     return total_consumo

# informacion['Insular'] = ('Puerto Ayora', 'Puerto Villamil')
# def total_por_region(region):

#     if region not in informacion.keys():
#         return 'region no existe'

#     ciudades_region = informacion[region]

#     total_consumo = 0
#     for ciudad_region in ciudades_region:
#         for planta in consumo_energia.keys():
#             for ciudad in consumo_energia[planta].keys():
#                 if ciudad_region ==  ciudad:
#                     total_consumo += sum(consumo_energia[planta][ciudad]['consumos']) * consumo_energia[planta][ciudad]['tarifa']
#     print("Total de la región seleccionada")
#     return total_consumo





# op = -1
# while op != 0:

#     print('<1> Total de energía consumida por planta y ciudad')
#     print("<2> Total de energia por ciudad")
#     print('<3> Total por región')
#     print('<0> Salir')

#     op = int(input('Ingrese opción:'))

#     if op == 1:
#         planta = input('Ingrese el nombre de la planta (Coca Codo Sinclair, Sopladora):')
#         ciudad = input('Ingrese el nombre de la ciudad:')

#         total = total_consumo_por_planta_ciudad(planta, ciudad)

#         if type(total) == int:
#             print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total, planta))
#         else:
#             print(total)
#     if op == 2:
#         ciudad = input('Ingrese el nombre de la ciudad:')
#         if ciudad in consumo_energia['Sopladora'].keys(): 
#             Sopla=sum(consumo_energia['Sopladora'][ciudad]['consumos'])
#             print('Planta sopladora consume:',Sopla,'mwb')

#             if ciudad in consumo_energia['Coca Codo Sinclair'].keys():
#                 Cocacos=sum(consumo_energia['Coca Codo Sinclair'][ciudad]['consumos'])
#                 print('Planta Coca Codo Sinclair consume:',Cocacos,'mwb') 
#             else:
#                 print('error')        

#     if op == 3:
#         region = input('Ingrese región:')
#         total = total_por_region(region)
#         print(region, ':', total, '\n')
#     if op == 0:
#         print('''   
# ¡Por este Ecuador amazónico, desde siempre y hasta siempre!
# 		    ¡Viva la patria!
#          ''')

