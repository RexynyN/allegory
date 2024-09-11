import zipfile
import os 
from os.path import join as join_path
from typing import ABC, abstractmethod, Optional



class Reader(ABC):
    @abstractmethod
    def read(self) -> str:
        raise NotImplementedError('To be overridden!')

    @abstractmethod
    def write(self, data: str) -> None:
        raise NotImplementedError('To be overridden!')
    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError('To be overridden!')

class CbzReader(ABC):
    pass

class EpubReader(ABC):
    pass

class PdfReader(ABC):
    pass

class DocxReader(ABC):
    pass

class MarkDownReader(ABC):
    pass

class MobiReader(ABC):
    pass

class Azw3Reader(ABC):
    pass

class HtmlReader(ABC):
    pass

class TxtReader(ABC):
    pass

class OdtReader(ABC):
    pass

