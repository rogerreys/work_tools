import re
from .utils import Utils


class Reloads:
    """
   Clase Reloads para procesar registros de logs SQL.

   Métodos:
   --------
   __init__(self, logs: str):
       Inicializa la instancia de la clase con los logs proporcionados.

   get_normal_queries(self, logs: str) -> list:
       Obtiene las consultas SQL normales de los logs.

   get_error_queries(self, log: str) -> list:
       Obtiene las consultas SQL que contienen errores de los logs.

   split_data_by_pattern(self) -> list:
       Divide los datos de los logs en consultas normales y consultas con errores.
   """

    def __init__(self, logs):
        """
        Inicializa la instancia de la clase Reloads.

        Parámetros:
        -----------
        logs : str
            Cadena de texto que contiene los logs SQL a procesar.
        """
        self.logs = logs
        self.patter_re = r"sql:'(.*)', prms:\[([^\]]*)\]"

        self.patter_param_val = r"Parameter value: ([^,]+)"
        self.patter_error_sent = r"Error in sentence: (.*)"
        self.patter_param = r"(.*)\sParameters: \{([^}]*)\}"

    def get_normal_queries(self, logs) -> list:
        """
        Obtiene las consultas SQL normales de los logs.

        Parámetros:
        -----------
        logs : str
            Cadena de texto que contiene los logs SQL.

        Retorna:
        --------
        list
            Lista de tuplas que contienen las consultas SQL y sus parámetros.
        """
        pattern = re.compile(self.patter_re)
        matches = pattern.findall(logs)

        return matches

    def get_error_queries(self, log) -> list:
        """
        Obtiene las consultas SQL que contienen errores de los logs.

        Parámetros:
        -----------
        log : str
            Cadena de texto que contiene un log SQL.

        Retorna:
        --------
        list
            Lista de tuplas que contienen las consultas SQL con errores y sus parámetros.
        """
        pattern_error = re.compile(self.patter_error_sent)
        pattern_values = re.compile(self.patter_param_val)
        patter = re.compile(self.patter_param)

        matches_error = []
        for match in pattern_error.findall(log):

            if pattern_values.findall(match):
                m = patter.findall(match)
                values = pattern_values.findall(m[0][1])
                values_p = [float(x) if Utils.is_number(x) else x for x in values]
                matches_error.append((m[0][0].strip(), values_p))
            else:
                matches_error.append((match.strip(), None))

        return matches_error

    def split_data_by_pattern(self) -> list:
        """
        Divide los datos de los logs en consultas normales y consultas con errores.

        Retorna:
        --------
        list
            Lista de listas que contienen las consultas normales y las consultas con errores.
        """
        logs_list = self.logs.strip().split("\n")
        content = []
        for logs in logs_list:
            if self.get_normal_queries(logs):
                content.append(self.get_normal_queries(logs))
            elif self.get_error_queries(logs):
                content.append(self.get_error_queries(logs))
        return content
