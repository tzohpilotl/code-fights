from helper import counter
from linked_list import print_list, LinkedList, pad_to_equal_length, map_list, length, ListNode, shift_list, create_linked_list_callback, LinkedListIterator

def add_digit_by_digit(a, b):
  carry = 0
  result = ''
  print("a", a, "b", b)
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

def prepare_value(n): 
  n.value = str(n.value)
  pad_list_node(n)
  return n.value

preapare_and_add = lambda n, n2: add_digit_by_digit(prepare_value(n), prepare_value(n2))

def add_huge_numbers(ll, ll2):
  ll, ll2 = equalize_lengths(ll, ll2)
  zipped_lls = zip(LinkedListIterator(ll), LinkedListIterator(ll2))
  result = [preapare_and_add(n, n2) for n, n2 in zipped_lls]
  print("result", result)
  lists_of_4 = slice_for_linked_list(list(''.join(result)))
  chunks = [int(''.join(l)) for l in lists_of_4]
  return LinkedList.fromList(chunks)
