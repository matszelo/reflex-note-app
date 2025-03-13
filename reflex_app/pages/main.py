import reflex as rx
from ..UI.base import base
from ..note import state, model
from .. import note

def note_entry_list_item(note: model.NoteEntryModel):
    return rx.box(
        rx.heading(note.title),
        rx.text(note.text),
        padding='1em'
    )

def Main_page() -> rx.Component:
    my_form = note.note_form()
    my_child = rx.flex(
            rx.alert_dialog.root(
                rx.alert_dialog.trigger(
                    rx.box(
                        rx.button(
                            rx.icon("notebook-pen"),
                            "New note",
                            color_scheme="orange",
                            size="4",
                            width="100%",
                            margin_bottom="18px",
                        ),
                    ),
                ),
                rx.alert_dialog.content(
                    rx.alert_dialog.title(
                        "Write new note",
                    ),
                    my_form
                ),
            ),
            rx.box(   
                rx.vstack(
                    rx.foreach(state.NoteState.notes, note_entry_list_item),
                )  
            ),
            direction="column",
            width="100%",
        )
    return base(my_child)