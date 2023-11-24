import random


class Server:
	def __init__(self):
		"""Creates a new server instance, with no active connections."""
		self.connections = {}

	def add_connection(self, connection_id):
		"""Adds a new connection to this server."""
		connection_load = random.random() * 10 + 1
		# Add the connection to the dictionary with the calculated load
		self.connections[connection_id] = connection_load

	def close_connection(self, connection_id):
		"""Closes a connection on this server."""
		#         self.connections.pop(connection_id)
		del self.connections[connection_id]
		# Remove the connection from the dictionary

	def load(self):
		"""Calculates the current load for all connections."""
		current_loads = 0
		# Add up the load for each of the connections
		for load in self.connections.values():
			current_loads += load
		return current_loads  # dung lượng truy cập mb/s

	def __str__(self):
		"""Returns a string with the current load of the server"""
		return "{:.2f}%".format(self.load())
