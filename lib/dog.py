from models import Dog
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///example.db')
session=sessionmaker(bind=engine)
session=session()

def create_table(base,engine):
    base.metadata.create_all(engine)    

def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    pass
    return session.query(Dog).all()

def find_by_name(session, name):
    pass

    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    pass

    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    
    
    return session.query(Dog).filter_by(name=name,breed=breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed=breed
    session.commit()
    

# new_dog=Dog(name='Kiplagit',breed='chihuahua')
# session.add(new_dog)
# session.commit()
# session.close()