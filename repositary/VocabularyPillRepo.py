from fastapi import HTTPException , status ,Response
import schemas
import models
from sqlalchemy.orm import Session


def get_all(db:Session):
    vocabs = db.query(models.VocabularyPill).all()
    return vocabs

def create(request:schemas.VocabularyPill,db:Session):
    try:
        new_vocab = models.VocabularyPill(word = request.word , word_meaning = request.word_meaning,word_examples=request.word_examples)
        db.add(new_vocab)
        db.commit()
        db.refresh(new_vocab)
        return new_vocab
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=str(e))