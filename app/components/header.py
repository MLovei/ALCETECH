import reflex as rx


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.el.span("ALCE", class_name="font-bold"),
                        rx.el.span("TECH", class_name="font-light"),
                        class_name="text-2xl text-[#fefadc] tracking-widest",
                    ),
                    href="/",
                ),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.el.a(
                    "HOME",
                    href="#",
                    class_name="text-[#fefadc] hover:text-[#f78000] transition-colors duration-300 px-3 py-2 rounded-sm font-medium",
                ),
                rx.el.a(
                    "SOLUTIONS",
                    href="#services",
                    class_name="text-[#fefadc] hover:text-[#f78000] transition-colors duration-300 px-3 py-2 rounded-sm font-medium",
                ),
                rx.el.a(
                    "NEWS",
                    href="#",
                    class_name="text-[#fefadc] hover:text-[#f78000] transition-colors duration-300 px-3 py-2 rounded-sm font-medium",
                ),
                rx.el.a(
                    "CONTACT",
                    href="#contact",
                    class_name="text-[#fefadc] hover:text-[#f78000] transition-colors duration-300 px-3 py-2 rounded-sm font-medium",
                ),
                class_name="hidden md:flex items-center gap-4",
            ),
            rx.el.a(
                "CUSTOMER LOGIN",
                href="#",
                class_name="hidden md:block border border-[#fefadc] text-[#fefadc] px-6 py-2 rounded-sm font-medium hover:bg-[#f78000] hover:border-[#f78000] transition-colors duration-300 shadow-lg",
            ),
            class_name="flex items-center justify-between w-full max-w-7xl mx-auto px-4 md:px-8 py-6",
        ),
        class_name="w-full bg-transparent absolute top-0 left-0 z-10 animate-fade-in-down",
    )