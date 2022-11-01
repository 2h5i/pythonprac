from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.rmhhmma.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

movie = db.movies.find_one({'title':'가버나움'})
print(movie['star'])

movies = list(db.movies.find({'star': movie['star']},{'_id':False}))
for movie1 in movies:
    print(movie1['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})