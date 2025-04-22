import reflex as rx

from .state import NoteState

def note_form() -> rx.Component:
    return rx.form(
        rx.flex(
            rx.input(
                placeholder="Title",
                name="title",
                required=True,
            ),
            rx.text_area(
                placeholder="Text",
                name="text",
                resize="vertical",
                height="200px"
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                rx.dialog.close(
                    rx.button(
                        "Submit", 
                        type="submit",
                        color_scheme="orange",
                        on_click=rx.toast.success("Note added successfully", duration=5000),
                    ),
                ),
                spacing="3",
                justify="end",
            ),
            direction="column",
            spacing="4",
        ),
        on_submit=NoteState.submit,
        reset_on_submit=True,
    ),