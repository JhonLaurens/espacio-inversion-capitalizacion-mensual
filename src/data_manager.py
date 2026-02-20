
import csv
import os
from datetime import datetime

class DataManager:
    """
    Manejo de exportación de datos.
    """
    
    @staticmethod
    def exportar_csv(datos: list, output_dir: str = "output"):
        """
        Exporta la lista de datos a un archivo CSV.
        
        Args:
            datos: Lista de diccionarios con los datos a exportar.
            output_dir: Directorio de salida.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_dir, f"reporte_inversion_{timestamp}.csv")
        
        if not datos:
            print("No hay datos para exportar.")
            return

        keys = datos[0].keys()
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys)
                writer.writeheader()
                writer.writerows(datos)
            print(f"Reporte exportado exitosamente a: {filename}")
        except IOError as e:
            print(f"Error al escribir el archivo CSV: {e}")
