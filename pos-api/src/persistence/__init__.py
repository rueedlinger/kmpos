from fastapi.params import Depends
from typing_extensions import Annotated
from sqlmodel import SQLModel, Session, create_engine

print("Initializing persistence module...")

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    print("Creating database and tables...")
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

def get_session_deps():
    SessionDep = Annotated[Session, Depends(get_session)]
    return SessionDep
