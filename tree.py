import os

def print_tree(startpath, indent='  '):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        lead = indent * level
        print(f'{lead}{os.path.basename(root)}/')
        for f in files:
            print(f'{lead}{indent}{f}')

print_tree('.')