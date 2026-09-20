from datetime import datetime

from sqlalchemy import CheckConstraint, ForeignKey, String, Text, TIMESTAMP, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

from config import settings


engine = create_engine(settings.database_url, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    start_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now())
    end_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)

    tasks: Mapped[list["Task"]] = relationship("Task", back_populates="project", cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    priority: Mapped[str] = mapped_column(String(20), nullable=False)
    due_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)

    project: Mapped["Project"] = relationship("Project", back_populates="tasks")

    __table_args__ = (
        CheckConstraint("status IN ('active', 'completed', 'in_progress')", name="check_task_status"),
        CheckConstraint("priority IN ('low', 'medium', 'high', 'critical')", name="check_task_priority"),
    )


def create_tables(): Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()