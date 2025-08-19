import csv
import json
from datetime import datetime

# Función para consumir el archivo .csv 
def cargar_compras(ruta):
    compras_validas = []

    archivo = open(ruta, newline='', encoding='utf-8')
    lector = csv.DictReader(archivo)

    for fila in lector:
        
        fila_limpia = {}
        for clave in fila:
            clave_limpia = clave.strip()
            valor_limpio = fila[clave].strip()
            fila_limpia[clave_limpia] = valor_limpio

        
        cantidad = int(fila_limpia["cantidad"])
        precio = int(fila_limpia["precio_unitario"])
        fecha = fila_limpia["fecha"]

        
        if cantidad > 0 and precio > 0:
            if len(fecha) == 10 and fecha[4] == "-" and fecha[7] == "-":
                compras_validas.append(fila_limpia)
            else:
                print("⚠️ Fecha inválida:", fecha)
        else:
            print("⚠️ Cantidad o precio inválidos:", cantidad, precio)

    archivo.close()
    return compras_validas


def estadisticas(data):
    total_ingresos = 0
    ingresos_por_producto = {}
    compras_por_cliente = {}

    for compra in data:
        cantidad = int(compra["cantidad"])
        precio = int(compra["precio_unitario"])
        cliente = compra["cliente"]
        producto = compra["producto"]

        ingreso = cantidad * precio
        total_ingresos += ingreso

        
        if producto in ingresos_por_producto:
            ingresos_por_producto[producto] += ingreso
        else:
            ingresos_por_producto[producto] = ingreso

        
        if cliente in compras_por_cliente:
            compras_por_cliente[cliente] += cantidad
        else:
            compras_por_cliente[cliente] = cantidad

    
    max_ingresos = 0
    top_producto = ""
    for producto in ingresos_por_producto:
        if ingresos_por_producto[producto] > max_ingresos:
            max_ingresos = ingresos_por_producto[producto]
            top_producto = producto

    bono = False
    if total_ingresos > 6000000:
        bono = True

    resumen = {
        "total_ingresos": total_ingresos,
        "top_producto_por_ingresos": top_producto,
        "compras_por_cliente": compras_por_cliente,
        "bono": bono
    }

    return resumen


def generar_reporte(resumen, ruta_salida):
    if resumen["bono"] == True:
        resumen["mensaje"] = "Umbral superado, aplicar descuento corporativo 5% en próxima compra"

    archivo = open(ruta_salida, "w", encoding="utf-8")
    texto_json = json.dumps(resumen, indent=4, ensure_ascii=False)
    archivo.write(texto_json)
    archivo.close()
