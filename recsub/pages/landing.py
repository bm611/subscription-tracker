import reflex as rx


def landing_page() -> rx.Component:
    return rx.el.div(
        # Background with dark theme
        rx.el.div(
            # Color mode button
            rx.color_mode.button(position="top-right", class_name="z-10 relative"),
            # Main content
            rx.el.div(
                rx.el.div(
                    # Badge
                    rx.el.div(
                        "100% Free Forever",
                        class_name="inline-block px-4 py-2 bg-green-400/20 text-green-400 text-sm font-medium rounded-full border border-green-400/30 mb-6",
                    ),
                    # Main heading
                    rx.el.h1(
                        rx.el.span("Track all your", class_name="text-white block"),
                        rx.el.span("subscriptions.", class_name="text-white block"),
                        rx.el.span("In one place.", class_name="text-green-400 block"),
                        class_name="text-4xl md:text-5xl lg:text-6xl font-bold leading-tight mb-12",
                    ),
                    # CTA Buttons
                    rx.el.div(
                        # View Demo Button
                        rx.link(
                            rx.el.div(
                                rx.el.span(
                                    "View Demo",
                                    class_name="text-base sm:text-lg font-medium whitespace-nowrap",
                                ),
                                rx.el.div(
                                    "→",
                                    class_name="text-lg sm:text-xl ml-2 sm:ml-4 transform group-hover:translate-x-2 transition-transform duration-300",
                                ),
                                class_name="flex items-center justify-center px-4 py-3 sm:px-8 sm:py-4 bg-white text-black rounded-xl hover:bg-gray-100 transition-all duration-300 group shadow-lg hover:shadow-xl transform hover:scale-105 h-12 sm:h-auto",
                            ),
                            href="/demo",
                            class_name="inline-block mr-3 sm:mr-4 flex-[1.4] sm:flex-none",
                        ),
                        # Sign In Button
                        rx.link(
                            rx.el.div(
                                rx.el.span(
                                    "Sign In",
                                    class_name="text-base sm:text-lg font-medium whitespace-nowrap",
                                ),
                                class_name="flex items-center justify-center px-4 py-3 sm:px-8 sm:py-4 bg-transparent border-2 border-green-400 text-green-400 rounded-xl hover:bg-green-400 hover:text-black transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105 h-12 sm:h-auto",
                            ),
                            href="/signin",
                            class_name="inline-block flex-1 sm:flex-none",
                        ),
                        class_name="flex flex-row items-center w-full sm:w-auto",
                    ),
                    class_name="text-left max-w-lg",
                ),
                class_name="flex items-center justify-start min-h-screen px-8 md:px-16 lg:px-24 relative z-10",
            ),
            class_name="min-h-screen bg-gray-900 relative overflow-hidden",
        ),
        class_name="min-h-screen",
    )
