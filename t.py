
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    # Define the locations and their coordinates
    data['locations'] = [
        (39, -120),  # Location 0: Reno
        (38, -121),  # Location 1: Sacramento
        (34, -118),  # Location 2: Los Angeles
        (36, -119),  # Location 3: Fresno
        (37, -122),  # Location 4: San Francisco
    ]
    data['num_locations'] = len(data['locations'])
    data['depot'] = 0  # The depot is the starting point for all vehicles
    return data


def compute_distance(lat1, lon1, lat2, lon2):
    """Computes the Euclidean distance between two locations."""
    return ((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2) ** 0.5


def main():
    """Entry point of the program."""
    # Instantiate the data problem
    data = create_data_model()

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(data['num_locations'], 1, data['depot'])

    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a distance callback
    distance_callback = lambda from_index, to_index: compute_distance(
        data['locations'][manager.IndexToNode(from_index)][0],
        data['locations'][manager.IndexToNode(from_index)][1],
        data['locations'][manager.IndexToNode(to_index)][0],
        data['locations'][manager.IndexToNode(to_index)][1])
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Set 10 seconds as the maximum time allowed per each search for a solution
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.time_limit.seconds = 10

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    


    # Print solution
    if solution:
        print('Objective: {} miles'.format(solution.ObjectiveValue()))
        index = routing.Start(0)
        while not routing.IsEnd(index):
            print('Node {} -> '.format(manager.IndexToNode(index)), end='')
            index = solution.Value(routing.NextVar(index))
        print('Node {}'.format(manager.IndexToNode(index)))


if __name__ == '__main__':
    main()
