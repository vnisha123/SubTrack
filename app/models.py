from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint,Date,DateTime,Numeric,func
from app.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    subs = relationship("Sub", back_populates="owner", cascade="all, delete-orphan")


class Sub(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    cost = Column(Numeric(10, 2), nullable=False)
    billing_cycle = Column(String, default="Monthly")
    next_billing_date = Column(Date, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"), nullable=False)
    owner = relationship("User", back_populates="subs")

    __table_args__ = (
        UniqueConstraint('user_id','service_name', name='_user_service_name_us'),
    )