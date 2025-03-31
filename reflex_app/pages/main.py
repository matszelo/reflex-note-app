import reflex as rx
from ..UI.base import base
from ..note import state, model
from .. import note, navigation

def note_detail_link(child: rx.Component, note: model.NoteEntryModel):
    if note is None:
        return rx.fragment(child)
    note_id = note.id
    if note_id is None:
        return rx.fragment(child)
    root_path = navigation.routes.NOTE_ROUTE
    note_detail_url = f"{root_path}/{note_id}"
    return rx.link(
        child,
        href=note_detail_url
    )        

def note_entry_list_item(note: model.NoteEntryModel) -> rx.Component:
    return note_detail_link(
        rx.card(
            rx.flex(
                rx.vstack(
                    rx.heading(note.title, size="4", underline="none", weight="bold", color_scheme="gray", high_contrast=True),
                    rx.text(note.text, size="2", underline="none", color_scheme="gray", high_contrast=True), 
                ),
            ),
            height="200px",       
        ),
        note,
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