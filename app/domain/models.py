import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: str = Column(String, unique=True, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow)

    borrows = relationship("Borrow", back_populates="user")
    reviews = relationship("Review", back_populates="user")


class Book(Base):
    __tablename__ = "books"

    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title: str = Column(String, nullable=False)
    author: str = Column(String, nullable=False)
    file_path: str = Column(String, nullable=False)

    summary: Optional[str] = Column(Text, nullable=True)
    review_consensus: Optional[str] = Column(Text, nullable=True)

    created_at: datetime = Column(DateTime, default=datetime.utcnow)

    borrows = relationship("Borrow", back_populates="book")
    reviews = relationship("Review", back_populates="book")


class Borrow(Base):
    __tablename__ = "borrows"

    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: uuid.UUID = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    book_id: uuid.UUID = Column(UUID(as_uuid=True), ForeignKey("books.id"))

    borrowed_at: datetime = Column(DateTime, default=datetime.utcnow)
    returned_at: Optional[datetime] = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="borrows")
    book = relationship("Book", back_populates="borrows")


class Review(Base):
    __tablename__ = "reviews"

    id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: uuid.UUID = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    book_id: uuid.UUID = Column(UUID(as_uuid=True), ForeignKey("books.id"))

    rating: int = Column(Integer, nullable=False)
    comment: str = Column(Text, nullable=False)

    created_at: datetime = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reviews")
    book = relationship("Book", back_populates="reviews")
