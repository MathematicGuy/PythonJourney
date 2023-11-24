import os

current_dir = os.path.dirname(__file__)
print(current_dir)
with open(os.path.join(current_dir, 'help.txt'), 'r', encoding='utf-8') as f:
    print(f.read())
