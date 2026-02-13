from abc import ABC, abstractmethod
from typing import BinaryIO


class StorageInterface(ABC):
    @abstractmethod
    async def save_file(self, file: BinaryIO, filename: str) -> str:
        pass

    @abstractmethod
    async def delete_file(self, path: str) -> None:
        pass
