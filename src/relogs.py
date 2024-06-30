import re
from utils import Utils


class Relogs:
    def __init__(self, logs):
        self.logs = logs
        self.patter_re = r"sql:'(.*)', prms:\[([^\]]*)\]"

        self.patter_param_val = r"Parameter value: ([^,]+)"
        self.patter_error_sent = r"Error in sentence: (.*)"
        self.patter_param = r"(.*)\sParameters: \{([^}]*)\}"

    def get_normal_queries(self, logs):
        pattern = re.compile(self.patter_re)
        matches = pattern.findall(logs)

        return matches

    def get_error_queries(self, log):
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

    def main(self):
        logs_list = self.logs.strip().split("\n")
        content = []
        for logs in logs_list:
            if self.get_normal_queries(logs):
                content.append(self.get_normal_queries(logs))
            elif self.get_error_queries(logs):
                content.append(self.get_error_queries(logs))
        return content
