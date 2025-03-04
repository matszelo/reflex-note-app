import reflex as rx

from .navbar import navbar

def base(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.container(
        navbar(),
        child,
    )