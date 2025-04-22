import reflex as rx
from .model import NoteEntryModel
from sqlmodel import select
from typing import List, Optional
from .. import navigation

class NoteState(rx.State):
    form_data: dict = {}
    notes: List['NoteEntryModel'] = []
    note: Optional['NoteEntryModel'] = None
    note_text: str = ""
 

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
            self.note_text = self.note.text

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

    def delete(self):
        with rx.session() as session:
            if self.note_detail_id == "":
                self.note = None
                return
            note = session.exec(
                select(NoteEntryModel).where(
                    NoteEntryModel.id == self.note_detail_id
                )
            ).one_or_none()
            self.note = note
            session.delete(note)
            session.commit()   
            return rx.redirect(navigation.routes.HOME_ROUTE)
         
        
    def save_note_edits(self, note_id:int, updated_data:dict):
        with rx.session() as session:
            note = session.exec(
                select(NoteEntryModel).where(
                    NoteEntryModel.id == note_id
                )
            ).one_or_none()
            if note is None:
                return
            for key, value in updated_data.items():
                setattr(note, key, value)
            session.add(note)
            session.commit()
            session.refresh(note)
            self.note = note

    def to_note_page(self):
        if not self.note:
            return rx.redirect("/note")
        return rx.redirect(f"/note/{self.note.id}")


    def list_notes(self):
        with rx.session() as session:
            entries = session.exec(
                select(NoteEntryModel)
            ).all()
            self.notes = entries           

class EditNoteState(NoteState):
    note_form_data: dict = {}

    def handle_submit(self, note_form_data):
        self.note_form_data = note_form_data
        updated_data = {**note_form_data}
        note_id = note_form_data.pop("note_id")
        self.save_note_edits(note_id, updated_data)
        return self.to_note_page()
