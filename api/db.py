import sqlite3

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

db_path = './db.db'

def create():
  print("Creating")
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  c.execute('''
            create table if not exists orders(
              id integer primary key autoincrement,
              name text not null,
              price real not null,
              cost real not null,
              quantity int
            )
            ''')
  conn.commit()
  
  conn.close()
  
def seed():
  print("Seeding")
  conn = sqlite3.connect(db_path)
  products = [
    ('apples', 1.25, .99, 25),
    ('bananas', .75, .50, 12),
    ('burgers', 3.99, 2.99, 8),
    ('hamburger buns', 3.25, 2.99, 6),
    ('lettuce', .99, .79, 3),
    ('ketchup', 3.29, 2.99, 6),
    ('mustard', 2.99, 2.79, 4),
    ('hot dogs', 4.59, 3.99, 6),
    ('hot dog buns', 2.75, 1.99, 6),
    ('pickles', 1.25, .99, 3)
  ]
  
  c = conn.cursor()
  c.executemany('insert into orders (name, price, cost, quantity) VALUES (?,?,?,?)', products)
  conn.commit()
  conn.close()

def run():
  print(f"{GREEN}Enter command:{RESET}")
  while True:
    user_input = input(">: ")
    if user_input.lower() == "bye":
      print(f"{GREEN}Have a nice dat{RESET}")
      break
    elif user_input.lower() == "create":
      create()
    elif user_input.lower() == "seed":
      seed()
  
  
if __name__ == "__main__":
  run()