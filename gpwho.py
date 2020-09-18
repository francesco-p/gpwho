import re
import time
import subprocess
import datetime
from collections import defaultdict


def parse_subdivision(usage_subdivision):
    user_regex = re.compile(r"(.+)\((.+)M\)")
    usage_dict = defaultdict(int)
    for user_usage in usage_subdivision:
        res = user_regex.search(user_usage)
        user = res.group(1)
        usage = res.group(2)
        usage_dict[user] += int(usage)
    return usage_dict


def parse_gpustat(response):
    main_regex = re.compile(r"\[0\] GeForce .+ \| .+ \% \| (.+) / (.+) MB \| (.+)")
    res = main_regex.search(response)
    total_usage = int(res.group(1).rstrip().lstrip())
    max_memory = res.group(2).rstrip().lstrip()
    usage_subdivision = res.group(3).rstrip().lstrip().split(' ')
    return total_usage, max_memory, usage_subdivision


def main():
    #--- Param ---#
    SECONDS = 20
    #-------------#

    init = True
    print("gpwho initialization...")
    while True:
        time.sleep(SECONDS)
        timestamp = f"{datetime.datetime.now():%Y/%m/%d %H:%M:%S }"
        total_usage, max_memory, usage_subdivision = parse_gpustat(subprocess.check_output(['gpustat']).decode())
        usage = parse_subdivision(usage_subdivision)

        for user in usage.keys():
            user_usage = usage[user]
            detailed_entry = f"{user},{user_usage},{total_usage},{max_memory},{timestamp}\n"
            with open("detailed_usage.csv", "a") as f:
                f.write(detailed_entry)
        if init:
            print(f"Status OK, first entry:\n{detailed_entry}\nIt is possible now to start tgram.py...")
        init = False


if __name__ == "__main__":
    main()
