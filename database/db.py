from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./database/ranking.db"

engine = create_engine(
    DATABASE_URL,
    # "sqlite:///./test.db",
    connect_args={
        "check_same_thread": False,
        "timeout": 10,
    }
)

with engine.connect() as conn:
    try:
        result = conn.execute(text("PRAGMA journal_mode=WAL;"))
        print("WAL mode:", result.fetchone())
    except Exception as e:
        print("WAL設定失敗（無視OK）:", e)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()