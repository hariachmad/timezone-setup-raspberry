import zoneinfo
import datetime

timezone = "Asia/Jakarta"

if timezone in zoneinfo.available_timezones():
    print("Timezone tersedia")
else:
    print("Timezone tidak tersedia")

print(datetime.datetime.now().astimezone().tzinfo)
    