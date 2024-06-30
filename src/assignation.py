class Assignation():

    @staticmethod
    def assignation_values(self, data):
        # FORMATO 
        #  {"sql":"QUERY", "prms":["val", 0, "val2", ....]}

        copy, i = "", 0

        for x in data['sql']:
            if x == "?":
                if data['prms'] and (type(list(data['prms'])[i]) == float or type(list(data['prms'])[i]) == int):
                    x = str(list(data['prms'])[i])
                elif type(list(data['prms'])[i]) == str:
                    x = '"' + str(list(data['prms'])[i]) + '"'
                i += 1
            copy += x
        return copy
