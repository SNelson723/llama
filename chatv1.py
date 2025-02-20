from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

base_url = 'http://localhost:11434/v1'
model = 'llama3.2:latest'

client = OpenAI(
  base_url = base_url,
  api_key = 'llama', 
)

# system_message = "You are a helpful assistant."
system_message = "You are an advanced Grocery Business expert. You can help manage profit margins and analyze prices for the maximized profitability."

def process_chat(question, history):
  print(f"history: {history}")
  messages = [{"role": "system", "content": system_message}]
  for human, assistant in history:
    messages.append({"role": "user", "content": human})
    messages.append({"role": "assistant", "content": assistant})
    
  messages.append({"role": "user", "content": question})
  
  print(f"messages: {messages}")
  response = client.chat.completions.create(
    model = model,
    messages = messages
  )
  
  print(response)
  messages.append({"role": "assistant", "content": response.choices[0].message.content})
  
  pairs = []
  for i in range(0, len(messages) - 1):
    if messages[i]["role"] == "user" and messages[i + 1]["role"] == "assistant":
      pairs.append([messages[i]["content"], messages[i + 1]["content"]])
      
  return pairs

def chatbot(history):
  print("Hello bitches, your chatbot awaits 😎")
  while True:
    user_input = input("You: ")
    if (user_input.lower() == "bye"):
      print("have a nice day, we are out!!!!!")
      break
    
    history = process_chat(user_input, history)
    
if __name__ == "__main__":
  chatbot([])