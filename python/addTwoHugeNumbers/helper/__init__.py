def counted(f):
  def wrapper(*args, **kwargs):
    wrapper.calls += 1
    return f(*args, **kwargs)
  wrapper.calls = 0
  return wrapper

def counter():
  count = 0
  def add(*args):
    nonlocal count
    count += 1
    return count
  def get():
    return count
  return [get, add]