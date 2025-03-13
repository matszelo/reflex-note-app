import reflex as rx

def navbar() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.center(
                    rx.avatar(fallback="No", color_scheme="orange",),
                    rx.link("Notes", size="8", href="/", underline="none", weight="bold", color_scheme="gray", high_contrast=True),
                    spacing="2",
            ),    
            rx.spacer(),
            rx.center(
                rx.link(
                    "About app",
                    href="/about",
                    color_scheme="gray",
                    underline="none",
                    weight="medium",
                    padding_top="10px"
                ),
            ),
        ),   
        margin_bottom="20px",
    )