from mi_utils import cargar_compras, estadisticas, generar_reporte

def main():
    ruta_archivo = "data/ComprasProyecto.csv"
    ruta_salida = "reporte.json"

    compras = cargar_compras(ruta_archivo)
    print("✅ Compras válidas:", len(compras))

    resumen = estadisticas(compras)
    print("📊 Resumen:")
    print(resumen)

    generar_reporte(resumen, ruta_salida)
    print("📁 Reporte generado:", ruta_salida)

main()
