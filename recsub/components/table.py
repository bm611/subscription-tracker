import reflex as rx
from typing import Dict, List


class SubscriptionTable(rx.State):
    subscription_data: List[Dict[str, str | bool | float]] = [
        {
            "service": "Netflix",
            "logo": "https://logos-world.net/wp-content/uploads/2020/04/Netflix-Logo.png",
            "category": "Streaming",
            "price": 15.99,
            "billing_cycle": "Monthly",
            "next_billing": "2024-01-15",
            "status": "Active",
            "active": True,
        },
        {
            "service": "Spotify",
            "logo": "https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png",
            "category": "Music",
            "price": 9.99,
            "billing_cycle": "Monthly",
            "next_billing": "2024-01-12",
            "status": "Active",
            "active": True,
        },
        {
            "service": "Adobe",
            "logo": "https://www.adobe.com/content/dam/cc/icons/Adobe_Corporate_Horizontal_Red_HEX.svg",
            "category": "Software",
            "price": 52.99,
            "billing_cycle": "Monthly",
            "next_billing": "2024-01-20",
            "status": "Active",
            "active": True,
        },
        {
            "service": "GitHub Pro",
            "logo": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
            "category": "Development",
            "price": 4.00,
            "billing_cycle": "Monthly",
            "next_billing": "2024-01-08",
            "status": "Active",
            "active": True,
        },
        {
            "service": "Notion",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/4/45/Notion_app_logo.png",
            "category": "Productivity",
            "price": 8.00,
            "billing_cycle": "Monthly",
            "next_billing": "2024-01-25",
            "status": "Canceled",
            "active": False,
        },
        {
            "service": "Disney+",
            "logo": "https://cnbl-cdn.bamgrid.com/assets/7ecc8bcb60ad77193058d63e321bd21cbac2fc67051bf9a3b2c4b9e6c7c9f080.png",
            "category": "Streaming",
            "price": 10.99,
            "billing_cycle": "Monthly",
            "next_billing": "2024-01-18",
            "status": "Active",
            "active": True,
        },
    ]


def subscription_table():
    def render_subscription_row(data: dict[str, str | bool | float]):
        return rx.table.row(
            rx.table.cell(
                rx.vstack(
                    rx.text(
                        data["service"],
                        size="1",
                        weight="bold",
                    ),
                    rx.text(data["category"], size="1"),
                    spacing="0",
                    align="start",
                )
            ),
            rx.table.cell(
                rx.text(f"${data['price']:.2f}", size="1", weight="medium"),
                width="100px",
            ),
            rx.table.cell(rx.text(data["billing_cycle"], size="1", weight="regular")),
            rx.table.cell(rx.text(data["next_billing"], size="1", weight="regular")),
            rx.table.cell(
                rx.badge(
                    data["status"],
                    color_scheme=rx.cond(data["active"], "blue", "gray"),
                    size="1",
                    width="100%",
                    display="flex",
                    justify_content="center",
                    padding="0.25em 0.15em",
                ),
            ),
            rx.table.cell(
                rx.hstack(
                    rx.icon_button(
                        rx.icon("pencil", size=14),
                        size="1",
                        variant="ghost",
                        cursor="pointer",
                    ),
                    rx.icon_button(
                        rx.icon("trash-2", size=14),
                        size="1",
                        variant="ghost",
                        color_scheme="red",
                        cursor="pointer",
                    ),
                    spacing="1",
                ),
            ),
            white_space="nowrap",
            align="center",
        )

    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.foreach(
                    [
                        "Service",
                        "Price",
                        "Billing",
                        "Next Billing",
                        "Status",
                        "Actions",
                    ],
                    lambda title: rx.table.column_header_cell(
                        rx.text(title, size="1", weight="bold")
                    ),
                ),
                white_space="nowrap",
            ),
        ),
        rx.table.body(
            rx.foreach(SubscriptionTable.subscription_data, render_subscription_row)
        ),
        width="100%",
        variant="ghost",
        size="1",
        class_name="min-w-full",
    )
