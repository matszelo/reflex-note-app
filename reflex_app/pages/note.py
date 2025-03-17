import reflex as rx
from ..UI.base import base
from .. import navigation

def Note_page() -> rx.Component:
    my_child = rx.flex(
            rx.box(
                rx.heading("Edit note", size="7"),      
            ),
            direction="column",
            width="100%",
        )           
    return base(my_child)