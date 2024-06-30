from src.assignation import Assignation
from src.reloads import Reloads
from src.utils import Utils


def get_queries_by_log(logs, path_result) -> None:
    reloads = Reloads(logs)
    data = []
    for i in reloads.split_data_by_pattern():
        query, prm = i[0]
        data.append({"sql": query, "prms": prm})

    assign = Assignation()
    for i in data:
        result = Utils.save_values_to_file(assign.assignation_values(i), path_result)
    print(result)


if __name__ == '__main__':
    path_json = Utils.PATH_JSON
    json_data = Utils.read_json_file(path_json)
    if json_data is not None:
        path_logs, path_result = Utils.get_data_from_json(json_data)

        logs = Utils.read_file_to_variable(path_logs)

        get_queries_by_log(logs, path_result)
    # if path is not None:
    #     print("El valor de 'path' es:", path)


