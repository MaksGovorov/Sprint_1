time = '1h 45m,360s,25m,30m 120s,2h 60s'
time_values = time.split(',')

total_minutes = 0

for time_value in time_values:
    time_units = time_value.split()
    for time_unit in time_units:
        if 'h' in time_unit:
            total_minutes +=int(time_unit.replace('h', '')) * 60
        elif 'm' in time_unit:
            total_minutes +=int(time_unit.replace('m', ''))
        elif 's' in time_unit:
            total_minutes +=int(time_unit.replace('s', '')) // 60
print(total_minutes)




