from fastapi import APIRouter,Depends,status,Response
import schemas
import models
from sqlalchemy.orm import Session
from database import get_db
from typing import List

from repositary import VocabularyPillRepo

router = APIRouter(
    prefix = '/vocabpill',
    tags = ['VocabPill']
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.VocabularyPill,db:Session = Depends(get_db)):
    return VocabularyPillRepo.create(request,db)

@router.get('/',response_model=List[schemas.ShowVocabularyPill])
def all(response:Response,db:Session=Depends(get_db)):
    return VocabularyPillRepo.get_all(db)