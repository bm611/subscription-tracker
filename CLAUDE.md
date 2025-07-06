# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

RecSub is a subscription management web application built with Reflex (Python web framework). It provides a dashboard for tracking and managing subscriptions with features like spending analytics, charts, and subscription tables.

## Development Commands

### Running the Application
```bash
reflex run
```

### Development Server
```bash
reflex run --dev
```

### Building for Production
```bash
reflex export
```

### Installing Dependencies
```bash
uv install
```

## Architecture

### Framework
- **Reflex**: Python-based web framework for building full-stack applications
- **TailwindCSS**: Utility-first CSS framework via TailwindV4Plugin
- **Recharts**: Chart library for data visualization

### Project Structure
```
recsub/
├── components/          # Reusable UI components
│   ├── chart.py        # Chart components (pie_chart, bar_chart)
│   ├── navbar.py       # Navigation components
│   └── table.py        # Subscription table component
├── recsub.py           # Main application and pages
└── __init__.py
```

### Key Components

#### State Management
- `State` class in `recsub.py` - Main application state
- `SubscriptionTable` class in `table.py` - Subscription data state with sample data

#### UI Components
- **Charts**: Configured with standardized tooltip, grid, and axis styling
- **Navbar**: Responsive navigation with mobile menu support
- **Table**: Subscription data display with edit/delete actions
- **Stats Cards**: Dashboard metrics display

### Configuration
- `rxconfig.py`: Reflex configuration with SitemapPlugin and TailwindV4Plugin
- `pyproject.toml`: Python dependencies (requires Python >=3.13, Reflex >=0.8.0)

### Data Structure
Subscription data includes:
- Service name and logo
- Category, price, billing cycle
- Next billing date and status
- Active/inactive state

## Development Notes

### Component Patterns
- Components use `rx.el.div` for HTML elements with Tailwind classes
- State management through Reflex State classes
- Responsive design with mobile-first approach
- Dark mode support via `rx.color_mode`

### Chart Configuration
- Standardized chart styling in `chart.py`
- Reusable tooltip, grid, and axis functions
- Color scheme matches application theme

### Styling Approach
- Tailwind utility classes for all styling
- Responsive breakpoints (sm, md, lg)
- Dark mode variants throughout
- Consistent spacing and color patterns