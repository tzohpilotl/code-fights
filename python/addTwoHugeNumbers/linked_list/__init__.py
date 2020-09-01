from helper import counter

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

class LinkedList():
  @classmethod
  def fromList(cls, l):
    if not l:
      return None
    root = ListNode(l[-1])
    for x in reversed(l[:-1]):
      root = shift_list(ListNode(x), root)
    return root

class LinkedListIterator():
  def __init__(self, root):
    super().__init__()
    self.root = root
    self.current = root

  def __iter__(self):
    return self

  def __next__(self):
    if self.current.next == None:
      raise StopIteration
    else:
      tmp = self.current
      self.current = self.current.next
      return self.current


def pad_to_equal_length(target_length, l):
  [get_count, count] = counter()
  map_list(create_linked_list_callback(count), l)

  if get_count() >= target_length:
    return l
  
  delta = target_length - get_count()

  longer_list = None

  for i in range(delta):
    longer_list = shift_list(ListNode('0'), longer_list)

  shift_list(last_of_list(longer_list), l)
  return longer_list

def create_linked_list_callback(f):
  return lambda l: f(l)

def last_of_list(l):
  if l == None:
    return None
  while l.next != None:
    l = l.next
  return l

def length(l):
  [get_count, count] = counter()
  map_list(count, l)
  return get_count()

def print_list(l):
  if l == None:
    print('List is empty')
  callback = create_linked_list_callback(lambda l: print(l.value))
  map_list(callback, l)

def shift_list(n, l):
  n.next = l
  return n

def map_list(fn, l):
  while l != None:
    create_linked_list_callback(fn)(l)
    l = l.next