from datetime import datetime
import json, os, errno


class Utils:
    """
    Clase Utils que proporciona métodos utilitarios estáticos.

    Métodos:
    --------
    is_number(s: str) -> bool:
        Verifica si una cadena de texto puede ser convertida a un número.
    """
    PATH_JSON = "config.json"

    @staticmethod
    def is_number(s) -> bool:
        """
        Verifica si una cadena de texto puede ser convertida a un número.

        Parámetros:
        -----------
        s : str
            Cadena de texto a verificar.

        Retorna:
        --------
        bool
            Retorna True si la cadena puede ser convertida a un número, False en caso contrario.
        """
        try:
            if len(s) == 10 and float(s):
                return False
            float(s)
            return True
        except ValueError:
            return False

    @staticmethod
    def read_file_to_variable(file_path) -> str:
        """
        Lee el contenido de un archivo y lo guarda en una variable.

        Parámetros:
        -----------
        file_path : str
            La ruta del archivo a leer.

        Retorna:
        --------
        str
            El contenido del archivo.
        """

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"Error: El archivo '{file_path}' no fue encontrado.")
            return None
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None

    import json

    @staticmethod
    def read_json_file(file_path):
        """
        Lee el contenido de un archivo JSON y lo guarda en una variable.

        Parámetros:
        -----------
        file_path : str
            La ruta del archivo JSON a leer.

        Retorna:
        --------
        dict
            El contenido del archivo JSON como un diccionario.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: El archivo '{file_path}' no fue encontrado.")
            return None
        except json.JSONDecodeError:
            print(f"Error: El archivo '{file_path}' no es un JSON válido.")
            return None
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None

    @staticmethod
    def get_data_from_json(json_data):
        """
        Obtiene el valor de la clave 'path' dentro de la configuración del JSON.

        Parámetros:
        -----------
        json_data : dict
            El contenido del archivo JSON como un diccionario.

        Retorna:
        --------
        str
            El valor de la clave 'path' dentro de 'config'.
        """
        try:
            return json_data['config']['path_logs'], json_data['config']['path_response']
        except KeyError:
            print("Error: La clave 'path' no se encuentra en la configuración del JSON.")
            return None

    @staticmethod
    def save_values_to_file(data, file_path):
        """
        Guarda el resultado de la función assignation_values en un archivo de texto.

        Parámetros:
        -----------
        data : list
            Lista de diccionarios que contienen las claves 'sql' y 'prms'.
        file_path : str
            La ruta del archivo donde se guardarán los resultados.
        """
        try:
            # Obtener el nombre del archivo de la ruta completa
            base_name, ext = os.path.splitext(os.path.basename(file_path))
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            filename = f"{base_name}_{current_time}{ext}"

            # Crear las carpetas necesarias si no existen
            folder_path = os.path.dirname(file_path)

            file_path = f"{folder_path}/{filename}"
            if folder_path:
                os.makedirs(folder_path, exist_ok=True)

            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(data + '\n')
        except OSError as e:
            if e.errno == errno.ENOENT:
                print(f"Error: No se encontró el directorio para '{file_path}'")
            else:
                print(f"Error al guardar los resultados en el archivo: {e}")
        except Exception as e:
            print(f"Error al guardar los resultados en el archivo: {e}")

        return f"Resultados guardados en '{file_path}'"
