from app import db

# db.create_all()

from app import Db_Content
# try:
#     item = Db_Content(name="UrlShort", content="Hello everyone", time="15:41:00")
#     db.session.add(item)
#     db.session.commit()
# except:
#     pass
# db.drop_all()
x = Db_Content.query.all()
for i in x:
    print(i.name)
    print(i.content)
    print(i.time)