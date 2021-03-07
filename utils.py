import pandas as pd

# add label coloum to each row

fake = pd.read_csv("./data/FakeNews/Fake.csv")
real = pd.read_csv("./data/FakeNews/True.csv")

fake['label'] = [1]*fake.shape[0]
real['label'] = [0]*real.shape[0]

fake.to_csv("./data/FakeNews/Fake.csv")
real.to_csv("./data/FakeNews/True.csv")