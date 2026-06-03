import abc

from pydantic import BaseModel

from src.data_preparation.text_cleaning import TextProcessor
from src.schemas.type_models import SourceDocument


class ProcessingStep(abc.ABC):

    @abc.abstractmethod
    def process(self):
        """Uses Processor on the data, and passes on the result"""


class TextToEmbeddingsProcessingStep(ProcessingStep, BaseModel):

    id_: int
    data: SourceDocument
    processor: TextProcessor
