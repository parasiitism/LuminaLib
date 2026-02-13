from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.domain.models import User
from app.infrastructure.llm.mock_llm import MockLLM
from app.infrastructure.llm.ollama_client import OllamaClient
from app.infrastructure.storage.local_storage import LocalStorage

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_storage():
    if settings.STORAGE_PROVIDER == "local":
        return LocalStorage()
    raise ValueError("Invalid storage provider")


def get_llm():
    if settings.LLM_PROVIDER == "mock":
        return MockLLM()
    if settings.LLM_PROVIDER == "ollama":
        return OllamaClient()
    raise ValueError("Invalid LLM provider")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise Exception("Invalid token")

    except JWTError:
        raise Exception("Invalid token")

    user = await db.get(User, user_id)
    if user is None:
        raise Exception("User not found")

    return user
