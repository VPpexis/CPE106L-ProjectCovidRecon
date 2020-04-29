import dataset

db = dataset.connect("sqlite:///tweets.db")
result = db['myTable'].all()
dataset.freeze(result, format='csv', filename='tweets.csv')
