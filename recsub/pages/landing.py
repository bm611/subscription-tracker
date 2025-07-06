import reflex as rx


def landing_page() -> rx.Component:
    return rx.el.div(
        rx.color_mode.button(position="top-right"),
        # Hero Section
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "RecSub",
                    class_name="text-4xl md:text-6xl lg:text-7xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-6",
                ),
                rx.el.p(
                    "Take control of your subscriptions with our powerful management platform",
                    class_name="text-lg md:text-xl lg:text-2xl opacity-70 mb-8 max-w-2xl mx-auto",
                ),
                rx.link(
                    rx.el.button(
                        "View Demo",
                        class_name="px-8 py-4 bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-lg hover:from-blue-700 hover:to-blue-800 font-medium text-lg transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105",
                    ),
                    href="/demo",
                ),
                class_name="text-center",
            ),
            class_name="flex items-center justify-center min-h-screen max-w-4xl mx-auto p-4 md:p-6 lg:p-8",
        ),
        class_name="min-h-screen",
    )