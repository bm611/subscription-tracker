import reflex as rx
from recsub.components.chart import pie_chart, bar_chart
from recsub.components.table import subscription_table


class State(rx.State):
    """The app state."""


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
                        class_name="text-2xl md:text-3xl lg:text-4xl font-bold",
                    ),
                    rx.el.p(
                        "Manage and track all your subscriptions in one place",
                        class_name="mt-2 text-sm md:text-base lg:text-lg opacity-70",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("calendar", size=16, class_name="mr-2"),
                        rx.el.span("Calendar View", class_name="hidden sm:inline"),
                        rx.el.span("Cal", class_name="sm:hidden"),
                        class_name="px-3 md:px-4 py-2 border border-opacity-20 rounded-lg hover:bg-opacity-10 flex items-center text-sm font-medium transition-colors duration-200",
                    ),
                    rx.el.button(
                        rx.icon("plus", size=16, class_name="mr-2"),
                        rx.el.span("Add Subscription", class_name="hidden sm:inline"),
                        rx.el.span("Add", class_name="sm:hidden"),
                        class_name="px-3 md:px-4 py-2 bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-lg hover:from-blue-700 hover:to-blue-800 flex items-center ml-2 text-sm font-medium transition-all duration-200 shadow-lg hover:shadow-xl",
                    ),
                    class_name="flex items-center",
                ),
                class_name="flex flex-col sm:flex-row sm:items-center sm:justify-between w-full mb-8 md:mb-10 gap-4 sm:gap-0",
            ),
            # Stats Cards Row
            rx.el.div(
                stats_card("Active Subscriptions", "6"),
                stats_card("Monthly Spending", "$101.30"),
                stats_card("Annual Spending", "$1215.62"),
                stats_card("Due This Week", "0"),
                class_name="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-8 md:mb-10",
            ),
            
            # Charts Section - Bento Style
            rx.el.div(
                # Spending by Category - Large tile
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Spending by Category",
                            class_name="text-lg md:text-xl font-bold mb-4",
                        ),
                        pie_chart(),
                        class_name="flex flex-col items-center h-full",
                    ),
                    class_name="col-span-1 lg:col-span-1 p-4 md:p-6 backdrop-blur-md rounded-xl md:rounded-2xl border border-opacity-20 shadow-xl hover:shadow-2xl transition-all duration-300 min-h-[320px] md:min-h-[400px]",
                ),
                # Monthly Spending Trend - Medium tile
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Monthly Spending Trend",
                            class_name="text-lg md:text-xl font-bold mb-4",
                        ),
                        bar_chart(),
                        class_name="flex flex-col items-center h-full",
                    ),
                    class_name="col-span-1 lg:col-span-1 p-4 md:p-6 backdrop-blur-md rounded-xl md:rounded-2xl border border-opacity-20 shadow-xl hover:shadow-2xl transition-all duration-300 min-h-[320px] md:min-h-[400px]",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-4 md:gap-6 mb-8 md:mb-10",
            ),
            # Subscription Table Section - Full Width
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Active Subscriptions", 
                        class_name="text-xl md:text-2xl font-bold mb-6"
                    ),
                    subscription_table(),
                    class_name="w-full",
                ),
                class_name="p-4 md:p-6 lg:p-8 backdrop-blur-sm rounded-xl md:rounded-2xl border border-opacity-20 shadow-xl hover:shadow-2xl transition-all duration-300 overflow-x-auto",
            ),
            class_name="max-w-7xl mx-auto p-4 md:p-6 lg:p-8 min-h-screen",
        ),
        class_name="min-h-screen",
    )


style = {
    "font_family": "funnel",
}


app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css"],
)
app.add_page(index)
