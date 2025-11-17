import json
import pathlib
import logging
import csv

#task 1
def union_for_csv(path_to_csv_1, path_to_csv_2):
    with open(path_to_csv_1, 'r') as csvfile:
        csv_1 = list(csv.reader(csvfile))
        print(csv_1)
    with open(path_to_csv_2, 'r') as csvfile:
        csv_2 = list(csv.reader(csvfile))
        print(csv_2)

    csv_header = csv_1[0]
    csv_result = []

    csv_result.extend(csv_1[1:])
    csv_result.extend(csv_2[1:])

    csv_result = [tuple(t) for t in csv_result]
    csv_result_set = set(csv_result)
    csv_result = [list(t) for t in csv_result_set]

    csv_result.insert(0, csv_header)
    print(csv_result)
    with open("results_Buhai.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(csv_result)


#task 2
def is_json_valid(file_dir):
    for files in file_dir.iterdir():
        if files.suffix == '.json':
            path_to_json = pathlib.Path(files)
            try:
                with open(path_to_json, "r", encoding="utf-8") as json_file:
                    data = json.load(json_file)

            except json.JSONDecodeError as e:
                logger.error(
                    f"Invalid JSON in file '{path_to_json}': {e.msg} "
                    f"(line {e.lineno}, column {e.colno})")

#task 3
def search_in_group(group, file):
    

if __name__ == "__main__":
    # task 1
    csv_1_path = pathlib.Path(__file__).parent / "task_1_csv" / "random.csv"
    csv_2_path = pathlib.Path(__file__).parent / "task_1_csv" / "random-michaels.csv"

    union_for_csv(csv_1_path, csv_2_path)

    # task 2
    logging.basicConfig(
        filename="json_Buhai.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    dir_with_jsons = pathlib.Path(__file__).parent / "task_2_json"
    is_json_valid(dir_with_jsons)


    #task 3