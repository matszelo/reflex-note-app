"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


def my_page():
    return rx.container(
       rx.text("Root Page"),
    )


app = rx.App()
app.add_page(my_page, route="/")
