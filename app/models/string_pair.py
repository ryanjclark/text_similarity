from pydantic import BaseModel


class StringPair(BaseModel):
    doc_1: str
    doc_2: str
