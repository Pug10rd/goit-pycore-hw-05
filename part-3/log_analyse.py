from pathlib import Path
import sys


try:
    if sys.argv[1]:
        input_value = sys.argv[1]
except IndexError:
    print("You have to provide file path")
    exit()
    
# input_value = sys.argv[1]
route = Path(input_value)

logs_counts = {}

def load_logs(path: str):
    path_param = Path(path)
    if path_param.exists() and path_param.is_file():
        with open(path_param, 'r') as fh:
            lines_list = [line for line in fh.readlines() if line.strip()]

            return lines_list
    else:
        print("load_logs error")

def parse_log_line(line: str):
    return line.split()

def filter_logs_by_level(logs: list, level: str):
    def filter_check(line: str):
        return line.split()[2].lower() == level.strip().lower()
          
    filtered_logs = filter(filter_check, logs)
    filtered_list = list(filtered_logs)
    if len(filtered_list) > 0:
        print("\vDetails: \v")
        for line in filtered_list:
            print(str(line).strip().lower().replace(level, "-"))
    
    else:
        print("\vERROR: you need to use one of the following arguments: info, error, debug, warning") 

def count_logs_by_level(logs: list):
    for line in logs:
        if line.split()[2] in logs_counts:
            logs_counts[line.split()[2]] += 1
        else:
            logs_counts[line.split()[2]] = 1
    return logs_counts

def display_log_counts(counts: dict):
    for key, value in counts.items():
            print(f"{key}: {value}")


if route.is_file() and len(sys.argv) > 2:
    #if we DO want to filter our logs for a specific level
    level = sys.argv[2]
    display_log_counts(count_logs_by_level(load_logs(route)))   
    filter_logs_by_level(load_logs(route), level)

elif route.is_file() and len(sys.argv) == 2:
    #if we DO NOT want to filter our logs for a specific level
    display_log_counts(count_logs_by_level(load_logs(route)))

else:
    print(f"Path: '{input_value}' is not a correct path, please check it and try again")