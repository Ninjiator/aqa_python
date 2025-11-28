from datetime import datetime


def filter_log_by_key(file, key):
    with open(file, 'r') as f:
        log_data = f.readlines()
    log_for_key = []
    for row in log_data:
        if key in row:
            log_for_key.append(row)
    with open('log_by_key.txt', 'w') as file:
        file.writelines(log_for_key)

def log_requirements_analysis(file):
    """
для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log"""

    with open(file, 'r') as f:
        log_data = f.readlines()
    for row in log_data:
        time_stamp_index = row.find('Timestamp') + len('Timestamp')
        time_stamp_str = row[time_stamp_index + 1:(time_stamp_index + len('Timestamp'))]
        print('->',time_stamp_str)
        time_stamp = datetime.strptime(time_stamp_str, "%H:%M:%S")
        print(time_stamp)





key = 'TSTFEED0300|7E3E|0400'
filter_log_by_key('hblog.txt', key)

log_requirements_analysis('log_by_key.txt')