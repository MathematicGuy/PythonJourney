import sys  # use to assign infinite cost
from heapq import heapify, heappush  # healp to implement heap sort function

''' Dijkstra algorithm '''

from unittest import TestCase
# Test cases
class TryTesting(TestCase):
	def test_always_passes(self):
		self.assertTrue(True)

	def test_always_fails(self):
		self.assertTrue(False)


def dijskatra(graph, scr, dest):
    inf = sys.maxsize  # chứa -> giá trị vô tận
    ''' node_data lưu (giá của các điểm và điểm tr'c nó) đi từ A '''
    node_data = {
        # previous_node / predecessors: điểm trước nó
        # inf -> vô tận
        # dist -> distance: khoảng cách
        'A': {'gia_tri': inf, 'previous_node': []},
        'B': {'gia_tri': inf, 'previous_node': []},
        'C': {'gia_tri': inf, 'previous_node': []},
        'D': {'gia_tri': inf, 'previous_node': []},
        'E': {'gia_tri': inf, 'previous_node': []},
        'F': {'gia_tri': inf, 'previous_node': []},
    }
    # lưu lại điểm trước nó để in ra đường ngắn nhất tới destination.

    node_data[scr]['gia_tri'] = 0  # khoảng cách tới điểm ban đầu = 0
    visited = []  # Mọi điểm trong Visited sẽ ko đc Xét
    diem_bat_dau_hien_tai = scr  # điểm bắt đầu (Thay mỗi khi hết 1 chu kì)
    total_node = 6  # số nút trong hình

    #Space-Complexity : O(n^2)
    for i in range(total_node - 1):  # số đoạn = số nút - 1
        if diem_bat_dau_hien_tai not in visited:  # nếu điểm bắt đầu ko trong visited
            visited.append(diem_bat_dau_hien_tai)  # thêm điểm bắt đầu vào visited
            min_heap = []  # chứa (khoảng cách đi tới các điểm lân cận và điểm đó) của điểm hiện tại.
            # VD: A->B: 0 + 2 = 2 và A -> C = 0 + 4 = 4  nên min_heap = [(2, 'B'), (4, 'C')]

            '''
             Xét khoảng cách đi tới các điểm lân cận 
                + graph[diem_bat_dau_hien_tai] -> các điểm lân cận của điểm bắt đầu hiện tại. VD: 'A': {'B': 2, 'C': 4}
                + Vs ' diem_bat_dau_hien_tai ' là A thì ' tung_diem_lan_can ' là B và C 
            '''
            for tung_diem_lan_can in graph[diem_bat_dau_hien_tai]:  # Cho từng điểm lân cận trong điểm hiện tại từ đồ thị.
                if tung_diem_lan_can not in visited:  # Kiểm tra nếu điểm lân cận nằm trong visited

                    ''' 
                        Mục đích: Thay giá trị nhỏ nhất cho điểm hiện tại
                        So sánh khoảng cách mới tới điểm lân cận cũ với mới
                        + gia_tri: khoảng cách mới.  Dùng để thay nếu nó bé hơn giá trị hiện tại
                        + node_data[diem_bat_dau_hien_tai]['gia_tri'] -> khoảng cách tới điểm hiện tại tính từ điểm xuất phát A
                        + graph[diem_bat_dau_hien_tai][tung_diem_lan_can] -> Khoảng cách từ điểm hiện tại tới điểm lân cận
                    '''

                    gia_tri = node_data[diem_bat_dau_hien_tai]['gia_tri'] + graph[diem_bat_dau_hien_tai][tung_diem_lan_can]  # tính tổng khoảng cách đi tới điểm đó
                    if gia_tri < node_data[tung_diem_lan_can]['gia_tri']:  # so sánh khoảng cách hiện tại vs khoảng cách mới ?
                        node_data[tung_diem_lan_can]['gia_tri'] = gia_tri  # Thay khoảng cách hiện tại = khoảng cách mới

                        """
                         Thay Previous Node mới cho Node khi tìm đc đường ngắn hơn cho nó   
                         node_data[tung_diem_lan_can]['previous_node'] -> các điểm đi qua từ A đến điểm hiện tại
                         VD: điểm hiện tại là D thì A -> D đi qua các điểm A-C-D
                         list(diem_bat_dau_hien_tai) -> cho diem_bat_dau_hien_tai vào 1 danh sách
                         VD: diem_bat_dau_hien_tai = 'D' hàm list trên trả lại ['D']
                        """

                        node_data[tung_diem_lan_can]['previous_node'] = node_data[diem_bat_dau_hien_tai]['previous_node'] + list(diem_bat_dau_hien_tai)
                        print('đường ngắn nhất tới điểm hiện tại từ A: ', node_data[tung_diem_lan_can]['previous_node'])
                        print()

                    ''' Tìm khoảng cách ngắn nhất giữa các Nodes '''

                    # cho từng (giá trị của các điểm lân cận và điểm đó) vào danh sách min_heap

                    heappush(min_heap, (node_data[tung_diem_lan_can]['gia_tri'], tung_diem_lan_can))
                    print('Khoảng cách của các điểm lân cận:', min_heap)

        # time complexity is O(v^2) without using min-priority queue. With it time-complexity is O(V+E.log(v))
        heapify(min_heap)  # trả lại giá trị nhỏ nhất trong danh sách min_heap.
        diem_bat_dau_hien_tai = min_heap[0][1]  # Thay điểm bắt đầu hiện tại bằng điểm có giá trị nhỏ nhất

        print('min_heap[0]: {} : (gia_tri, node)'.format(min_heap[0])) # trả lại tên node và khoảng cách ngắn nhất từ A tới đó
    print('Shortest Distance: ' + str(node_data[dest]['gia_tri'])) # trả lại khoảng cách ngắn nhất từ A -> F
    print('Shortest Path: ' + str(node_data[dest]['previous_node'] + list(dest)))  # các điểm đi qua để tới 'F'(dest)


if __name__ == "__main__":
    # get a graph data structure
    graph = {
        # cost from current Vertexies to its neighbour
        'A': {'B': 2, 'C': 4},
        'B': {'A': 2, 'C': 3, 'D': 8, },
        'C': {'A': 4, 'B': 3, 'E': 5, 'D': 2},
        'D': {'B': 8, 'C': 2, 'E': 11, 'F': 22},
        'E': {'C': 5, 'D': 11, 'F': 1},
        'F': {'D': 22, 'E': 1},
    }

    source = 'A'
    destination = 'F'
    dijskatra(graph, source, destination)

