"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from .UI.base import base


class State(rx.State):
    """The app state."""


def my_page() -> rx.Component:
    return base(
        rx.grid(
            rx.foreach(
                rx.Var.range(12),
                lambda i: rx.card(f"Card {i + 1}", height="10vh"),
            ),
            columns="3",
            spacing="4",
            width="100%",
        )
    )


app = rx.App()
app.add_page(my_page, route="/", title="Main site")
