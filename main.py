from utils import find_cheapest_path, get_data_from_path

airports = get_data_from_path('data/data.json')

start_airport = input('Enter the start airport: ').upper()
end_airport = input('Enter the end airport: ').upper()

path, cost = find_cheapest_path(airports, start_airport, end_airport)
print(f'\nPath: {path}', f'Cost: {cost}', sep='\n')