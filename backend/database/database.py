from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time

# Allow environment variable override for database URL
SQLALCHEMY_DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "sqlite:///./skillsprint.db"
)

# Performance optimizations for the SQLAlchemy engine
# For SQLite, we need different configuration
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False}  # SQLite specific
    )
else:
    # PostgreSQL configuration
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_pre_ping=True,      # Verify connections before using them
        pool_size=10,            # Connection pool size
        max_overflow=20,         # Max number of connections to create above pool_size
        pool_recycle=1800,       # Recycle connections after 30 minutes
    )

# Configure session with optimized settings
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# Connection retry decorator
def with_retry(max_retries=3, retry_delay=0.5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    if retries >= max_retries:
                        raise
                    print(f"Database operation failed, retrying ({retries}/{max_retries}): {e}")
                    time.sleep(retry_delay)
        return wrapper
    return decorator

# Dependency to get DB session with automatic retry
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
