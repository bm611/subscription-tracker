import reflex as rx


def navbar() -> rx.Component:
    """Create a responsive navbar component."""
    return rx.el.nav(
        rx.el.div(
            # Logo/Brand section
            rx.el.div(
                rx.el.div(
                    rx.icon("credit_card", size=24, class_name="text-blue-600"),
                    rx.el.span(
                        "RecSub",
                        class_name="ml-2 text-xl font-bold text-gray-900 dark:text-white",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex items-center",
            ),
            
            # Desktop Navigation Links
            rx.el.div(
                rx.el.a(
                    "Dashboard",
                    href="/",
                    class_name="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                rx.el.a(
                    "Subscriptions",
                    href="/subscriptions",
                    class_name="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                rx.el.a(
                    "Analytics",
                    href="/analytics",
                    class_name="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                rx.el.a(
                    "Settings",
                    href="/settings",
                    class_name="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                class_name="hidden md:flex md:items-center md:space-x-1",
            ),
            
            # Right section with actions and mobile menu
            rx.el.div(
                # Add Subscription button
                rx.el.button(
                    rx.icon("plus", size=16, class_name="mr-2"),
                    "Add Subscription",
                    class_name="hidden sm:flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium transition-colors",
                ),
                
                # Dark mode toggle
                rx.color_mode.button(
                    rx.icon("sun", size=20, class_name="text-yellow-500 dark:hidden"),
                    rx.icon("moon", size=20, class_name="text-gray-300 hidden dark:block"),
                    class_name="ml-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors",
                ),
                
                # Mobile menu button
                rx.el.button(
                    rx.icon("menu", size=20),
                    id="mobile-menu-button",
                    class_name="md:hidden ml-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors",
                ),
                
                class_name="flex items-center",
            ),
            
            class_name="flex items-center justify-between w-full",
        ),
        
        # Mobile menu (initially hidden)
        rx.el.div(
            rx.el.div(
                rx.el.a(
                    "Dashboard",
                    href="/",
                    class_name="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                rx.el.a(
                    "Subscriptions",
                    href="/subscriptions",
                    class_name="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                rx.el.a(
                    "Analytics",
                    href="/analytics",
                    class_name="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                rx.el.a(
                    "Settings",
                    href="/settings",
                    class_name="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("plus", size=16, class_name="mr-2"),
                        "Add Subscription",
                        class_name="w-full flex items-center justify-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium transition-colors",
                    ),
                    class_name="mt-4 px-3",
                ),
                class_name="px-2 pt-2 pb-3 space-y-1 sm:px-3",
            ),
            id="mobile-menu",
            class_name="md:hidden border-t border-gray-200 dark:border-gray-700",
        ),
        
        class_name="bg-white dark:bg-gray-900 shadow-sm border-b border-gray-200 dark:border-gray-700 sticky top-0 z-50",
    )


def navbar_simple() -> rx.Component:
    """Create a simpler navbar without mobile menu functionality."""
    return rx.el.nav(
        rx.el.div(
            # Logo/Brand section
            rx.el.div(
                rx.icon("credit_card", size=24, class_name="text-blue-600"),
                rx.el.span(
                    "RecSub",
                    class_name="ml-2 text-xl font-bold text-gray-900 dark:text-white",
                ),
                class_name="flex items-center",
            ),
            
            # Navigation Links
            rx.el.div(
                rx.el.a(
                    "Dashboard",
                    href="/",
                    class_name="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                rx.el.a(
                    "Subscriptions",
                    href="/subscriptions",
                    class_name="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                rx.el.a(
                    "Analytics",
                    href="/analytics",
                    class_name="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:text-blue-400 dark:hover:bg-gray-800 transition-colors",
                ),
                class_name="hidden md:flex md:items-center md:space-x-1",
            ),
            
            # Right section with actions
            rx.el.div(
                rx.el.button(
                    rx.icon("plus", size=16, class_name="mr-2"),
                    "Add",
                    class_name="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 text-sm font-medium transition-colors",
                ),
                rx.color_mode.button(
                    class_name="ml-2 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors",
                ),
                class_name="flex items-center",
            ),
            
            class_name="flex items-center justify-between w-full max-w-7xl mx-auto px-4 py-3",
        ),
        class_name="bg-white dark:bg-gray-900 shadow-sm border-b border-gray-200 dark:border-gray-700 sticky top-0 z-50",
    )
