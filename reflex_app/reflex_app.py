"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from . import pages, note, navigation

app = rx.App()
app.add_page(pages.Main_page, route=navigation.routes.HOME_ROUTE, title="Main site", on_load=note.NoteState.list_notes)
app.add_page(pages.About_app_page, route=navigation.routes.ABOUT_ROUTE, title="About app")
app.add_page(pages.Note_page, route="/note/[note_id]", title="Note", on_load=note.NoteState.get_note_detail)