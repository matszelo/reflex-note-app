import reflex as rx
from ..UI.base import base
from ..note import state, model
from .. import note, navigation

def note_entry_list_item(note: model.NoteEntryModel) -> rx.Component:
    return rx.card(
        rx.flex(
            rx.vstack(
                rx.text(note.title),
                rx.text(note.text, size="2"),
            ),    
        ),
        height="200px",
        on_click=navigation.NavState.to_note,
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
                rx.desktop_only(   
                    rx.grid(
                        rx.foreach(state.NoteState.notes, note_entry_list_item),
                        columns="2",
                        spacing="4",
                        width="100%", 
                    ),
                ),     
                rx.mobile_and_tablet(
                    rx.grid(
                        rx.foreach(state.NoteState.notes, note_entry_list_item),
                        columns="1",
                        spacing="4",
                        width="100%",
                    ), 
                ),    
            ),
            direction="column",
            width="100%",
        )
    return base(my_child)