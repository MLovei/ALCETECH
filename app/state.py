import reflex as rx


class State(rx.State):
    """The app state."""

    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data