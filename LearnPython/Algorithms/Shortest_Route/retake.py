# tep 0: import heapq for finding the lowest cost, sys for infinite
import sys
from heapq import heapify, heappush


# step 2: Making dijkstra function
def dijkstra(graph, start, end):
	inf = sys.maxsize  # create infinite value
	nodes_data = {
		# previous nodes các điểm đi qua tr'c đó tới điểm hiện tại.
		'a': {'cost': inf, 'previous_node': []},
		'b': {'cost': inf, 'previous_node': []},
		'c': {'cost': inf, 'previous_node': []},
		'd': {'cost': inf, 'previous_node': []},
		'e': {'cost': inf, 'previous_node': []},
		'f': {'cost': inf, 'previous_node': []},
	}

	nodes_data[start]['cost'] = 0
	new_start = start
	visited = []
	total_node = len(nodes_data)

	for index in range(total_node - 1):
		if new_start not in visited:
			visited.append(new_start)
			min_heap = []

			for each_neighbor in graph[start]:  # for each vertex neighbor
				if each_neighbor not in visited:
					new_cost = nodes_data[new_start]['cost'] + graph[new_start][each_neighbor]
					print('new cost:', new_cost)
					if new_cost < nodes_data[each_neighbor]['cost']:
						nodes_data[each_neighbor]['cost'] = new_cost
						nodes_data[each_neighbor]['previous_node'] = nodes_data[each_neighbor]['previous_node'] + list(
							new_start)
					# min_heap = [('B':2)] vì heappush(list, value) thus to store > 1 values must use (var1, var2)
					heappush(min_heap, (each_neighbor, nodes_data[each_neighbor]['cost']))
					print(min_heap)

			# Only using min-priority after pushing all nodes cost in to min-heap list
			heapify(min_heap)

			new_start = min_heap[0][0]
		# take the lowest cost node
		print('Shortest route: {} take {} cost'.format(nodes_data[end]['previous_node'], nodes_data[end]['cost']))


# print(str(nodes_data[end]['cost']) + nodes_data[end]['previous_node'])

# Step 1: Making da Graph, initialize values

graph = {
	'a': {'b': 2, 'c': 4},
	'b': {'a': 2, 'c': 3, 'd': 8, },
	'c': {'a': 4, 'b': 3, 'd': 2, 'e': 5},
	'd': {'b': 8, 'c': 2, 'e': 11, 'f': 22},
	'e': {'c': 5, 'd': 11, 'f': 1},
	'f': {'d': 22, 'e': 1},
}
start = 'a'
end = 'f'
dijkstra(graph, start, end)
