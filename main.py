import zoneinfo
import datetime

timezones = sorted(zoneinfo.available_timezones())

for timezone in timezones:
    print(timezone)

timezone = "Asia/Jakarta"

if timezone in zoneinfo.available_timezones():
    print(f"\n{timezone} tersedia")
else:
    print(f"\n{timezone} tidak tersedia")

# Menampilkan timezone yang sedang digunakan sistem
print("Timezone sistem:", datetime.datetime.now().astimezone().tzinfo)