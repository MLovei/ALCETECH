import reflex as rx
from app.state import State


def contact_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.h2(
                "Contact Us",
                class_name="text-4xl md:text-5xl font-bold text-[#fefadc] mb-12 text-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.form(
                        rx.el.div(
                            rx.el.input(
                                placeholder="Full Name *",
                                name="full_name",
                                type="text",
                                class_name="w-full bg-transparent border-b border-white/20 rounded-none px-1 py-2 text-[#fefadc] placeholder:text-white/50 focus:outline-none focus:border-[#f78000] transition-colors",
                            ),
                            rx.el.input(
                                placeholder="Phone",
                                name="phone",
                                type="tel",
                                class_name="w-full bg-transparent border-b border-white/20 rounded-none px-1 py-2 text-[#fefadc] placeholder:text-white/50 focus:outline-none focus:border-[#f78000] transition-colors",
                            ),
                            rx.el.input(
                                placeholder="Email *",
                                name="email",
                                type="email",
                                class_name="w-full bg-transparent border-b border-white/20 rounded-none px-1 py-2 text-[#fefadc] placeholder:text-white/50 focus:outline-none focus:border-[#f78000] transition-colors",
                            ),
                            rx.el.textarea(
                                placeholder="Message",
                                name="message",
                                class_name="w-full bg-transparent border-b border-white/20 rounded-none px-1 py-2 text-[#fefadc] placeholder:text-white/50 focus:outline-none focus:border-[#f78000] transition-colors h-24",
                            ),
                            rx.el.button(
                                "SEND MESSAGE",
                                type="submit",
                                class_name="bg-[#f78000] text-black px-8 py-3 rounded-sm font-bold hover:bg-[#fefadc] transition-colors duration-300 shadow-lg w-fit mt-4",
                            ),
                            class_name="flex flex-col gap-8",
                        ),
                        on_submit=State.handle_submit,
                        reset_on_submit=True,
                    ),
                    class_name="w-full",
                ),
                rx.el.div(
                    rx.el.iframe(
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3283.834854583693!2d33.34449831522964!3d35.1691689802702!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14de1a5a5b8a6b6f%3A0x8f2d5a3b1d3e1d1!2sEplan%20Consultants%20Ltd!5e0!3m2!1sen!2s!4v1678886971578!5m2!1sen!2s",
                        class_name="w-full h-full border-0 rounded-lg",
                        loading="lazy",
                        referrer_policy="no-referrer-when-downgrade",
                    ),
                    class_name="hidden lg:block w-full h-full",
                ),
                class_name="grid lg:grid-cols-2 gap-16 items-start",
            ),
            class_name="py-20 px-4 max-w-7xl mx-auto",
        ),
        id="contact",
        class_name="w-full",
    )