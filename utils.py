import heapq
import json
from typing import Dict, List, Optional, Tuple

def find_cheapest_path(airports: List[Dict[str, str]], start: str, end: str) -> Tuple[Optional[List[str]], float]:
    """
    Finds the cheapest path from the start to the end airport using Dijkstra's algorithm.

    Args:
        airports (List[Dict[str, str]]): A list of dictionaries containing different routes between airports and their costs.
        start (str): Target airport to start the journey.
        end (str): Target airport for the journey to end.

    Returns:
        Tuple (Optional[List[str]], float): A tuple containing the cheapest path from the start to the end airport and the cost of the path.
    """
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

def get_data_from_path(path: str) -> List[Dict[str, str]]:
    """
    Reads data from a JSON file and returns a list of dictionaries.

    Args:
        path (str): Path to the JSON file.

    Returns:
        List[Dict[str, str, float]]: A list of dictionaries containing different routes between airports and their costs.
    """
    with open(path, 'r') as file:
        data = file.read()
    # convert to json
    try:
        data = json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON: {e.msg}")

    if not data:
        raise ValueError('No data found in the file.')

    if not isinstance(data, list):
        raise TypeError('Invalid data format. Must be a list of dictionaries.')

    if not all(isinstance(route, dict) for route in data):
        raise TypeError('Invalid data format. Must be a list of dictionaries.')

    if not all('start' in route and 'end' in route and 'cost' in route for route in data):
        raise KeyError('Invalid data format. Each route must have a start, end, and cost.')

    # make all airports uppercase
    for route in data:
        route['start'] = route['start'].upper()
        route['end'] = route['end'].upper()
    
    return data