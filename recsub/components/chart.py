import reflex as rx

tooltip = {
    "is_animation_active": False,
    "separator": "",
    "cursor": False,
    "item_style": {
        "color": "currentColor",
        "display": "flex",
        "paddingBottom": "0px",
        "justifyContent": "space-between",
        "textTransform": "capitalize",
    },
    "label_style": {
        "color": rx.color("slate", 10),
        "fontWeight": "500",
    },
    "content_style": {
        "background": rx.color_mode_cond("oklch(0.97 0.00 0)", "oklch(0.14 0.00 286)"),
        "borderColor": rx.color("slate", 5),
        "borderRadius": "5px",
        "fontFamily": "IBM Plex Mono,ui-monospace,monospace",
        "fontSize": "0.875rem",
        "lineHeight": "1.25rem",
        "fontWeight": "500",
        "letterSpacing": "-0.01rem",
        "minWidth": "8rem",
        "width": "175px",
        "padding": "0.375rem 0.625rem ",
        "position": "relative",
    },
}


def info(title: str, size: str, subtitle: str, align: str):
    return rx.vstack(
        rx.heading(title, size=size, weight="bold"),
        rx.text(subtitle, size="1", color=rx.color("slate", 11), weight="medium"),
        spacing="1",
        align=align,
    )


def get_tooltip():
    """Standard tooltip for all charts."""
    return rx.recharts.graphing_tooltip(**tooltip)


def get_cartesian_grid():
    """Standard cartesian grid for charts."""
    return rx.recharts.cartesian_grid(
        horizontal=True, vertical=False, class_name="opacity-25"
    )


def get_x_axis(data_key: str):
    """Standard X axis configuration."""
    return rx.recharts.x_axis(
        data_key=data_key,
        axis_line=False,
        tick_size=10,
        tick_line=False,
        custom_attrs={"fontSize": "12px"},
        interval="preserveStartEnd",
    )


def pie_chart() -> rx.Component:
    data = [
        {"name": "Software", "value": 45, "color": "rgb(59, 130, 246)"},
        {"name": "Shopping", "value": 15, "color": "rgb(34, 197, 94)"},
        {"name": "Productivity", "value": 8, "color": "rgb(6, 182, 212)"},
        {"name": "Streaming", "value": 25, "color": "rgb(239, 68, 68)"},
        {"name": "Gaming", "value": 7, "color": "rgb(168, 85, 247)"},
    ]

    return rx.el.div(
        rx.el.div(
            rx.recharts.pie_chart(
                rx.recharts.pie(
                    rx.foreach(
                        ["#3b82f6", "#22c55e", "#06b6d4", "#ef4444", "#a855f7"],
                        lambda color, index: rx.recharts.cell(fill=color),
                    ),
                    data=data,
                    data_key="value",
                    name_key="name",
                    stroke="0",
                    inner_radius=50,
                    outer_radius=90,
                    custom_attrs={"paddingAngle": 3, "cornerRadius": 4},
                ),
                get_tooltip(),
                width="100%",
                height=220,
            ),
            class_name="flex justify-center items-center",
        ),
        rx.el.div(
            rx.foreach(
                [
                    ["Software", "blue"],
                    ["Shopping", "green"],
                    ["Productivity", "cyan"],
                    ["Streaming", "red"],
                    ["Gaming", "purple"],
                ],
                lambda key: rx.el.div(
                    rx.el.div(
                        class_name="w-3 h-3 rounded-full shadow-sm",
                        style={"background-color": rx.color(key[1])},
                    ),
                    rx.el.span(
                        key[0],
                        class_name="text-xs md:text-sm font-medium opacity-80",
                    ),
                    class_name="flex items-center gap-2",
                ),
            ),
            class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-3 md:gap-4 mt-4 px-2",
        ),
        class_name="flex flex-col w-full h-full justify-center",
    )


def bar_chart() -> rx.Component:
    data = [
        {"month": "Aug", "amount": 155},
        {"month": "Sep", "amount": 102},
        {"month": "Oct", "amount": 120},
        {"month": "Nov", "amount": 105},
        {"month": "Dec", "amount": 118},
        {"month": "Jan", "amount": 108},
    ]

    return rx.el.div(
        rx.recharts.bar_chart(
            rx.recharts.bar(
                rx.recharts.label_list(
                    data_key="amount",
                    position="top",
                    custom_attrs={
                        "fontSize": "12px",
                        "fontWeight": "500",
                        "fill": "currentColor",
                        "dy": -4
                    }
                ),
                data_key="amount",
                stroke="rgb(59, 130, 246)",
                fill="rgb(59, 130, 246)",
                radius=[6, 6, 0, 0],
            ),
            get_x_axis("month"),
            rx.recharts.y_axis(
                hide=True,
            ),
            get_tooltip(),
            data=data,
            width="100%",
            height=280,
            margin={"left": 0, "right": 0, "top": 30, "bottom": 20},
        ),
        class_name="flex justify-center items-center w-full h-full",
    )
