"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from . import pages
from . import note

app = rx.App()
app.add_page(pages.Main_page, route="/", title="Main site", on_load=note.NoteState.list_notes)
app.add_page(pages.About_app_page, route="/about", title="About app")
