import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.el.div(
                            rx.el.span("ALCE", class_name="font-bold"),
                            rx.el.span("TECH", class_name="font-light"),
                            class_name="text-4xl text-white tracking-widest",
                        ),
                        href="/",
                    ),
                    class_name="mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h4(
                            "CONTACT DETAILS",
                            class_name="font-bold text-white mb-4 tracking-wider",
                        ),
                        rx.el.p(
                            "72, 28th October Street, Office 201,",
                            class_name="text-white/70",
                        ),
                        rx.el.p(
                            "2414, Egkomi, Nicosia, Cyprus", class_name="text-white/70"
                        ),
                        rx.el.a(
                            "info@alcetech.com",
                            href="mailto:info@alcetech.com",
                            class_name="text-white/70 hover:text-[#f78000] mt-4 block",
                        ),
                        rx.el.a(
                            "+357 22 519516",
                            href="tel:+35722519516",
                            class_name="text-white/70 hover:text-[#f78000] block",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h4(
                            "PARTNERS WITH",
                            class_name="font-bold text-white mb-4 tracking-wider",
                        ),
                        rx.el.p("Google Cloud Partner", class_name="text-white/70"),
                        rx.el.p("Odoo Gold Partner", class_name="text-white/70"),
                        rx.el.p("Zoho Authorized Partner", class_name="text-white/70"),
                    ),
                    rx.el.div(
                        rx.el.h4(
                            "CERTIFIED BY",
                            class_name="font-bold text-white mb-4 tracking-wider",
                        ),
                        rx.el.p(
                            "Human Resource Development", class_name="text-white/70"
                        ),
                        rx.el.p("Authority of Cyprus", class_name="text-white/70"),
                        rx.el.div(
                            rx.icon(
                                tag="facebook",
                                class_name="text-white/70 hover:text-[#f78000] cursor-pointer",
                            ),
                            rx.icon(
                                tag="twitter",
                                class_name="text-white/70 hover:text-[#f78000] cursor-pointer",
                            ),
                            rx.icon(
                                tag="linkedin",
                                class_name="text-white/70 hover:text-[#f78000] cursor-pointer",
                            ),
                            class_name="flex gap-4 mt-4",
                        ),
                    ),
                    class_name="grid md:grid-cols-3 gap-8",
                ),
                class_name="grid lg:grid-cols-2 gap-8 items-start border-t border-white/20 pt-12",
            ),
            class_name="max-w-7xl mx-auto px-4 py-12",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "© 2024 AlceTech Consultants. All rights reserved.",
                    class_name="text-sm text-white/50",
                ),
                class_name="max-w-7xl mx-auto px-4 py-6 border-t border-white/20 text-center",
            )
        ),
        class_name="bg-[#1c1c1c]",
    )