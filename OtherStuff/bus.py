def number(bus_stops):
    peopleCount = 0
    for i in range(len(bus_stops)):
        print(bus_stops[i])
        for j in range(len(bus_stops[i])):
            print(bus_stops[i][j])

number([[10,0],[3,5],[5,8]])