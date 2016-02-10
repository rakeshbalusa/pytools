week = ['Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']
startday_type = 3
datestart = 1
dateend = 16
for day in range(datestart, dateend + 1):
    print week[startday_type] + ', ' + 'Jan' + str(day)
    startday_type += 1
    if startday_type >= len(week):
        startday_type = 0
    day = day + 1
