from linked_list import LinkedList, print_list
from add_huge_numbers import add_huge_numbers

if __name__ == '__main__':
  ll = LinkedList.fromList([9876, 5432, 1999])
  ll2 = LinkedList.fromList([1, 8001])

  print_list(add_huge_numbers(ll, ll2))
