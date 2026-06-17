from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password
from app.core.exceptions import UserAlreadyExistsException

def get_user_by_email(db:Session, email:str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db:Session, user_id:int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def create_user(db:Session, user_data:UserCreate) -> User:
    """
    Creates a new user.
    Raises UserAlreadyExistsException if email is taken.
    Hashes the password before storing.
    """
    existing_user = get_user_by_email(db, user_data.email)

    if existing_user:
        raise UserAlreadyExistsException

    new_user = User(
        email = user_data.email,
        hashed_password = hashed_password(user_data.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db:Session, email:str, password:str) -> User:
    """
    Verifies email and password combination.
    Returns the user if credentials are valid, None otherwise.
    Note: Returns None rather than raising an exception deliberately.
    The endpoint layer decides what error to surface.
    """
    user = get_user_by_email(db, email=email)

    if not user:
        verify_password(password, "wjqkdncncmm1kk2k3j3j49494i4ynvnfcn110faketoken")
    
    if not verify_password(password, user.hashed_password):
        return None
    return user
