import sys  # use to assign infinite cost
from heapq import heapify, heappush  # healp to implement heap sort function
from graph import the_graph

''' Dijkstra algorithm '''


def dijskatra(graph, scr, dest):
	inf = sys.maxsize  # chứa -> giá trị vô tận
	''' node_data lưu (giá của các điểm và điểm tr'c nó) đi từ A '''
	node_data = {
		'A': {'gia_tri': inf, 'previous_node': []},
		'B': {'gia_tri': inf, 'previous_node': []},
		'C': {'gia_tri': inf, 'previous_node': []},
		'D': {'gia_tri': inf, 'previous_node': []},
		'E': {'gia_tri': inf, 'previous_node': []},
		'F': {'gia_tri': inf, 'previous_node': []},
	}

	node_data[scr]['gia_tri'] = 0  # khoảng cách tới điểm ban đầu = 0
	visited = []  # Mọi điểm trong Visited sẽ ko đc Xét
	diem_bat_dau_hien_tai = scr  # điểm bắt đầu (Thay mỗi khi hết 1 chu kì)
	total_node = len(node_data)  # 6 nút trong hình

	for i in range(total_node - 1):  # số đoạn = số nút - 1
		if diem_bat_dau_hien_tai not in visited:  # nếu điểm bắt đầu ko trong visited
			visited.append(diem_bat_dau_hien_tai)  # thêm điểm bắt đầu vào visited
			min_heap = []  # chứa (khoảng cách đi tới các điểm lân cận và điểm đó) của điểm hiện tại.

			for diem_lan_can in graph[diem_bat_dau_hien_tai]:  # Cho từng điểm lân cận trong điểm hiện tại từ đồ thị.
				if diem_lan_can not in visited:  # Kiểm tra nếu điểm lân cận nằm trong visited
					gia_tri = node_data[diem_bat_dau_hien_tai]['gia_tri'] + graph[diem_bat_dau_hien_tai][
						diem_lan_can]  # tính tổng khoảng cách đi tới điểm đó
					if gia_tri < node_data[diem_lan_can]['gia_tri']:  # so sánh khoảng cách hiện tại vs khoảng cách mới ?
						node_data[diem_lan_can]['gia_tri'] = gia_tri  # Thay khoảng cách hiện tại = khoảng cách mới
						node_data[diem_lan_can]['previous_node'] = node_data[diem_bat_dau_hien_tai]['previous_node'] + list(diem_bat_dau_hien_tai)
						print('đường ngắn nhất tới điểm hiện tại từ A: ', node_data[diem_lan_can]['previous_node'])
						print()

					''' Tìm khoảng cách ngắn nhất giữa các Nodes '''
					heappush(min_heap, (node_data[diem_lan_can]['gia_tri'], diem_lan_can))
					print('Khoảng cách của các điểm lân cận:', min_heap)

		heapify(min_heap)  # heapify tạo 1 list có GTNN ở vị trí thứ nhất [0] và lớn nhất ở giữa [len(min_heap)/2].
		diem_bat_dau_hien_tai = min_heap[0][1]  # Thay điểm bắt đầu hiện tại bằng điểm có giá trị nhỏ nhất

		print('min_heap[0]: {} : (gia_tri, node)'.format(min_heap[0]))  # trả lại tên node và khoảng cách ngắn nhất từ A tới đó
	print('Shortest Distance: ' + str(node_data[dest]['gia_tri']))  # trả lại khoảng cách ngắn nhất từ A -> F
	print('Shortest Path: ' + str(node_data[dest]['previous_node'] + list(dest)))  # các điểm đi qua để tới 'F'(dest)


if __name__ == "__main__":  # to optimize running time

	graph = the_graph['normal']

	source = '1'
	destination = '7'
	dijskatra(graph, source, destination)
