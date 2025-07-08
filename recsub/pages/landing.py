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
                    rx.link(
                        rx.el.div(
                            "Free and Open Source",
                            class_name="inline-block px-4 py-1 bg-indigo-200/30 text-indigo-500 text-sm font-medium rounded-full border border-indigo-300/40 mb-2",
                        ),
                        href="https://github.com/bm611/subscription-tracker",
                        is_external=True,
                        class_name="no-underline",
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
                                class_name="flex items-center justify-center px-3 py-2 sm:px-8 sm:py-4 bg-indigo-400 text-white rounded-xl hover:bg-indigo-500 transition-all duration-300 group shadow-lg hover:shadow-xl transform hover:scale-105 h-10 sm:h-auto",
                            ),
                            href="/demo",
                            class_name="inline-block mr-3 sm:mr-4 flex-1 sm:flex-none no-underline",
                        ),
                        # Sign In Button
                        rx.link(
                            rx.el.div(
                                rx.el.span(
                                    "Sign In",
                                    class_name="text-base sm:text-lg font-medium whitespace-nowrap",
                                ),
                                class_name="flex items-center justify-center px-3 py-2 sm:px-8 sm:py-4 bg-transparent border-2 border-indigo-400 text-indigo-500 rounded-xl hover:bg-indigo-400 hover:text-white transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105 h-10 sm:h-auto",
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
                    # Glowing border container with pulse animation
                    rx.el.div(
                        # Decorative background elements
                        rx.el.div(
                            class_name="absolute inset-0 bg-gradient-to-br from-indigo-100/20 to-purple-100/20 rounded-2xl animate-pulse",
                            style={"animation-duration": "4s"},
                        ),
                        # Logo grid
                        rx.el.div(
                            *[
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.img(
                                            src=url,
                                            alt=f"Subscribe to {url.split('/')[-1].replace('.com', '').title()} - Subscription service logo",
                                            class_name="w-11 h-11 object-contain transition-all duration-500 group-hover:scale-110 rounded-md",
                                        ),
                                        class_name="relative z-10 transition-all duration-300",
                                    ),
                                    # Gradient border effect
                                    rx.el.div(
                                        class_name="absolute inset-0 bg-gradient-to-br from-indigo-200/40 via-purple-200/40 to-pink-200/40 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-sm",
                                    ),
                                    class_name="group relative bg-white/90 backdrop-blur-sm rounded-xl p-3 shadow-lg hover:shadow-2xl transition-all duration-500 flex items-center justify-center border border-white/40 hover:border-indigo-200/60 transform hover:scale-105 hover:-translate-y-1",
                                    style={
                                        "animation-delay": f"{(i % 12) * 0.1}s",
                                        "animation-fill-mode": "both",
                                        "box-shadow": "0 4px 20px rgba(79, 70, 229, 0.08), 0 1px 3px rgba(0, 0, 0, 0.1)",
                                    },
                                )
                                for i, url in enumerate(logo_url)
                            ],
                            class_name="grid grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-3 lg:gap-4 p-6 lg:p-8 relative z-10",
                        ),
                        class_name="bg-gradient-to-br from-white/85 to-indigo-50/85 backdrop-blur-md rounded-2xl shadow-2xl border border-white/30 relative overflow-hidden",
                        style={
                            "box-shadow": "0 0 60px rgba(79, 70, 229, 0.12), 0 0 120px rgba(79, 70, 229, 0.08), 0 25px 50px rgba(0, 0, 0, 0.1)",
                            "background": "linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(238, 242, 255, 0.9) 50%, rgba(224, 231, 255, 0.9) 100%)",
                        },
                    ),
                    class_name="hidden lg:flex items-center justify-center mb-24 animate-fade-in",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 min-h-screen px-8 md:px-16 lg:px-36 relative z-10 items-center",
            ),
            class_name="min-h-screen bg-gradient-to-br from-indigo-50 via-blue-50 to-purple-50 relative overflow-hidden",
        ),
        class_name="min-h-screen",
    )
