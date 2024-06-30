class Utils():

    @staticmethod
    def is_number(s):
        try:
            if len(s) == 10 and float(s):
                return False
            float(s)
            return True
        except ValueError:
            return False
