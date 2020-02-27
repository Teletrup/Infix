import sys
from collections import deque

#	deque - struktura danych pozwalająca na dostęp do ostatniego
# 	elementu w czasie O(1) zamiast O(n) jak w przypadku listy


class Token:
	def __init__(self, name, order):
		self.name = name
		self.order = order
	def print(self):
		print(self.name, self.order)


order_num = 3


def lex(code):
	tokens = []
	order_base = 0
	for c in code:
		if c == '(':
			order_base += order_num
		elif c == ')':
			order_base -= order_num
		elif c == '+':
			tokens.append(Token('+', order_base + 0))
		elif c == '-':                             
			tokens.append(Token('-', order_base + 0))
		elif c == '*':                             
			tokens.append(Token('*', order_base + 1))
		elif c == '/':                             
			tokens.append(Token('/', order_base + 1))
		elif c != ' ':
			tokens.append(Token(c, order_base + order_num - 1))
	return tokens

def parse(tokens):
	expr = []
	stack = deque()
	for t in tokens:
		while stack and stack[-1].order >= t.order:
			expr.append(stack.pop())
		stack.append(t)
	while stack:
		expr.append(stack.pop())
	return expr


if len(sys.argv) != 2:
	exit("bad input")
tokens = lex(sys.argv[1])
expr = parse(tokens)
for t in expr:
	sys.stdout.write(t.name)
print()

