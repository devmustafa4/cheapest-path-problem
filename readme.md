# Cheapest Path Finder

## Description
The Cheapest Path Finder is a Python program that uses Dijkstra's algorithm to determine the most cost-effective route between two airports. Given a set of routes, each defined by a starting airport, a destination airport, and the associated travel cost, the program efficiently calculates the cheapest path.

The input data is read from a JSON file, and the program validates the data for correctness before processing. The result includes the cheapest path (as a list of airports) and the total cost of that path.

## Usage
### Running the code

Run the following command after cloning the repository.

```bash
python main.py
```

You can also import the `find_cheapest_path` function from `utils.py` and use it in your own code.

```python
from utils import find_cheapest_path

# Example usage
airports = [
    {"start": "A", "end": "B", "cost": 10},
    {"start": "B", "end": "C", "cost": 15},
    {"start": "A", "end": "C", "cost": 30},
    {"start": "B", "end": "D", "cost": 50},
    {"start": "D", "end": "C", "cost": 30},
    {"start": "A", "end": "D", "cost": 100}
]

start = "A"
end = "C"

path, cost = find_cheapest_path(airports, start, end)
print(f"Cheapest path: {path}")
print(f"Total cost: {cost}")
```

If you want to use a JSON file as input, you can use the `get_data_from_path` function to read the data from the file.

```python
from utils import get_data_from_path, find_cheapest_path

# Example usage
path = "data/data.json"
airports = get_data_from_path(path)

start = "A"
end = "C"

path, cost = find_cheapest_path(airports, start, end)
print(f"Cheapest path: {path}")
print(f"Total cost: {cost}")
```

## Project Structure

### Data
Contains the example JSON file `data.json` which stores the airport routes. The JSON file contains a list of dictionaries, where each dictionary represents a route with the following keys:
- `start`: The starting airport code.
- `end`: The destination airport code.
- `cost`: The cost of the route.

### Main.py
Contains an example `main()` function which prompts the users for start and end airports and returns the cheapest path and cost.

### Utils.py
The program consists of two main functions:

1. **`find_cheapest_path(airports, start, end)`**
   - Finds the cheapest path between the specified start and end airports.
   - **Parameters:**
     - `airports` (list of dicts): List of routes where each route is represented as a dictionary with `start`, `end`, and `cost`. See `data.json` in the `data` folder for reference.
     - `start` (str): The starting airport code.
     - `end` (str): The destination airport code.
   - **Returns:**
     - A tuple containing the cheapest path (list of airports) and the total cost (float).
   
2. **`get_data_from_path(path)`**
   - Reads airport route data from a specified JSON file and validates it.
   - **Parameters:**
     - `path` (str): The file path to the JSON data file.
   - **Returns:**
     - A list of routes (dictionaries) after validation.

### Tests.py
1. **`TestFindCheapestPath`**
    - Contains test cases for the `find_cheapest_path` function.

2. **`TestGetDataFromPath`**
    - Contains test cases for the `get_data_from_path` function.

## Testing
To run the tests, execute the following command:

```bash
python tests.py
```

## Time and Space Complexity
- Time complexity: `O(E logV)` where E is the number of edges and V is the number of vertices in the graph.
  - The `heapq` module is used to implement the priority queue in the algorithm, which has a time complexity of O(log n) for insertion and deletion.
- Space complexity: `O(V + E)` where V is the number of vertices and E is the number of edges in the graph.