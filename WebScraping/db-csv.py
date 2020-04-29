import dataset

db = dataset.connect("sqlite:///tweets-2.db")
result = db['myTable'].all()
dataset.freeze(result, format='csv', filename='tweets.csv')
