import csv  # Importa el módulo csv de Python, que proporciona funcionalidades para leer y escribir archivos CSV.

def read_csv(path):
    """
    Función para leer un archivo CSV y convertir su contenido en una lista de diccionarios.
    
    Args:
        path (str): Ruta del archivo CSV a leer.
        
    Returns:
        list: Lista de diccionarios donde las claves son los encabezados de las columnas y los valores son los datos correspondientes de cada fila.
    """
    with open(path, 'r') as csvfile:  # Abre el archivo CSV en modo de lectura.
        reader = csv.reader(csvfile, delimiter=',')  # Crea un objeto reader para leer el archivo CSV.
        header = next(reader)  # Lee la primera línea del archivo, que contiene los encabezados de las columnas.
        data = []  # Inicializa una lista para almacenar los datos.
        for row in reader:  # Itera sobre cada fila del archivo (excluyendo la primera fila, que son los encabezados).
            iterable = zip(header, row)  # Combina los encabezados con los valores de la fila actual.
            country_dict = {key: value for key, value in iterable}  # Crea un diccionario para la fila actual.
            data.append(country_dict)  # Agrega el diccionario a la lista de datos.
        return data  # Devuelve la lista de diccionarios.

if __name__ == '__main__':
    # Si el script se ejecuta directamente, lee el archivo CSV y muestra la primera fila de datos.
    data = read_csv('./app/data.csv')  # Lee el archivo CSV.
    print(data[0])  # Imprime la primera fila de datos.
