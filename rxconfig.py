import reflex as rx
import os

railway_domain = "RAILWAY_PUBLIC_DOMAIN"


class ReflextemplateConfig(rx.Config):
    pass


config = ReflextemplateConfig(
    app_name="recsub",
    telemetry_enabled=False,
    frontend_port=3000,  # default frontend port
    backend_port=8000,  # default backend port
    # For production on Railway, we need to use the public domain
    api_url=f"https://{os.environ[railway_domain]}"
    if railway_domain in os.environ
    else "http://localhost:8000",
    # Set backend host to bind to all interfaces in production
    backend_host="0.0.0.0" if railway_domain in os.environ else "127.0.0.1",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    show_built_with_reflex=False,
)
