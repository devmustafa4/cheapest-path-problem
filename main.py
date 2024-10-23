from utils import find_cheapest_path, get_data_from_path

airports = get_data_from_path('data/data.json')
start_airport = 'ISB'
end_airport = 'NYC'
path, cost = find_cheapest_path(airports, start_airport, end_airport)
# Expected output: ['ISB', 'CBS', 'NYC'], 1350
print(f'Start: {start_airport}', f'End: {end_airport}', f'Path: {path}', f'Cost: {cost}', sep='\n')