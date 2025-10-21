from database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Text
from sqlalchemy.orm import relationship


class VocabularyPill(Base):
    __tablename__ = 'vocubularyPills'
    
    id = Column(Integer,primary_key=True,index=True)
    word = Column(String(255))
    word_meaning = Column(Text)
    word_examples = Column(Text) 
