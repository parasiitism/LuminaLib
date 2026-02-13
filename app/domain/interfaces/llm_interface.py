from abc import ABC, abstractmethod


class LLMInterface(ABC):
    @abstractmethod
    async def generate_summary(self, text: str) -> str:
        pass

    @abstractmethod
    async def analyze_reviews(self, reviews: list[str]) -> str:
        pass
