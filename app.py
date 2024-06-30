from src.assignation import Assignation
from src.reloads import Reloads
from src.utils import Utils


def get_queries_by_log(logs) -> None:
    reloads = Reloads(logs)
    data = []
    for i in reloads.split_data_by_pattern():
        query, prm = i[0]
        data.append({"sql": query, "prms": prm})

    assign = Assignation()
    for i in data:
        print(assign.assignation_values(i))


if __name__ == '__main__':
    path_json = Utils.PATH_JSON
    json_data = Utils.read_json_file(path_json)
    if json_data is not None:
        path = Utils.get_data_from_json(json_data)

        logs = Utils.read_file_to_variable(path)

        get_queries_by_log(logs)
    if path is not None:
        print("El valor de 'path' es:", path)


