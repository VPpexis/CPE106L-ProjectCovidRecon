import dataset

<<<<<<< HEAD
db = dataset.connect("sqlite:///tweets.db")
=======
db = dataset.connect("sqlite:///tweets-2.db")
>>>>>>> 6b42f9c5980a22d5bd520d4382b39df79a5bf087
result = db['myTable'].all()
dataset.freeze(result, format='csv', filename='tweets.csv')
