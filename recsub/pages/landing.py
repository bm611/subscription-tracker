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
                            class_name="inline-block w-full sm:w-auto sm:mr-4 no-underline",
                        ),
                        # Sign In Button
                        rx.link(
                            rx.el.div(
                                rx.el.div(
                                    rx.html(
                                        '<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="20" height="20" viewBox="0 0 48 48"><path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"></path><path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"></path><path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"></path><path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"></path></svg>'
                                    ),
                                    class_name="w-5 h-5 mr-2 flex items-center justify-center",
                                ),
                                rx.el.span(
                                    "Sign in with Google",
                                    class_name="text-base sm:text-lg font-medium whitespace-nowrap",
                                ),
                                class_name="flex items-center justify-center px-3 py-2 sm:px-8 sm:py-4 bg-transparent border-2 border-indigo-400 text-indigo-500 rounded-xl hover:bg-indigo-400 hover:text-white transition-all duration-300 shadow-lg hover:shadow-xl transform hover:scale-105 h-10 sm:h-auto",
                            ),
                            href="/signin",
                            class_name="inline-block w-full sm:w-auto no-underline",
                        ),
                        class_name="flex flex-col sm:flex-row items-center w-full sm:w-auto space-y-3 sm:space-y-0 mx-auto sm:mx-0",
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
