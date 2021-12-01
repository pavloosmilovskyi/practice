from random import *
class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, data):
		self.data = data

	def set_next(self, next):
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def apppend(self, data):
		new_node = Node(data)
		cur_node = self.head
		if cur_node == None:
			self.head = new_node
			return
		while cur_node.get_next() != None:
			cur_node = cur_node.get_next()
		cur_node.set_next(new_node)

	def generate_list(self, length, start, end):
		if start > end:
			start,end = end, start
		for i in range(length):
			self.apppend(randint(start, end))
		return self

	def show(self):
		cur_node = self.head
		output = ""
		while cur_node != None:
			output += str(cur_node.get_data()) + " "
			cur_node = cur_node.get_next()
		print(output, "\n")

	def length(self):
		cur_node = self.head
		count = 0
		while cur_node != None:
			count += 1
			cur_node = cur_node.get_next()
		return count

	def push_front(self, data):
		new_node = Node(data)
		cur_node = self.head
		new_node.set_next(cur_node)
		self.head = new_node

	def insert(self, index, data):
		new_node = Node(data)
		cur_node = self.head
		count = 0
		last_index = self.length()
		while cur_node.get_next() != None:
			if index == 1:
				self.push_front(data)
				return
			elif last_index + 1 == index :
				self.apppend(data)
				return
			elif count + 2 == index:
				the_node_after_cur = cur_node.get_next()
				cur_node.set_next(new_node)
				new_node.set_next(the_node_after_cur)
				return
			count += 1
			cur_node = cur_node.get_next()
		print("Index is out of range")

	def remove_front(self):
		cur_node = self.head
		self.head = cur_node.get_next()


	def remove(self, index):
		cur_node = self.head
		count = 0
		while cur_node.get_next() != None:
			if index == 1:
				self.remove_front()
				return
			elif count + 2 == index:
				the_node_to_remove = cur_node.get_next()
				the_node_after_removed = the_node_to_remove.get_next()
				cur_node.set_next(the_node_after_removed)
				return
			count += 1
			cur_node = cur_node.get_next()
		print("Index is out of range")

	def method(self):
		check_condition = False
		length = self.length()
		cur_node = self.head
		ccc_node = cur_node.get_next()
		while ccc_node != None:
			a = cur_node.get_data()
			b = ccc_node.get_data()
			if (a > 0 and b < 0) or (a < 0 and b > 0):
				check_condition = True
				cur_node = cur_node.get_next()
				ccc_node = cur_node.get_next()
			else:
				check_condition = False
				break
		cur_node = self.head
		sumar = 0
		if check_condition == True:
			for _ in range(length):
				if cur_node.get_data() > 0:
					sumar += cur_node.get_data()
				cur_node = cur_node.next
			print("sum of positive elements is: ", sumar, "\n")

		else:
			print("negative elements are: ")
			for _ in range(length):
				if cur_node.get_data() < 0:
					print(cur_node.get_data(), end=" ")
				cur_node = cur_node.next
			print("\n")

	def using_generator_or_iterator(self, iterable):
		for i in iterable:
			self.apppend(i)
