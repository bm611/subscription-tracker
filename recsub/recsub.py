import reflex as rx
from recsub.pages.landing import landing_page
from recsub.pages.demo import demo_page


class State(rx.State):
    """The app state."""


@rx.page(route="/")
def index() -> rx.Component:
    return landing_page()


@rx.page(route="/demo")
def demo() -> rx.Component:
    return demo_page()


style = {
    "font_family": "funnel",
}


app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css", "/animations.css"],
)
