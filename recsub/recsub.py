import reflex as rx
from recsub.components.chart import pie_chart, bar_chart
from recsub.components.table import subscription_table


class State(rx.State):
    """The app state."""


def stats_card(title: str, value: str, icon: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(title, class_name="text-sm"),
                rx.el.p(value, class_name="text-2xl font-bold"),
                class_name="flex flex-col space-y-1",
            ),
            rx.el.div(
                rx.icon(icon, size=24, class_name="text-white"),
                class_name="p-3 rounded-lg",
                style={"background-color": color},
            ),
            class_name="flex items-center justify-between w-full",
        ),
        class_name="p-6 rounded-lg shadow-sm border",
    )


def index() -> rx.Component:
    return rx.el.div(
        # Main Content
        rx.el.div(
            rx.color_mode.button(position="top-right"),
            # Header
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Subscription Manager",
                        class_name="text-2xl md:text-4xl font-bold",
                    ),
                    rx.el.p(
                        "Manage and track all your subscriptions in one place",
                        class_name="mt-2 text-sm md:text-base",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("calendar", size=16, class_name="mr-2"),
                        rx.el.span("Calendar View", class_name="hidden sm:inline"),
                        rx.el.span("Cal", class_name="sm:hidden"),
                        class_name="px-3 md:px-4 py-2 border rounded-lg hover:bg-opacity-10 flex items-center text-sm",
                    ),
                    rx.el.button(
                        rx.icon("plus", size=16, class_name="mr-2"),
                        rx.el.span("Add Subscription", class_name="hidden sm:inline"),
                        rx.el.span("Add", class_name="sm:hidden"),
                        class_name="px-3 md:px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 flex items-center ml-2 text-sm",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex flex-col sm:flex-row sm:items-center sm:justify-between w-full mb-6 md:mb-8 gap-4 sm:gap-0",
            ),
            # Stats Cards
            rx.el.div(
                stats_card(
                    "Active Subscriptions", "6", "credit_card", "rgb(59, 130, 246)"
                ),
                stats_card(
                    "Monthly Spending", "$101.30", "dollar_sign", "rgb(34, 197, 94)"
                ),
                stats_card(
                    "Annual Spending", "$1215.62", "trending_up", "rgb(168, 85, 247)"
                ),
                stats_card("Due This Week", "0", "calendar", "rgb(249, 115, 22)"),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-6 md:mb-8",
            ),
            # Charts Section
            rx.el.div(
                # Spending by Category
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Spending by Category",
                            class_name="text-xl font-bold mb-4",
                        ),
                        pie_chart(),
                        class_name="flex flex-col items-center",
                    ),
                    class_name="p-4 md:p-6 rounded-lg shadow-sm border h-80 md:h-96",
                ),
                # Monthly Spending Trend
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Monthly Spending Trend",
                            class_name="text-xl font-bold mb-4",
                        ),
                        bar_chart(),
                        class_name="flex flex-col items-center",
                    ),
                    class_name="p-4 md:p-6 rounded-lg shadow-sm border h-80 md:h-96",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 md:gap-6 mb-6 md:mb-8",
            ),
            # Subscription Table Section
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Active Subscriptions", class_name="text-2xl font-bold mb-6"
                    ),
                    subscription_table(),
                    class_name="w-full",
                ),
                class_name="p-4 md:p-6 rounded-lg shadow-sm border overflow-x-auto",
            ),
            class_name="max-w-7xl mx-auto p-4 md:p-6 min-h-screen",
        ),
    )


app = rx.App(
    # theme=rx.theme(
    #     appearance="light",
    # ),
)
app.add_page(index)
