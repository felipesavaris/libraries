from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.domain.models import User, table_registry


def test_model_create_user():
    engine = create_engine('sqlite:///database.db')
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(name='Felps', email='felps@sava.com', password='123')

        session.add(user)
        session.commit()

    assert user.name == 'Felps'
