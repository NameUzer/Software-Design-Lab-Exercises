class Node:
            
	def __init__(self,coeff,exp):
		self.coeff = coeff
		self.exp = exp
		self.next = None

class Linkedlist:
	'''
	Connect a set of coeeficients and polynomial 
	to reperesent an equation
	'''
	def __init__(self):
		self.head = None


	''' Add node in decending order'''
	def add_node(self,coeff,exp):
		if not (self.head):
			self.head = Node(coeff,exp)
			return
		node_last = None
		curr = self.head
		prev = None
		while curr is not None:
			if exp > curr.exp:
				if prev is None:
					item = Node(coeff,exp)
					item.next = self.head
					self.head = item
					return
				item = Node(coeff,exp)
				#nxt = curr.next
				prev.next = item
				item.next = curr
				return

			prev = curr
			curr = curr.next
		prev.next = Node(coeff,exp)

	''' reprsent the equation'''
	def represent(self):
		curr = self.head
		s = ''
		while curr is not None:
			s+= f'{curr.coeff}x^{curr.exp}  '
			curr = curr.next
		return print(s)


# still working on code below this->


l = Linkedlist()

l.add_node(2,1)
l.add_node(3,3)
l.add_node(1,0)

l.represent()

l2 = Linkedlist()

l2.add_node(5,2)
l2.add_node(6,1)
l2.add_node(2,0)

l2.represent()


def add_equations(eq1,eq2):
	'''Add two equations'''
	curr1 = eq1.head
	curr2 = eq2.head

	s = ''

	while curr1 is not None or curr2 is not None:
		if curr1.exp == curr2.exp:
			val = curr1.coeff + curr2.coeff
			s+= f'{val}x^{curr1.exp}  '
			curr1 = curr1.next
			curr2 = curr2.next
		else :
			if curr1.exp> curr2.exp:
				s+= f'{curr1.coeff}x^{curr1.exp}  '
				curr1 = curr1.next
			if curr1.exp< curr2.exp:
				s+= f'{curr2.coeff}x^{curr2.exp}  '
				curr2 = curr2.next

	return print(s)
add_equations(l,l2)