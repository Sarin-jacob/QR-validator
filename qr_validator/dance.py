from time import sleep
from os import system
# print('\n')
def do():
  system("")
  a=[]
  a.append('''
            oooooo
          oooooooooo
        oo[]oooo[]oo  │
        oooo\__/oooo  │
          oooooooooo   │
            │    │     │
      ┌─────┤    ├─────┘
      │     │    │
      │     │    │
      │     └┬──┬┘
            │  │
            ▼  ▼

  ''')
  a.append('''
            oooooo
          oooooooooo
        oo[]oooo[]oo
  ────┐ oooo\__/oooo  ┌────
      │  oooooooooo   │
      │    │    │     │
      └────┤    ├─────┘
            │    │
            │    │
            └┬──┬┘
            │  │
            ▼  ▼

  ''')
  a.append('''
            oooooo
          oooooooooo
        oo[]oooo--oo
  │     oooo\__/oooo      │
  └───┐  oooooooooo  ┌────┘
      │    │    │    │
      └────┤    ├────┘
            │    │
            │    │
            └┬──┬┘
            │  │
            ▼  ▼

  ''')
  a.append('''
            oooooo
          oooooooooo
        oo[]oooo--oo
  ────┐ oooo\__/oooo  ┌────
      │  oooooooooo   │
      │    │    │     │
      └────┤    ├─────┘
            │    │
            │    │
            └┬──┬┘
            │  │
            ▼  ▼

  ''')
  a.append('''
            oooooo
          oooooooooo
        oo--oooo[]oo
  ────┐ oooo\__/oooo  ┌────
      │  oooooooooo   │
      │    │    │     │
      └────┤    ├─────┘
            │    │
            │    │
            └┬──┬┘
            │  │
            ▼  ▼

  ''')
  a.append('''
            oooooo
          oooooooooo
        oo[]oooo[]oo
      │ oooo\__/oooo
      │  oooooooooo
      │   │    │
      └───┤    ├────┐
          │    │    │
          │    │    │
          └┬──┬┘    │
            │  │
            ▼  ▼

  ''')
  for i in range(5):
      for i in a:
          print(i,end="\033[F"*13)
          sleep(0.3)    
          print('''
                                                                                  
                                                                                
                                                                                
                                                                                
                                                                                    
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
  ''',end="\033[F"*16)

  print('\n','                          \n'*6)
  print("\033[F"*9)

