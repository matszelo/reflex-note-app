import reflex as rx
from .model import NoteEntryModel
from sqlmodel import select
from typing import List

class NoteState(rx.State):
    form_data: dict = {}
    notes: List['NoteEntryModel'] = []

    def submit(self, form_data: dict):
        self.form_data = form_data
        data = {}
        for k,v in form_data.items():
            if v == "" or v is None:
                continue
            data[k] = v   
        with rx.session() as session:
            db_entry = NoteEntryModel(
                **form_data
            )
            session.add(db_entry)
            session.commit()
        return rx.redirect("/")

    def list_notes(self):
        with rx.session() as session:
            notes = session.exec(
                select(NoteEntryModel)
            ).all()
            self.notes = notes
            
                