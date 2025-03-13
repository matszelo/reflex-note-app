import reflex as rx
from ..UI.base import base


def About_app_page() -> rx.Component:
    my_child = rx.flex(
            rx.box(
                rx.heading("About app", size="7"),      
            ),
            direction="column",
            width="100%",
        )           
    return base(my_child)