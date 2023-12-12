from fastapi import FastAPI

from app.database import engine
from app.models import Base

# DBテーブル作成
Base.metadata.create_all(bind=engine)


app = FastAPI()


if __name__ == "__main__":
    # TODO: initialize tables
    pass