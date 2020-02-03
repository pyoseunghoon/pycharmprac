from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# db.users.insert_one({'name':'bobby','age':21})
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})

# user_one = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user_one)

# all_users = list(db.users.find({},{'_id':False}))
# print(all_users)
# for user in all_users :
#     if user['age'] <25 :
#         print(user)

db.users.update_many({},{'$set':{'age':19}})