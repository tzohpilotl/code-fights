import math

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def addTwoHugeNumbers(a, b):
    full_a = ""
    full_b = ""
    while a != None or b != None:
        full_a += pad_leading_zeroes(str(a.value)) if a != None else ""
        full_b += pad_leading_zeroes(str(b.value)) if b != None else ""
        a = a.next if a != None else None
        b = b.next if b != None else None
    [full_a, full_b] = pad_full_zeroes(full_a, full_b)
    total = sum_right_to_left(full_a, full_b)
    [total, _] = pad_full_zeroes(total, "0" * len(total))

    root = None
    current = None
    tmp = ""
    for i, n in enumerate(total):
        if len(tmp) == 4:
            if root == None:
                root = ListNode(int(tmp))
                current = root
            else:
                current.next = ListNode(int(tmp))
                current = current.next
            tmp = ""
        tmp += n
    if root == None:
        root = ListNode(int(tmp))
        tmp = ""
    if len(tmp) > 0:
        current.next = ListNode(int(tmp))
    return root

def print_list(l):
    if l == None:
        return
    print(l.value)
    return print_list(l.next)    

def sum_right_to_left(a, b):
    if a == "":
        return pad_leading_zeroes(str(b))
    if b == "":
        return pad_leading_zeroes(str(a))
    A = [n for n in pad_leading_zeroes(str(a))]
    B = [n for n in pad_leading_zeroes(str(b))]
    print(A, B)
    carry = 0
    result = ""
    for _a, _b in zip(reversed(A), reversed(B)):
        addition = int(_a) + int(_b) + carry
        carry = 0
        with_decimal = addition / 10
        [integer, decimal] = str(with_decimal).split('.')
        carry = int(integer)
        result = decimal + result
    
    if carry > 0:
        result = str(carry) + result

    return result

def find_missing_zeroes(s):
    if len(s) %4 == 0:
        return 0
    else:
        div = math.ceil(len(s) /4)
        number = 4 * div
        return number - len(s)

def pad_full_zeroes(a, b):
    digits_delta = abs(len(a) - len(b))
    if len(a) < len(b):
        a = "0" * digits_delta + a
    else:
        b = "0" * digits_delta + b
    missing_zeroes = find_missing_zeroes(a)
    a = "0" * missing_zeroes + a
    b = "0" * missing_zeroes + b
    return [a, b]

def pad_leading_zeroes(number_str):
    digits = len(number_str)
    if digits == 0:
        return "0000"
    if digits == 1:
        return "000" + number_str
    if digits == 2:
        return "00" + number_str
    if digits == 3:
        return "0" + number_str
    return number_str