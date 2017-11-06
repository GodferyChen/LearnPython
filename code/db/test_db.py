from bson import ObjectId
from pymongo import MongoClient

# 连接数据库
conn = MongoClient('localhost', 27017)
db = conn.baikedb

# 新增
db.col.insert({'url': 'http://baike.com/测试', 'title': '测试', 'summary': '测试测试测试'})

# 新增多条记录
db.col.insert([
    {"name": 'yanying', 'province': '江苏', 'age': 25},
    {"name": '张三', 'province': '浙江', 'age': 24},
    {"name": '张三1', 'province': '浙江1', 'age': 25},
    {"name": '张三2', 'province': '浙江2', 'age': 26},
    {"name": '张三3', 'province': '浙江3', 'age': 28},
])

# 查询一条
db.col.find_one()

# 查询所有
db.col.find()

# 统计查询
db.col.find().count()

# 结果排序
db.col.find().sort("age")

# 条件查询
db.col.find({'name': "yanying"})

# 根据_id查询记录
db.col.find_one({'_id': ObjectId('592550e5d92fac0b8c449f87')})

# 更新
db.col.update({'_id': ObjectId('59255118d92fac43dcb1999a')}, {'$set': {'name': '王二麻33333'}})

# 删除
db.col.remove({'name': '王二麻33333'})
# 删除所有
db.col.remove()
