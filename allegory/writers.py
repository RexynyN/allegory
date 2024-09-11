import zipfile
import os 
from os.path import join as join_path
from typing import ABC, abstractmethod, Optional

class Writer(ABC):
    @abstractmethod
    def read(self) -> str:
        raise NotImplementedError('To be overridden!')

    @abstractmethod
    def write(self, data: str) -> None:
        raise NotImplementedError('To be overridden!')
    
    @abstractmethod
    def close(self) -> None:
        raise NotImplementedError('To be overridden!')

class CbzWriter(Writer):
    pass

class EpubWriter(Writer):
    pass

class PdfWriter(Writer):
    pass

class DocxWriter(Writer):
    pass

class MarkDownWriter(Writer):
    pass

class MobiWriter(Writer):
    pass

class Azw3Writer(Writer):
    pass

class HtmlWriter(Writer):
    pass

class TxtWriter(Writer):
    pass

class OdtWriter(Writer):
    pass

