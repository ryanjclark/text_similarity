from pydantic import BaseModel


class SimilarityScore(BaseModel):
    score: float
