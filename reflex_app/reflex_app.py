"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from .UI.base import base

class note(rx.Model, table=True):
    title: str
    text: str

class FormState(rx.State):
    new_note: note = note()

    @rx.event
    def add_note_to_database(self, form_data: dict):
        """Handle the form submit."""
        self.new_note = form_data

def Main() -> rx.Component:
    return base(
        rx.flex(
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
            rx.box(    
                rx.grid(
                    rx.foreach(
                        rx.Var.range(4),
                        lambda i: rx.card(f"Card {i + 1}", height="10vh"),
                    ),
                    rows="2",
                    flow="column",
                    columns="2",
                    justify="between",
                    spacing="4",
                    width="100%",
                ),
            ),
            direction="column",
            width="100%",
        ),           
    )


app = rx.App()
app.add_page(Main, route="/", title="Main site")
