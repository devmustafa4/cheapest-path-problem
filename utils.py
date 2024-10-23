import heapq
import json

def find_cheapest_path(airports, start, end):
    costs = {start: 0}
    cheapest_paths = {}
    min_heap = [(0, start)] 
    visited = set()

    while min_heap:
        # get the airport with the lowest cost
        current_cost, current_airport = heapq.heappop(min_heap)

        if current_airport == end:
            break

        if current_airport in visited:
            continue

        visited.add(current_airport)

        # find neighboring airports and update the cost if a cheaper path is found
        for route in airports:
            if route['start'] == current_airport and route['end'] not in visited:
                new_cost = current_cost + route['cost']
                
                # if the neighboring airport is not visited or the new cost is lower than the existing
                if route['end'] not in costs or new_cost < costs[route['end']]:
                    costs[route['end']] = new_cost
                    cheapest_paths[route['end']] = current_airport
                    heapq.heappush(min_heap, (new_cost, route['end']))

    # if no path is found to the destination
    if end not in cheapest_paths and end != start:
        return None, float('inf')

    # path construction
    path = [end]
    while end != start:
        end = cheapest_paths[end]
        path.append(end)
    path.reverse()

    return path, costs[path[-1]]

def get_data_from_path(path):
    with open(path, 'r') as file:
        data = file.read()
    # convert to json
    data = json.loads(data)
    return data