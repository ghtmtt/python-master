import os

path = os.path.realpath(__file__)
print(path)

dirpath = os.path.dirname(__file__)
print(dirpath)

data_path = os.path.join(
    os.path.dirname(__file__),
    'data.csv'
)

print(data_path)

print(os.path.split(os.path.dirname(__file__)))