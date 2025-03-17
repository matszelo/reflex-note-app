import reflex as rx
from. import routes

class NavState(rx.State):
    
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    def to_about(self):
        return rx.redirect(routes.ABOUT_ROUTE)
    def to_note(self):
        return rx.redirect(routes.NOTE_ROUTE)