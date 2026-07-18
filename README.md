# KH-Eghtesadino

:::This file is made by AI:::
**Ghasr Eghtesadi** — Personal Finance Management Desktop Application

A desktop application for tracking income, expenses, and financial goals. Built with Python and CustomTkinter for a modern, responsive UI.

**Private Repository** — Team access only

---

## Table of Contents

- [KH-Eghtesadino](#kh-eghtesadino)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Project Structure](#project-structure)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the App](#running-the-app)
  - [Development](#development)
    - [Project Layout](#project-layout)
    - [Database Schema](#database-schema)
    - [Theme System](#theme-system)
    - [Scaling \& UI Components](#scaling--ui-components)
  - [Testing](#testing)
    - [Manual Testing Checklist](#manual-testing-checklist)
  - [Troubleshooting](#troubleshooting)
    - [Application won't start](#application-wont-start)
    - [Theme not changing](#theme-not-changing)
    - [Database errors](#database-errors)
    - ["CTkTextbox not available" error](#ctktextbox-not-available-error)
  - [Team Guidelines](#team-guidelines)
    - [Branching \& Commits](#branching--commits)
    - [Code Style](#code-style)
    - [Pull Requests](#pull-requests)
    - [Adding New Features](#adding-new-features)
    - [Database Changes](#database-changes)
  - [Future Enhancements](#future-enhancements)
  - [License](#license)
  - [Questions or Issues?](#questions-or-issues)

---

## Features

- **User Authentication**: Secure login and registration
- **Dashboard**: Quick overview of balance, recent transactions, and goals
- **Transaction Management**: Add income and expense transactions with categories
- **Goal Tracking**: Set financial goals and track progress with visual progress bars
- **Reports**: View expense breakdown by category over 30 days
- **Dark/Light Theme**: Toggle between themes (dark theme includes full UI color overrides)
- **Settings**: User preferences and theme management
- **Local Storage**: SQLite database for persistent data

---

## Project Structure

```
.
├── main.py                          # Application entry point
├── financial_data.db               # SQLite database (auto-created)
├── user_theme.json                 # Theme preference storage
├── models/
│   ├── __init__.py
│   └── financial_advisor.py        # Business logic (users, transactions, goals, stats)
├── screens/
│   ├── __init__.py
│   ├── login_screen.py             # Login/registration UI
│   ├── dashboard_screen.py         # Main dashboard with balance, goals, recent transactions
│   ├── reports_screen.py           # Expense reports and statistics
│   ├── settings_screen.py          # User settings and theme toggle
│   └── advice_screen.py            # (Optional) Financial advice placeholder
├── utils/
│   ├── __init__.py
│   ├── colors.py                   # Theme color adapter (light/dark mode aware)
│   ├── constants.py                # App constants (categories, window size)
│   ├── scale.py                    # DPI-aware scaling for responsive UI
│   ├── theme_manager.py            # Theme state and persistence
│   ├── ui_components.py            # Reusable themed UI widgets
│   └── theme/
│       ├── __init__.py
│       ├── colors.py               # Base color palette
│       └── sizes.py                # Base size tokens
├── tests/
│   └── run_theme_tests.py          # Theme smoke tests
├── README.md                        # This file
├── LICENSE                          # MIT License
└── .gitignore                       # Git ignore rules
```

---

## Getting Started

### Prerequisites

- **Python 3.8+** (tested on 3.13, 3.14)
- **pip** package manager
- **Virtual environment** (recommended)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Redstone-NFR/KH-Eghtesadino.git
   cd KH-Eghtesadino
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - **Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD):**
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install customtkinter
   ```

### Running the App

```bash
python main.py
```

The application window will open. Default credentials for testing:

- Username: `user` (create a new account to register)
- Password: any string (no validation currently)

---

## Development

### Project Layout

- **`models/`** — Business logic and data access
  - `financial_advisor.py`: SQLite wrapper for users, transactions, and goals
- **`screens/`** — UI screens (each uses `pack()` layout)
  - `login_screen.py`: Registration and login
  - `dashboard_screen.py`: Main hub with balance, goals, and transaction form
  - `reports_screen.py`: Expense category breakdown (last 30 days)
  - `settings_screen.py`: Theme toggle and other preferences
- **`utils/`** — Shared utilities
  - `colors.py`: Adapts base colors for light/dark modes
  - `ui_components.py`: Reusable widgets (Card, PillButton, ThemedLabel, etc.)
  - `theme_manager.py`: Manages theme mode and persistence
  - `scale.py`: DPI-aware scaling for responsive layout
  - `constants.py`: Income/expense categories, window dimensions

### Database Schema

The SQLite database (`financial_data.db`) includes three main tables:

**users**

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
)
```

**transactions**

```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    type TEXT,              -- 'income' or 'expense'
    category TEXT,          -- e.g., 'Salary', 'Food', 'Other'
    amount REAL,
    date TEXT,              -- ISO 8601 format
    description TEXT,       -- Custom note (especially for 'Other' category)
    FOREIGN KEY(user_id) REFERENCES users(id)
)
```

**goals**

```sql
CREATE TABLE goals (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    goal_name TEXT,
    target_amount REAL,
    current_amount REAL,
    deadline TEXT,          -- Optional; ISO 8601 format
    FOREIGN KEY(user_id) REFERENCES users(id)
)
```

### Theme System

The app supports **light** and **dark** themes:

1. **Color Mappings** (`utils/theme/colors.py`): Base RGBA tuples
2. **Adapter** (`utils/colors.py`): Maps base colors to dark-mode variants
3. **Manager** (`utils/theme_manager.py`): Persists preference in `user_theme.json`
4. **UI Components** (`utils/ui_components.py`): Themed widgets with automatic color application

To toggle theme, click the theme button in Settings.

### Scaling & UI Components

- **DPI-aware scaling** (`utils/scale.py`): All sizes adapt to screen DPI
- **Reusable components** (`utils/ui_components.py`):
  - `Card()` — Rounded container with background
  - `PillButton()` — Styled button with variants (primary, secondary, danger, etc.)
  - `TitleLabel()` — Bold header text
  - `ThemedLabel()` — Text color respects theme
  - `ThemedTextInput()` — Entry field respecting theme background

---

## Testing

Run the theme smoke tests to verify the app initializes without crashes:

```bash
python tests/run_theme_tests.py
```

Expected output:

```
All theme smoke tests passed
```

### Manual Testing Checklist

- [ ] Login/register with a new user
- [ ] Add income and expense transactions
- [ ] Verify categories update when switching transaction type
- [ ] Add a goal and check the progress bar displays
- [ ] Toggle theme (Dark ↔ Light) and verify UI colors update
- [ ] View Reports and check expense breakdown by category
- [ ] Update user details in Settings
- [ ] Delete your account (careful!)

---

## Troubleshooting

### Application won't start

- Ensure Python 3.8+ is installed: `python --version`
- Verify venv is active and CustomTkinter is installed: `pip list | grep -i customtkinter`
- Check for syntax errors: `python -m py_compile main.py`

### Theme not changing

- Delete `user_theme.json` to reset preferences
- Restart the app after toggling theme
- Verify `utils/colors.py` has the correct dark-mode overrides

### Database errors

- Delete `financial_data.db` to create a fresh database
- This will reset all users, transactions, and goals
- Restart the app

### "CTkTextbox not available" error

- Ensure CustomTkinter version supports CTkTextbox (latest versions do)
- Update: `pip install --upgrade customtkinter`

---

## Team Guidelines

### Branching & Commits

- Use feature branches: `git checkout -b feature/your-feature-name`
- Write clear commit messages: `fix: description` or `feat: description`
- Do not commit `__pycache__/`, `.venv/`, or `*.db` files (see `.gitignore`)

### Code Style

- Follow PEP 8
- Use descriptive variable and function names
- Add docstrings to classes and public methods
- Comment complex logic

### Pull Requests

- Describe what changed and why
- Test your changes before pushing: `python tests/run_theme_tests.py`
- Request review from at least one team member

### Adding New Features

1. Identify the relevant module(s) (model, screen, utils)
2. Add business logic to `models/financial_advisor.py` if needed
3. Add UI in the appropriate `screens/*.py` file
4. Use reusable components from `utils/ui_components.py`
5. Test locally: `python main.py`
6. Run tests: `python tests/run_theme_tests.py`
7. Commit and push

### Database Changes

- **Adding a column**: Update `init_database()` in `models/financial_advisor.py`
- **Adding a table**: Add a `CREATE TABLE` statement in `init_database()`
- **Migrations**: Document breaking schema changes in a migration guide (if applicable)

---

## Future Enhancements

- [ ] Budget management and alerts
- [ ] Recurring transactions
- [ ] Export to CSV/PDF
- [ ] Multi-language support
- [ ] Data visualization (charts/graphs)
- [ ] Cloud sync (optional)
- [ ] Mobile companion app

---

## License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## Questions or Issues?

Contact the team or refer to the troubleshooting section above.
