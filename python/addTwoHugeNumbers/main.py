from linked_list import LinkedList, print_list
from add_huge_numbers import add_huge_numbers

if __name__ == '__main__':
  ll = LinkedList.fromList(['999'])
  ll2 = LinkedList.fromList(['0', '0', '1'])
  print_list(add_huge_numbers(ll, ll2))
