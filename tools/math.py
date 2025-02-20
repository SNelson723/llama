from langchain_core.tools import tool
from collections import namedtuple

# """ => is a doc comment that is needed for the tool functions

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
  result = a + b
  ToolMessage = namedtuple('ToolMessage', ['content'])
  tool_msg = ToolMessage(content=str(result))
  return tool_msg

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
  result = a * b
  ToolMessage = namedtuple('ToolMessage', ['content'])
  tool_msg = ToolMessage(content=str(result))
  return tool_msg

