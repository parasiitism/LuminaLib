from abc import ABC, abstractmethod
from uuid import UUID
from typing import List


class RecommenderInterface(ABC):
    @abstractmethod
    async def recommend(self, user_id: UUID) -> List[UUID]:
        pass
