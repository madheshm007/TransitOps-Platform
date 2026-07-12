from sqlalchemy.orm import Session

from app.core.security import verify_password, create_access_token
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from app.schemas.user import UserCreate, UserLogin


def register_user(db: Session, user: UserCreate):
    existing = get_user_by_email(db, user.email)

    if existing:
        raise ValueError("Email already registered")

    return create_user(db, user)


def login_user(db: Session, user: UserLogin):
    db_user = get_user_by_email(db, user.email)

    if not db_user:
        raise ValueError("Invalid email or password")

    if not verify_password(user.password, db_user.password_hash):
        raise ValueError("Invalid email or password")

    token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }