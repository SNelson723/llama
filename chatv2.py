from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

base_url = "http://localhost:11434"
model = 'llama3.2:latest'

system_message = "You are a helpful assistant."

llm = ChatOllama(base_url=base_url, model=model, temparature = 0.9)

def process_chat(question, history):
  print(f"History: {history}")
  messages = [{"role": "system", "content": system_message}]
  
  for human, assistant in history:
    messages.append({"role": "user", "content": human})
    messages.append({"role": "assistant", "content": assistant})
    
  messages.append({"role": "user", "content": question})
  template = ChatPromptTemplate.from_messages(messages)
  
  chain = template | llm 
  response = chain.invoke({"prompt": messages})
  print(response)
  messages.append({"role": "assistant", "content": response.content})
  
  pairs = []
  for i in range(0, len(messages) - 1):
    if messages[i]["role"] == "user" and messages[i + 1]["role"] == "assistant":
      pairs.append([messages[i]["content"], messages[i + 1]["content"]])
  return pairs
  
  

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