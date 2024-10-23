from utils import find_cheapest_path

airports = [
    {'start': 'ISB', 'end': 'LHR', 'cost': 1000},
    {'start': 'LHR', 'end': 'NYC', 'cost': 750},
    {'start': 'CBS', 'end': 'NYC', 'cost': 775},
    {'start': 'ISB', 'end': 'CBS', 'cost': 575},
    {'start': 'CBS', 'end': 'GRC', 'cost': 731},
    {'start': 'NYC', 'end': 'GRC', 'cost': 459}
]

start_airport = 'ISB'
end_airport = 'NYC'
path, cost = find_cheapest_path(airports, start_airport, end_airport)
# Expected output: ['ISB', 'CBS', 'NYC'], 1350
print(f'Start: {start_airport}', f'End: {end_airport}', f'Path: {path}', f'Cost: {cost}', sep='\n')