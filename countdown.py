from datetime import datetime

LAUNCH_DATE = datetime(2025,10,1)

days_to_launch = LAUNCH_DATE - datetime.now()

with open('README.md', "w") as f:
    f.write("# HERMES Launch Countdown Clock\n\n")
    f.write("Launch date (???): {:%A, %B %d %Y}\n".format(LAUNCH_DATE))
    f.write("# {0} days".format(days_to_launch.days))
    f.write("\n\nLast Updated {:%A, %B %d %Y}".format(datetime.now()))
