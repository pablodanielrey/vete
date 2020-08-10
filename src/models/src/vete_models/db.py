import inject
import contextlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import Config

class Engine:
    @inject.autoparams()
    def __init__(self, config: Config):
        self.config = config
        self.engine = create_engine(f'postgresql://{self.config.dbuser}:{self.config.dbpassword}@{self.config.dbhost}:{self.config.dbport}/{self.config.dbname}', echo=False)

    def get(self):
        return self.engine

    def dispose(self):
        self.engine.dispose()


class Sessions:

    @inject.autoparams()
    def __init__(self, engine: Engine):
        self.engine = engine

    def generate_database(self):
        from vete_entities import Base
        engine = self.engine.get()
        try:
            Base.metadata.create_all(engine)
        finally:
            engine.dispose()

    @contextlib.contextmanager
    def get(self):
        Session = sessionmaker(bind=self.engine.get(), autoflush=False, autocommit=False, expire_on_commit=False)
        session = Session()
        try:
            yield session
        finally:
            # pylint: disable=no-member
            session.close()

    def __destroy__(self):
        self.engine.dispose()