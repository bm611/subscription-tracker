import reflex as rx


def stats_card(title: str, value: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                title, 
                class_name="text-xs md:text-sm font-medium opacity-70 uppercase tracking-wide"
            ),
            rx.el.p(
                value, 
                class_name="text-xl md:text-2xl lg:text-3xl font-bold mt-2"
            ),
            class_name="flex flex-col space-y-1",
        ),
        class_name="group col-span-1 p-4 md:p-6 backdrop-blur-sm rounded-xl md:rounded-2xl border border-opacity-20 shadow-lg hover:shadow-xl hover:scale-[1.02] transition-all duration-300 cursor-pointer",
    )