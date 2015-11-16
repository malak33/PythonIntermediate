from sqlalchemy import *
from sqlalchemy.orm import mapper, sessionmaker
class School(object):
    pass

db = create_engine('sqlite:///schools.db')
# db.echo = True
metadata = MetaData(db)

SchoolTable = Table('schools', metadata, autoload=True)
accountsmapper = mapper(School, SchoolTable)

Session = sessionmaker(autoflush=True, autocommit=True)
session = Session()
firstSchool = session.query(School).first()
print(firstSchool.fullname, firstSchool.country)
firstSchool.country = 'U.S.'
session.flush()
session.close()
session = Session()
school = session.query(School).first()
print(school.fullname, school.country)
