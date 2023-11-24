from LoadBalancing import LoadBalancing
from Server import Server

# from unittest import TestCase
# # Test cases
# class TryTesting(TestCase):
# 	def test_always_passes(self):
# 		self.assertTrue(True)
#
# 	def test_always_fails(self):
# 		self.assertTrue(False)


# Server
print('-- Server --')

server = Server()
server.add_connection("192.168.1.1")
print('server load: ', server.load())

server.close_connection("192.168.1.1")
print('server load after closed: ', server.load())

print()
# LoadBalancing
print('-- Load Balancing --')

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print('Average load adding 1 connection: ', l.avg_load())

l.servers.append(Server())
print('Average load adding 1 Server', l.avg_load())

l.close_connection("fdca:83d2::f20d")
print('average load close connection', l.avg_load())

n = 10000

for connection in range(n):
	l.add_connection(connection)
print('Testing load balancing when injecting {} connection'.format(n), l, )
print('Highest Load: {}%'.format(round(max(l.highest_load), ndigits=2)))
print(l.avg_load())
