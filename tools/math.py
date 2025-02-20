from langchain_core.tools import tool

@tool
def add(a, b):
  """
  Adds two numbers together
  Args:
    a (int): first number
    b (int): second number
  Returns: number
  """
  print(f"Running add with a: {a}, b: {b}")
  return a + b

@tool
def multiply(a, b):
  """
  Multiplies two numbers together
  Args:
    a (int): first number
    b (int): second number
  Returns: number
  """
  print(f"Running multiply with a: {a}, b: {b}")
  return a * b

