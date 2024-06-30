class Assignation:
    """
   Clase Assignation para asignar valores a una consulta SQL.

   Métodos:
   --------
   assignation_values(data: dict) -> str:
       Método estático que reemplaza los placeholders '?' en una consulta SQL con valores de los parámetros proporcionados.
   """

    @staticmethod
    def assignation_values(data) -> str:
        """
        Reemplaza los placeholders '?' en una consulta SQL con valores de los parámetros proporcionados.

        Parámetros:
        -----------
        data : dict
            Diccionario que contiene la consulta SQL y los parámetros.
            Formato del diccionario:
            {
                "sql": "QUERY",
                "prms": ["val", 0, "val2", ...]
            }

        Retorna:
        --------
        str
            La consulta SQL con los valores de los parámetros asignados en lugar de los placeholders.
        """
        # Inicializar variables
        copy, i = "", 0
        # Iterar sobre cada carácter en la consulta SQL
        for x in data['sql']:
            if x == "?":
                # Reemplazar el placeholder con el valor correspondiente del parámetro
                if data['prms'] and (type(list(data['prms'])[i]) == float or type(list(data['prms'])[i]) == int):
                    x = str(list(data['prms'])[i])
                elif type(list(data['prms'])[i]) == str:
                    x = '"' + str(list(data['prms'])[i]) + '"'
                i += 1
            copy += x
        return copy
