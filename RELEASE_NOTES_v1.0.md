# Release Notes: KH-Eghtesadino v1.0.0

**Release Date:** January 18, 2026  
**Version:** 1.0.0  
**Status:** Stable Release

---

## Overview

KH-Eghtesadino v1.0.0 is the initial stable release of a personal finance desktop application designed specifically for university students. This release provides core financial management features with a modern, secure, and user-friendly interface.

---

## What's New

### Core Features

#### User Authentication
- **Secure Registration** — Create accounts with username and password
- **PBKDF2-SHA256 Hashing** — Passwords encrypted with 200,000 iterations
- **Salt-Based Security** — Random 16-byte salt per user
- **Backward Compatibility** — Legacy password support

#### Transaction Management
- **Income & Expense Tracking** — Record all financial transactions
- **Category System** — Predefined categories for food, transport, education, and more
- **Custom Descriptions** — Add notes to each transaction
- **Encrypted Storage** — Sensitive data protected at rest

#### Balance Dashboard
- **Real-Time Overview** — Current balance, income, and expenses
- **Quick Stats** — At-a-glance financial summary
- **Transaction History** — Recent activity with filtering

#### Savings Goals
- **Goal Creation** — Set targets with deadlines
- **Fund Allocation** — Transfer funds from balance to goals
- **Progress Tracking** — Visual progress indicators
- **Time Estimates** — Predicted completion dates

### Analytics & Insights

#### Spending Insights
- **Daily Average** — Calculate average daily spending
- **Top Categories** — Identify where money goes
- **Savings Rate** — Track percentage saved
- **Spending Velocity** — Detect increasing/decreasing trends
- **Monthly Projections** — Forecast end-of-month balance

#### Monthly Comparison
- **Current vs. Previous** — Side-by-side month comparison
- **Percentage Changes** — Track improvement or decline
- **Income/Expense/Balance** — Full financial picture

#### Monthly Trend
- **6-Month History** — Long-term financial view
- **Income Trends** — Track earning patterns
- **Expense Trends** — Monitor spending habits
- **Balance Trends** — Overall financial health

#### Category Breakdown
- **Expense Distribution** — See where money goes
- **Visual Bar Charts** — Text-based visualization
- **Percentage Allocation** — Understand spending proportions

#### Recurring Expense Detection
- **Automatic Detection** — Identify regular expenses
- **Monthly Averages** — Calculate typical spending
- **Total Totals** — See overall recurring costs

#### Budget Alerts
- **Low Savings Warning** — Alert when savings rate drops
- **Rising Spending** — Notify when expenses increase
- **Goal Milestones** — Celebrate achievements
- **Smart Recommendations** — Actionable financial advice

### UX & Customization

#### Dark/Light Theme
- **Toggle Switch** — Instant theme change
- **Live Preview** — See changes immediately
- **Persistent Setting** — Theme remembered per user

#### DPI-Aware Scaling
- **Automatic Detection** — Adapts to screen resolution
- **Manual Override** — Adjust scaling in settings
- **Cached Performance** — Smooth scaling without lag

#### Compact Layout
- **Reduced Padding** — Better for smaller screens
- **Toggle Setting** — Enable/disable in settings

#### Learning Corner
- **Financial Tips** — Student-friendly advice
- **Needs vs Wants** — Basic budgeting concepts
- **Saving Goals** — How to save effectively
- **School Budgeting** — Managing student finances

#### Privacy Mode
- **Toggle Setting** — Enable/disable per account
- **Data Protection** — Enhanced privacy when enabled

### Security Features

- **PBKDF2-SHA256** — Industry-standard password hashing
- **Field-Level Encryption** — XOR cipher for sensitive data
- **SQL Injection Prevention** — Parameterized queries
- **Configurable Pepper** — Environment variable support
- **Secure Defaults** — Safe out-of-the-box configuration

---

## Installation

### Prerequisites
- Python 3.10 or later
- pip package manager

### Quick Install
```bash
git clone https://github.com/Itsahoora/Eghtesadino-Finance-App-.git
cd Eghtesadino-Finance-App-
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## Known Issues

1. **Chart Visualizations** — Text-based only, no graphical charts
2. **Data Export** — CSV/PDF export not yet available
3. **Multi-Currency** — Single currency support only
4. **Mobile Companion** — Desktop only

---

## Upgrade Instructions

This is the initial release. No upgrade path required.

---

## Support

- **Documentation** — See [README.md](../README.md)
- **Issues** — Report bugs via [GitHub Issues](https://github.com/Itsahoora/Eghtesadino-Finance-App-/issues)
- **Contributing** — See [CONTRIBUTING.md](../CONTRIBUTING.md)

---

## Acknowledgments

- **CustomTkinter** — Modern UI framework
- **Python Community** — Excellent documentation and tools
- **University Students** — Target users and feedback

---

## What's Next (v1.1.0)

- [ ] CSV/PDF Export
- [ ] Graphical Charts (matplotlib)
- [ ] Budget Limits per Category
- [ ] Recurring Income Detection
- [ ] Multi-Currency Support
- [ ] Data Backup/Restore
- [ ] Mobile Companion App

---

**Thank you for using KH-Eghtesadino!**

*Built for students, by students*
