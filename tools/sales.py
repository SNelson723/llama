from langchain_core.tools import tool
import httpx
from collections import namedtuple

@tool
def sales_fetcher():
  '''
    Use this tool if you need to generate sales data for a users request
    This is will go out to FastAPI and grab some sales data
    There are no arguments for this tool
    Args:
    Returns: list of dictionaries
  '''
  
  try:
    print(f"Running sales fetcher bitches")
    response = httpx.get("http://127.0.0.1:3054/grocery/orders")
    print(f"Response: {response.json()['data']}")
    ToolMessage = namedtuple('ToolMessage', ['error', 'content'])
    tool_msg = ToolMessage(error=0, content=response.json()['data'])
    return tool_msg
  except ValueError as e:
    ToolMessage = namedtuple('ToolMessage', ['content'])
    tool_msg = ToolMessage(error=1, content=str(e))
    return tool_msg
  
    
    