#!/bin/env/python3

import sys


# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     print(line.strip())




# logfile = sys.argv[1]
# with open(logfile) as f:
#   for line in f:
#     if "CRON" not in line:
#       continue
#     print(line.strip())




# pattern = r"USER \((\w+)\)$"
# line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
# result = re.search(pattern, line)
# print(result[1])



import re
def show_time_of_pid(line):
  pattern = r"^(\w+ \d+ \d+:\d+:\d+).*?\[(\d+)\]"
  result = re.search(pattern, line)
  if result:
    return f"{result[1]} pid:{result[2]}"
  return None

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440