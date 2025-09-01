from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

def get_user_by_id(db: Session, user_id: int):
    from ..models.user import User
    try:
        return db.query(User).filter(User.id == user_id).one()
    except NoResultFound:
        return None

def create_user(db: Session, user):
    from ..models.user import User
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_item_by_id(db: Session, item_id: int):
    from ..models.item import Item
    try:
        return db.query(Item).filter(Item.id == item_id).one()
    except NoResultFound:
        return None

def create_item(db: Session, item):
    from ..models.item import Item
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_all_items(db: Session):
    from ..models.item import Item
    return db.query(Item).all()