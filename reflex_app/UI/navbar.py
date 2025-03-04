import reflex as rx

def navbar() -> rx.Component:
    return rx.container(
        rx.flex(
            rx.avatar(fallback="RX", color_scheme="orange"),
            rx.heading("App name", size="8"),
            spacing="2",
        )    
    )