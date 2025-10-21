from pydantic import BaseModel

class VocabularyPill(BaseModel):
    word : str
    word_meaning : str
    word_examples : str

class ShowVocabularyPill(BaseModel):
    word : str
    word_meaning : str
    word_examples : str
    class Config():
        from_attributes = True