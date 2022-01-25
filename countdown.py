from dataclasses import dataclass
from datetime import datetime

LAUNCH_DATE = datetime(2024,11,1)

days_to_launch = LAUNCH_DATE - datetime.now()

print(days_to_launch.days)

with open('README.md', "w") as f:
    f.write("# HERMES Launch Countdown Clock\n\n")
    f.write("# {0} days".format(days_to_launch.days))