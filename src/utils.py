class Utils:
    """
    Clase Utils que proporciona métodos utilitarios estáticos.

    Métodos:
    --------
    is_number(s: str) -> bool:
        Verifica si una cadena de texto puede ser convertida a un número.
    """

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
