import reflex as rx
from .. import navigation

def navbar() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.center(
                    rx.avatar(fallback="No", color_scheme="orange",),
                    rx.link("Notes", href=navigation.routes.HOME_ROUTE , size="8", underline="none", weight="bold", color_scheme="gray", high_contrast=True),
                    spacing="2",
            ),    
            rx.spacer(),
            rx.center(
                rx.link(
                    "About app",
                    href=navigation.routes.ABOUT_ROUTE,
                    color_scheme="gray",
                    underline="none",
                    weight="medium",
                    padding_top="10px"
                ),
            ),
        ),   
        margin_bottom="20px",
    )