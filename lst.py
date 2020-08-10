import random

def to_str(*lst):
	print(list(map(str, *lst)))

int_lst = []
for _ in range(10):
	int_lst.append(random.randint(0,20))

to_str(int_lst)