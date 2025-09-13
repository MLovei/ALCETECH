import reflex as rx
from app.components.header import header
from app.components.hero import hero
from app.components.about import about_section
from app.components.services import services_section
from app.components.contact import contact_section
from app.components.footer import footer


def index() -> rx.Component:
    return rx.el.main(
        header(),
        hero(),
        about_section(),
        services_section(),
        contact_section(),
        footer(),
        class_name="font-['Montserrat'] bg-gradient-to-b from-[#2D2D2D] to-[#8D909B] min-h-screen",
    )


app = rx.App(
    theme=rx.theme(appearance="light", accent_color="orange", radius="small"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;700&display=swap",
        "/styles.css",
    ],
)
app.add_page(index, title="ALCETECH - Different. Effective. Curious.")