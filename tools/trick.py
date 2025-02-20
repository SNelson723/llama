from langchain_core.tools import tool

@tool
def trick(question):
  """
    This is a trick function to handle the eagerness of ollama models 
    to want to just call tools for no reason even when the user types
    something that has nothing to do with any other existing tools.
    
  Args:
      question (str): the users question to ask the llm
  Returns: str
  """
  print(f"Running trick tool with question: {question}")
  return question