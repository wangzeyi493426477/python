import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['text']
collction = db['student']
student = {
    'age':21,
    'number':3
}
collction.insert_one(student)
