from helper import counter
from linked_list import LinkedList, pad_to_equal_length, map_list, length, ListNode, print_list, shift_list, create_linked_list_callback, LinkedListIterator

def add_digit_by_digit(a, b):
  carry = 0
  result = ''
  for x, y in reversed(list(zip(a, b))):
    subtotal = int(x) + int(y) + carry
    carry = 0
    subtotal_str = str(subtotal)
    if subtotal > 9:
      carry = int(subtotal_str[0])
      result += subtotal_str[1]
    else:
      result += subtotal_str[0]
    
  result_str = ''.join(list(reversed(result)))
  return str(carry) + result_str  if carry else result_str

def equalize_lengths(l, l2):
  l_length = length(l)
  l2_length = length(l2)

  if l_length > l2_length:
    l2 = pad_to_equal_length(l_length, l2)
  elif l2_length > l_length:
    l = pad_to_equal_length(l2_length, l)
  
  return [l, l2]

def pad_leading_zeroes(n, s):
  l = ['0' for i in range(n)]
  return ''.join(l) + s

def pad_list_node(n):
  if n == None:
    return
  zeroes = 4 - len(n.value)
  n.value = pad_leading_zeroes(zeroes, n.value)

slice_for_linked_list = lambda l: [l[i: i + 4] for i in range(0, len(l), 4)]

def add_huge_numbers(ll, ll2):
  ll, ll2 = equalize_lengths(ll, ll2)
  map_list(pad_list_node, ll)
  map_list(pad_list_node, ll2)
  result = [add_digit_by_digit(n.value, n2.value) for n, n2 in zip(LinkedListIterator(ll), LinkedListIterator(ll2))]
  chunks = [''.join(l) for l in slice_for_linked_list(list(''.join(result)))]
  return LinkedList.fromList(chunks)

