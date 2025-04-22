import reflex as rx
from ..UI.base import base
from .. import navigation, note
from ..note import state

def Note_page() -> rx.Component:
    my_form = note.edit_form()
    my_child = rx.flex(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.box(
                    rx.button(
                        rx.icon("notebook-pen"),
                        "Edit note",
                        color_scheme="orange",
                        size="4",
                        width="100%",
                        margin_bottom="18px",
                    ),
                ),
            ),
            rx.dialog.content(
                rx.dialog.title(
                    "Edit note",
                ),
                my_form
            ),
        ),
        rx.card(
            rx.flex(
                rx.vstack(
                    rx.heading(state.NoteState.note.title, size="6", underline="none", weight="bold", color_scheme="gray", high_contrast=True),    
                    rx.text(state.NoteState.note.text, size="3", underline="none", color_scheme="gray", high_contrast=True, white_space='pre-wrap'),         
                ),
            ),
            width="100%",
        ),
        direction="column",   
    ),          
    return base(my_child)