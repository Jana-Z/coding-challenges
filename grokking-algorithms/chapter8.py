def greedy_radio_stations():
    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
    stations = {}
    stations["kone"] = {'id', 'nv', 'ut'}
    stations["ktwo"] = {'wa', 'is', 'mt'}
    stations["kthree"] = {'or', 'nv', 'ca'}
    stations["kfour"] = {'nv', 'ut'}
    stations["kfive"] = {'ca', 'az'}
    final_stations = set()
    while states_needed:
        localMaxStation = ('', float('inf'))
        for k, v in stations.items():
            if len(states_needed - v) < localMaxStation[1]:
                localMaxStation = (k, len(states_needed - v))
        states_needed = states_needed - stations[localMaxStation[0]]
        final_stations.add(localMaxStation[0])
    print(final_stations)

if __name__ == '__main__':
    greedy_radio_stations()