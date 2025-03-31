import reflex as rx
from .model import NoteEntryModel
from sqlmodel import select
from typing import List, Optional
from .. import navigation

class NoteState(rx.State):
    form_data: dict = {}
    notes: List['NoteEntryModel'] = []
    note: Optional['NoteEntryModel'] = None

    @rx.var
    def note_detail_id(self) -> str:
        return self.router.page.params.get("note_id", "")
    
    def get_note_detail(self):
        with rx.session() as session:
            if self.note_detail_id == "":
                self.note = None
                return
            result = session.exec(
                select(NoteEntryModel).where(
                    NoteEntryModel.id == self.note_detail_id
                )
            ).one_or_none()
            self.note = result

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
            return rx.redirect(navigation.routes.HOME_ROUTE)

    def list_notes(self):
        with rx.session() as session:
            entries = session.exec(
                select(NoteEntryModel)
            ).all()
            self.notes = entries           

class EditNoteState(rx.State):
    
    def submit(self, form_data):
        print(form_data)