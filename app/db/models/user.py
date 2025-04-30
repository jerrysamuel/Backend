# app/db/models/user.py
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates
from app.db.base_class import Base
import uuid

class User(Base):
    """Base user model for all user types."""
    __tablename__ = "users"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    email = Column(String, unique=True, nullable=False, index=True)
    is_verified = Column(Boolean, default=False)
    role = Column(String, nullable=False, default="reply_guy")  # Discriminator

    # Employer-specific fields (nullable for ReplyGuy)
    project_name = Column(String, nullable=True)

    # ReplyGuy-specific fields (nullable for Employer)
    
    badges = Column(list, nullable=True)

    __table_args__ = (
        Index("ix_users_role", "role"),  # Index for role-based queries
    )

    @validates("role")
    def validate_role(self, key: str, value: str) -> str:
        """Validate role values."""
        valid_roles = {"employer", "reply_guy"}
        if value not in valid_roles:
            raise ValueError(f"Role must be one of {valid_roles}")
        return value

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"


class Employer(User):
    """Employer-specific logic and validation."""
    def __init__(self, **kwargs):
        super().__init__(role="employer", **kwargs)

    @validates("company_name")
    def validate_company_name(self, key: str, value: Optional[str]) -> Optional[str]:
        """Ensure company_name is provided for employers."""
        if self.role == "employer" and not value:
            raise ValueError("Company name is required for employers")
        return value


class ReplyGuy(User):
    """ReplyGuy-specific logic and validation."""
    def __init__(self, **kwargs):
        super().__init__(role="reply_guy", **kwargs)

    @validates("badges")
    def validate_expertise(self, key: list, value: Optional[list]) -> Optional[str]:
        """Ensure expertise is provided for reply guys."""
        if self.role == "reply_guy" and not value:
            raise ValueError("Badges is required for reply guys")
        return value
    
    