import reflex as rx


def hero() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Different. Effective. Curious.",
                class_name="text-5xl md:text-7xl font-bold text-[#fefadc] mb-6 animate-fade-in-up",
            ),
            rx.el.p(
                "We operate in the present. We live in the future.",
                class_name="text-lg md:text-xl text-[#8d909b] mb-10 animate-fade-in-up animation-delay-300",
            ),
            rx.el.button(
                "CLOUD BASED SOLUTIONS FOR EVERYONE",
                class_name="bg-transparent border border-[#fefadc] text-[#fefadc] px-10 py-3 rounded-sm font-medium hover:bg-[#f78000] hover:border-[#f78000] transition-colors duration-300 shadow-lg animate-fade-in-up animation-delay-600",
            ),
            class_name="z-10 text-center flex flex-col items-center",
        ),
        rx.el.div(
            rx.icon(
                tag="arrow_up_wide_narrow",
                class_name="text-[#fefadc]/10 text-9xl absolute animate-float-up",
            ),
            class_name="absolute top-1/4 right-1/4 opacity-50",
        ),
        rx.el.div(
            rx.icon(
                tag="arrow_down_wide_narrow",
                class_name="text-[#fefadc]/10 text-9xl absolute animate-float-down",
            ),
            class_name="absolute bottom-1/4 left-1/4 opacity-50",
        ),
        class_name="relative flex items-center justify-center min-h-screen w-full px-4",
    )