from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database import Base


class Ilmoitus(Base):
    __tablename__ = "ilmoitukset"

    id = Column(Integer, primary_key=True, index=True)
    nimi = Column(String, index = True)
    aika = Column(DateTime, default=datetime.now)