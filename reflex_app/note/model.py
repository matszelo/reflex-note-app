import reflex as rx
from datetime import timezone, datetime
from sqlmodel import Field
import sqlalchemy

def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)

class NoteEntryModel(rx.Model, table=True):
    title: str 
    text: str | None = None
    #created_at: datetime = Field(
        #default_factory=get_utc_now,
        #sa_type=sqlalchemy.DateTime(timezone=True),
        #sa_column_kwargs={
            #'server_default': sqlalchemy.func.now()
        #},
        #nullable=False
    #) 