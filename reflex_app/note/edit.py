import reflex as rx
from .state import EditNoteState

def edit_form() -> rx.Component:
    note = EditNoteState.note
    title = note.title
    note_text = EditNoteState.note_text
    return rx.form(
        rx.box(
            rx.input(
                type='hidden',
                name='note_id',
                value=note.id
            ),
            display='none'
        ),    
        rx.flex(
            rx.input(
                default_value=title,
                placeholder="Title",
                name="title",
                required=True,
            ),
            rx.text_area(
                value=note_text,
                on_change = EditNoteState.set_note_text,
                placeholder="Text",
                name="text",
                resize="vertical",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),    
                rx.alert_dialog.action(
                    rx.button(
                        "Submit", 
                        type="submit",
                        color_scheme="orange",
                        on_click=rx.toast.success(
                            "Note edited successfully", duration=5000
                        ),
                    ),
                ),    
            ),        
            direction="column",
            spacing="4",
        ),
        on_submit=EditNoteState.handle_submit,
    ),