# KH-Eghtesadino

A personal finance desktop application built for university students to track income, manage expenses, set savings goals, and receive intelligent budgeting insights — all in a clean, modern interface.

## Description

KH-Eghtesadino is a Python desktop app that helps students take control of their finances. It provides real-time balance tracking, spending analysis with velocity indicators, monthly comparison reports, recurring expense detection, and goal progress estimation. The app features a secure authentication system with encrypted storage, a dark/light theme engine, and DPI-aware scaling that adapts to any screen size.

## Features

### Core
- **User Authentication** — Registration and login with salted PBKDF2-SHA256 password hashing
- **Transaction Management** — Add income and expense transactions with categories and descriptions
- **Balance Dashboard** — Real-time balance, income, and expense overview
- **Goal Tracking** — Create savings goals, allocate funds, and monitor progress with estimated completion dates

### Analytics & Insights
- **Spending Insights** — Daily average, top categories, savings rate, and spending velocity (increasing / stable / decreasing)
- **Monthly Comparison** — Side-by-side current vs. previous month with percentage change indicators
- **Monthly Trend** — 6-month historical table of income, expenses, and balance
- **Category Breakdown** — Expense distribution with text-based bar charts
- **Recurring Expense Detection** — Automatic identification of categories active across multiple months
- **Budget Alerts** — Smart notifications for low savings, rising spending, and goal milestones

### UX & Customization
- **Dark / Light Theme** — Toggle between palettes with live preview
- **DPI-Aware Scaling** — Automatic screen-resolution scaling with manual override
- **Compact Layout Mode** — Reduce padding for smaller screens
- **Learning Corner** — Student-friendly financial tips and actionable recommendations
- **Privacy Mode** — Toggle-able privacy setting per account

## Screenshots

<!-- Replace the placeholders below with actual screenshots -->

| Login | Dashboard |
|:-----:|:---------:|
| ![Login Screen](screenshots/login.png) | ![Dashboard](screenshots/dashboard.png) |

| Reports | Settings |
|:-------:|:--------:|
| ![Reports Screen](screenshots/reports.png) | ![Settings Screen](screenshots/settings.png) |

> **Note:** Add your screenshots to a `screenshots/` directory at the project root.

## Technologies

| Layer | Technology |
|-------|------------|
| Language | Python 3.10+ |
| GUI Framework | [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) |
| Database | SQLite 3 (via `sqlite3` stdlib) |
| Password Hashing | PBKDF2-HMAC-SHA256 (200 000 iterations) |
| Field Encryption | XOR stream cipher with PBKDF2-derived key |
| Theme Engine | Custom `ThemeManager` singleton with listener pattern |
| Scaling | DPI-based auto-scaling with `sv()` helper |

## Architecture

```
┌──────────────────────────────────────────────────┐
│                     main.py                      │
│         FinancialApp  (screen router)            │
└──────────┬────────────┬────────────┬─────────────┘
           │            │            │
    ┌──────▼──┐  ┌──────▼──┐  ┌─────▼─────┐
    │ Screens │  │ Models  │  │   Utils   │
    │ (UI)    │  │ (Logic) │  │ (Shared)  │
    └─────────┘  └─────────┘  └───────────┘
```

- **Screens** — Each screen is a self-contained class that builds its own UI tree and exposes `refresh_ui()`. The app router hides/shows screens via `pack`/`pack_forget`.
- **Models** — `FinancialAdvisor` is a single facade owning all database operations. No other module touches SQLite directly.
- **Utils** — `COLORS` (theme-aware palette), `sv()` (DPI scaling), `ICONS` (Unicode map), `font()` helper, and reusable UI components (`Card`, `TitleLabel`, `MutedLabel`, etc.).

## Installation

### Prerequisites
- Python 3.10 or later
- `pip` package manager

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Itsahoora/Eghtesadino-Finance-App-.git
cd Eghtesadino-Finance-App-

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows

# 3. Install dependencies
pip install customtkinter

# 4. Run the application
python main.py
```

The SQLite database (`financial_data.db`) is created automatically on first launch.

## Usage

1. **Register** a new account from the login screen.
2. **Sign in** with your credentials.
3. **Add transactions** using the form at the bottom of the dashboard — pick income/expense, category, amount, and description.
4. **Create savings goals** via the "Add Goal" button and allocate funds toward them.
5. **View Reports** for monthly comparison, category breakdown, recurring expenses, and spending insights.
6. **Customize** theme, privacy mode, and layout from Settings.

## Project Structure

```
Eghtesadino-Finance-App-/
├── main.py                        # Application entry point
├── models/
│   ├── __init__.py
│   └── financial_advisor.py       # Business logic & database layer
├── screens/
│   ├── __init__.py
│   ├── login_screen.py            # Authentication UI
│   ├── dashboard_screen.py        # Main hub: balance, transactions, goals
│   ├── reports_screen.py          # Analytics & reporting
│   ├── settings_screen.py         # Theme, privacy, display settings
│   └── add_goal_screen.py         # Goal creation form
├── utils/
│   ├── __init__.py
│   ├── constants.py               # Categories, icons, spacing tokens
│   ├── colors.py                  # Theme-aware color accessor
│   ├── scale.py                   # DPI scaling utilities
│   ├── theme_manager.py           # Theme singleton (dark/light toggle)
│   ├── ui_components.py           # Reusable widgets (Card, Labels, etc.)
│   └── theme/
│       ├── __init__.py
│       ├── colors.py              # Light & dark color palettes
│       └── sizes.py               # Design tokens (font sizes, radii)
├── tests/
│   ├── test_financial_features.py # Unit tests for core features
│   └── run_theme_tests.py         # Theme smoke tests
├── .gitignore
└── README.md
```

## Security Features

- **Password Hashing** — Passwords are hashed with PBKDF2-HMAC-SHA256 using a random 16-byte salt per user and 200 000 iterations. Plaintext passwords are stored only for backward compatibility with older accounts.
- **Field-Level Encryption** — Transaction categories and descriptions are encrypted at rest using an XOR stream cipher with a key derived from PBKDF2 (120 000 iterations), the user's salt, and an application pepper.
- **SQL Injection Prevention** — All database queries use parameterized statements.
- **Configurable Pepper** — The encryption pepper can be overridden via the `EGHTESADINO_PEPPER` environment variable.

## Future Improvements

- Export reports to CSV / PDF
- Budget limits per category with visual indicators
- Recurring income detection
- Multi-currency support
- Data backup and restore
- Chart-based visualizations (matplotlib integration)
- Mobile companion app

## Contributing

Contributions are welcome. To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Please ensure all existing tests pass before submitting:

```bash
python tests/test_financial_features.py
python tests/run_theme_tests.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Ahoora** — [Itsahoora](https://github.com/Itsahoora)

*Built for students at Kharazmi University*
