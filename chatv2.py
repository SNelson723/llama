from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools.math import add, multiply
from tools.trick import trick

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

load_dotenv()

base_url = "http://localhost:11434"
model = 'llama3.2:latest'

system_message = "You are a helpful assistant."

llm = ChatOllama(base_url=base_url, model=model)

tools = [trick, add, multiply]
list_of_tools = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools = tools)

def process_chat(question, history):
  print(f"History: {history}")
  messages = [{"role": "system", "content": system_message}]
  
  for human, assistant in history:
    messages.append({"role": "user", "content": human})
    messages.append({"role": "assistant", "content": assistant})
    
  messages.append({"role": "user", "content": question})
  
  # template = ChatPromptTemplate.from_messages(messages)
  # chain = template | llm 
  # response = chain.invoke({"prompt": messages})
  
  response = llm_with_tools.invoke(messages)
  print(response)
  
  # check for tool calls
  if len(response.tool_calls) > 0:
    for tool_call in response.tool_calls:
      result, tool_message = handle_tool_call(tool_call, messages)
      messages.append(result)
      print(f"response:{GREEN}tadAIr {tool_message.content}{RESET}")
  else:
    messages.append({"role": "assistant", "content": response.content})
    print(f"{GREEN}tadAIr {response.content}{RESET}")
      
  pairs = []
  for i in range(0, len(messages) - 1):
    if messages[i]["role"] == "user" and messages[i + 1]["role"] == "assistant":
      pairs.append([messages[i]["content"], messages[i + 1]["content"]])
  return pairs
  
  
def handle_tool_call(tool_call, messages):
  print("--------------------------------")
  print(f"tool call: {tool_call}")
  tool_name = tool_call["name"]
  print(f"tool_name: {tool_name}")
  selected_tool = list_of_tools[tool_name.lower()]
  print(f"Selected Tool: {selected_tool}")
  if tool_name == "trick":
    print("Using trick")
    tool_message = llm.invoke(messages)
  else:
    print("not using trick")
    tool_message = selected_tool.invoke(tool_call['args'])
    
  print(f"Tool Message: {tool_message}")
  result = {"role": "assistant", "content": tool_message.content}
  return result, tool_message
  


def chatbot(history):
  print("Helloo peeps, are you ready to chat? 😎")
  while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
      print("Have a nice day")
      break
  
    history = process_chat(user_input, history)

if __name__ == "__main__":
  chatbot([])