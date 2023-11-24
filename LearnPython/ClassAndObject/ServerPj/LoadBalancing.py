from Server import Server
import random

class LoadBalancing:
	def __init__(self):
		"""Initialize the load balancing system with one server"""
		self.connections = {}
		self.highest_load = []
		self.servers = [Server()]  # Server() from Server.py
		self.server_index = 0
		self.max_load = 50

	def add_connection(self, connection_id):
		"""Randomly selects a server and adds a connection to it."""

		# TODO: make a sort algorithm to find Server() have > 50 ip
		# server = random.choice(self.servers)

		server_index = self.server_index
		server = self.servers[server_index]
		#TODO: fix over flows bug

		# self.servers count from 1
		if (server.load()) > (self.max_load-5):
			self.server_index = -1

		# Add the connection to the dictionary with the selected server
		self.connections[connection_id] = server  # implement connection to Server class
		# Add the connection to the server
		self.connections[connection_id].add_connection(connection_id)  # add_connection in class Server not LoadBalancing

		self.ensure_availability()

	def close_connection(self, connection_id):
		""" Closes the connection on the the server corresponding to connection_id."""
		# Find out the right server
		del_server = self.connections[connection_id]
		# Close the connection on the server
		del_server.close_connection(connection_id)
		# Remove the connection from the load balancer
		del self.connections[connection_id]

	def avg_load(self):
		total_server = len(self.servers)
		"""Calculates the average load of all servers"""
		# Sum the load of each server and divide by the amount of servers
		total_load = sum(s.load() for s in self.servers)
		return total_load / total_server

	def ensure_availability(self):
		"""If the average load is higher than 50, spin up a new server"""
		if self.avg_load() > self.max_load:
			self.servers.append(Server())


	def __str__(self):
		"""Returns a string with the load for each server."""
		loads = [str(server) for server in self.servers]
		[self.highest_load.append((server.load())) for server in self.servers]

		return "[{}]".format(",".join(loads))


LoadBalancing().add_connection('fdca:83d2::f20d')
