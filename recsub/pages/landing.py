import reflex as rx
from recsub.data.url import logo_url


def landing_page() -> rx.Component:
    return rx.el.div(
        # Background with soft pastel theme
        rx.el.div(
            # Main content
            rx.el.div(
                # Left side - Main content
                rx.el.div(
                    # Badge
                    rx.el.div(
                        "100% Free Forever",
                        class_name="inline-block px-4 py-1 bg-indigo-200/30 text-indigo-500 text-sm font-medium rounded-full border border-indigo-300/40 mb-2",
                    ),
                    # Main heading
                    rx.el.h1(
                        rx.el.span("Track all your", class_name="text-gray-800 block"),
                        rx.el.span("subscriptions.", class_name="text-gray-800 block"),
                        rx.el.span("In one place.", class_name="text-indigo-500 block"),
                        class_name="text-5xl lg:text-7xl font-bold leading-tight mb-8",
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
                                class_name="flex items-center justify-center px-4 py-3 sm:px-8 sm:py-4 bg-indigo-400 text-white rounded-xl hover:bg-indigo-500 transition-all duration-300 group shadow-lg hover:shadow-xl transform hover:scale-105 h-12 sm:h-auto",
                            ),
                            href="/demo",
                            class_name="inline-block mr-3 sm:mr-4 flex-[1.4] sm:flex-none no-underline",
                        ),
                        # Sign In Button
                        rx.link(
                            rx.el.div(
                                rx.el.span(
                                    "Sign In",
                                    class_name="text-base sm:text-lg font-medium whitespace-nowrap",
                                ),
                                class_name="flex items-center justify-center px-4 py-3 sm:px-8 sm:py-4 bg-transparent border-2 border-indigo-400 text-indigo-500 rounded-xl hover:bg-indigo-400 hover:text-white transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105 h-12 sm:h-auto",
                            ),
                            href="/signin",
                            class_name="inline-block flex-1 sm:flex-none no-underline",
                        ),
                        class_name="flex flex-row items-center w-full sm:w-auto",
                    ),
                    class_name="text-left max-w-lg mb-24",
                ),
                # Right side - Logo grid (desktop only)
                rx.el.div(
                    # Glowing border container
                    rx.el.div(
                        # Logo grid
                        rx.el.div(
                            *[
                                rx.el.div(
                                    rx.el.img(
                                        src=url,
                                        alt="Subscription service logo",
                                        class_name="w-12 h-12 object-contain transition-all duration-300 hover:opacity-80 transform hover:scale-105 rounded-md",
                                    ),
                                    class_name="bg-white rounded-xl p-2 shadow-sm hover:shadow-md transition-all duration-300 flex items-center justify-center",
                                )
                                for url in logo_url
                            ],
                            class_name="grid grid-cols-6 gap-4 p-6",
                        ),
                        class_name="bg-gradient-to-br from-white/80 to-indigo-50/80 backdrop-blur-sm rounded-2xl shadow-2xl border border-white/20 relative overflow-hidden",
                        style={
                            "box-shadow": "0 0 40px rgba(79, 70, 229, 0.15), 0 0 80px rgba(79, 70, 229, 0.1)",
                            "border-image": "linear-gradient(135deg, rgba(79, 70, 229, 0.3), rgba(147, 51, 234, 0.3)) 1",
                        },
                    ),
                    class_name="hidden lg:flex items-center justify-center mb-24",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 min-h-screen px-8 md:px-16 lg:px-36 relative z-10 items-center",
            ),
            class_name="min-h-screen bg-gradient-to-br from-indigo-50 via-blue-50 to-purple-50 relative overflow-hidden",
        ),
        class_name="min-h-screen",
    )
