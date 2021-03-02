from fastapi import APIRouter

from ..models.similarity_score import SimilarityScore
from ..models.string_pair import StringPair
from ..services.levenshtein import LevenshteinService

router = APIRouter(prefix="/api/v1", tags=["levenshtein"])


@router.post("/text-similarity", response_model=SimilarityScore)
async def get_similarity_score(pair: StringPair):
    score = LevenshteinService(pair).get_similarity_score()

    return score
