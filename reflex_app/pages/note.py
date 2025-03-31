import reflex as rx
from ..UI.base import base
from .. import navigation, note
from ..note import state

def Note_page() -> rx.Component:
    my_child = rx.vstack(
            rx.flex(
                rx.card(
                    rx.heading(state.NoteState.note.title, size="4", underline="none", weight="bold", color_scheme="gray", high_contrast=True),
                    rx.text(state.NoteState.note.text, size="2", underline="none", color_scheme="gray", high_contrast=True),         
                ),
            ),
        )           
    return base(my_child)