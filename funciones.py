import csv
import json
import random

# Listado comida
lista_comida=["Completo","As","Papas fritas"]

nombre_error = str
opt=0

def guardar_json(nombre_archivo, datos):
    with open (nombre_archivo, 'w', encoding='utf-8') as json_file:
        json.dump(datos,json_file, indent=4)

def leer_json(nombre_archivo):
    with open (nombre_archivo, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
    
def guardar_archivo_csv(nombre_archivo, datos, fieldnames):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as csv_file:
        data_csv = csv.DictWriter(csv_file, fieldnames=fieldnames)
        data_csv.writeheader()
        data_csv.writerows(datos)


# opciones

def main_1():
    listado_completo=[]

    for i in lista_comida:
        valor = random.randint(1,80) * 100
        i_d = random.randint(1,100)
        n_producto={
            'nombre':i,
            'precio':valor,
            'id':i_d
        }
        listado_completo.append(n_producto)
    print("Listado generado, y guardado.")
    guardar_json('listado_completo.json', listado_completo)

def main_2():
    listado_leer = leer_json('listado_completo.json')
    n= len(listado_leer)

    for leer in listado_leer:
        print(f"====== Mostrar Json ======")
        print(f"= Cant de Elementos: {n}")
        print(f"==== ID: {leer['id']}") 
        print(f"= Nombre: {leer['nombre']}")
        print(f"== Precio: {leer['precio']}")
        print("==========================")

def main_3():
    listado_guardar = leer_json('listado_completo.json')
    fieldnames = ['nombre', 'precio', 'id']
    guardar_archivo_csv('reporte.csv', listado_guardar, fieldnames)
    print("Reporte Guardado Exitosamente!")

def main_4():
    print("Saliendo...")
    exit()