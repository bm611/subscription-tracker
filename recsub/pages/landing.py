import reflex as rx


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
                # Right side - Features (desktop only)
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            # Analytics Feature
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        tag="bar-chart-3",
                                        class_name="w-6 h-6 text-indigo-500",
                                    ),
                                    class_name="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center mb-3",
                                ),
                                rx.el.h3(
                                    "Smart Analytics",
                                    class_name="text-lg font-semibold text-gray-800 mb-2",
                                ),
                                rx.el.p(
                                    "Track spending patterns and subscription trends with detailed charts and insights.",
                                    class_name="text-gray-600 text-sm",
                                ),
                                class_name="bg-white/70 backdrop-blur-sm p-6 rounded-xl shadow-lg border border-indigo-100/50 hover:shadow-xl transition-all duration-300",
                            ),
                            # Calendar View Feature
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        tag="calendar",
                                        class_name="w-6 h-6 text-indigo-500",
                                    ),
                                    class_name="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center mb-3",
                                ),
                                rx.el.h3(
                                    "Calendar View",
                                    class_name="text-lg font-semibold text-gray-800 mb-2",
                                ),
                                rx.el.p(
                                    "See all your upcoming billing dates in an intuitive calendar interface.",
                                    class_name="text-gray-600 text-sm",
                                ),
                                class_name="bg-white/70 backdrop-blur-sm p-6 rounded-xl shadow-lg border border-indigo-100/50 hover:shadow-xl transition-all duration-300",
                            ),
                            # Notifications Feature
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        tag="bell",
                                        class_name="w-6 h-6 text-indigo-500",
                                    ),
                                    class_name="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center mb-3",
                                ),
                                rx.el.h3(
                                    "Smart Alerts",
                                    class_name="text-lg font-semibold text-gray-800 mb-2",
                                ),
                                rx.el.p(
                                    "Get notified before billing dates and track subscription changes automatically.",
                                    class_name="text-gray-600 text-sm",
                                ),
                                class_name="bg-white/70 backdrop-blur-sm p-6 rounded-xl shadow-lg border border-indigo-100/50 hover:shadow-xl transition-all duration-300",
                            ),
                            # Budget Tracking Feature
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        tag="dollar-sign",
                                        class_name="w-6 h-6 text-indigo-500",
                                    ),
                                    class_name="w-12 h-12 bg-indigo-100 rounded-lg flex items-center justify-center mb-3",
                                ),
                                rx.el.h3(
                                    "Budget Control",
                                    class_name="text-lg font-semibold text-gray-800 mb-2",
                                ),
                                rx.el.p(
                                    "Set spending limits and monitor your subscription costs against your budget.",
                                    class_name="text-gray-600 text-sm",
                                ),
                                class_name="bg-white/70 backdrop-blur-sm p-6 rounded-xl shadow-lg border border-indigo-100/50 hover:shadow-xl transition-all duration-300",
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                        ),
                    ),
                    class_name="hidden lg:flex items-center justify-center mb-24",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 min-h-screen px-8 md:px-16 lg:px-36 relative z-10 items-center",
            ),
            class_name="min-h-screen bg-gradient-to-br from-indigo-50 via-blue-50 to-purple-50 relative overflow-hidden",
        ),
        class_name="min-h-screen",
    )
