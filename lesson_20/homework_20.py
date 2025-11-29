from argparse import FileType
import logging
from datetime import datetime, timedelta


def filter_log_by_key(log_file : FileType, key_time_stamp : str) -> list[datetime]:
    with open(log_file, 'r') as f:
        log_data = f.readlines()
    log_for_key = []
    for row in log_data:
        if key_time_stamp in row:
            time_stamp_index = row.find('Timestamp') + len('Timestamp')
            time_stamp_str = row[time_stamp_index + 1:(time_stamp_index + len('Timestamp'))]

            time_stamp = datetime.strptime(time_stamp_str, "%H:%M:%S")
            log_for_key.append(time_stamp)
    return log_for_key

def log_requirements_analysis(list_of_datetime: list[datetime]):
    index = 1
    while index <= len(list_of_datetime) - 1:
        time_diff = list_of_datetime[index - 1] - list_of_datetime[index]
        if time_diff > timedelta(seconds=31) and time_diff < timedelta(minutes=33):
            logger.warning(f'time_diff between {list_of_datetime[index - 1].time()} and {list_of_datetime[index].time()} is {time_diff}')

        if time_diff > timedelta(seconds=33):
            logger.error(f'time_diff between {list_of_datetime[index - 1].time()} and {list_of_datetime[index].time()} is {time_diff}')
        index += 1



logger = logging.getLogger('Log_analyzer')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('hb_test.log')
formatter = logging.Formatter("%(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

key = 'TSTFEED0300|7E3E|0400'
list_time_stamps = filter_log_by_key('hblog.txt', key)
log_requirements_analysis(list_time_stamps)

