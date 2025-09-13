import reflex as rx


def about_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Who We Are",
                class_name="text-4xl md:text-5xl font-bold text-[#fefadc] mb-8 text-center",
            ),
            rx.el.p(
                "We are a team of passionate innovators, dedicated to crafting cutting-edge cloud solutions. Our expertise lies in transforming complex challenges into simple, effective, and elegant digital experiences. We believe in the power of technology to drive progress and are constantly exploring new frontiers to stay ahead of the curve.",
                class_name="text-lg text-[#d3d3d3] max-w-3xl mx-auto text-center leading-relaxed",
            ),
            class_name="py-20 px-4 max-w-7xl mx-auto",
        ),
        id="about",
        class_name="w-full",
    )