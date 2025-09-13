import reflex as rx


def service_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.icon(tag=icon, class_name="text-[#f78000] w-12 h-12 mb-4"),
        rx.el.h3(title, class_name="text-2xl font-bold text-[#fefadc] mb-2"),
        rx.el.p(description, class_name="text-[#8d909b]"),
        class_name="bg-[#2d2d2d]/50 p-8 rounded-lg border border-white/10 text-center flex flex-col items-center",
    )


def services_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "What We Do",
                class_name="text-4xl md:text-5xl font-bold text-[#fefadc] mb-12 text-center",
            ),
            rx.el.div(
                service_card(
                    "cloud",
                    "Cloud Migration",
                    "Seamlessly transition your infrastructure to the cloud with minimal downtime.",
                ),
                service_card(
                    "database",
                    "Data Solutions",
                    "Unlock the power of your data with our custom analytics and database management services.",
                ),
                service_card(
                    "shield_check",
                    "Cybersecurity",
                    "Protect your digital assets with our robust and proactive security measures.",
                ),
                service_card(
                    "code",
                    "Custom Development",
                    "Bespoke software solutions tailored to your unique business needs and goals.",
                ),
                class_name="grid md:grid-cols-2 lg:grid-cols-4 gap-8",
            ),
            class_name="py-20 px-4 max-w-7xl mx-auto",
        ),
        id="services",
        class_name="w-full",
    )