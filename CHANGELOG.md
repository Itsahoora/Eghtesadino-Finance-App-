# Changelog

All notable changes to Eghtesadino will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-18

### Added

#### Core Features
- User registration and authentication with PBKDF2-SHA256 password hashing
- Transaction management (income/expense tracking)
- Real-time balance dashboard
- Savings goal creation and tracking
- Goal fund allocation

#### Analytics & Insights
- Spending insights with daily average and spending velocity
- Monthly comparison (current vs. previous month)
- 6-month historical trend analysis
- Category breakdown with visual bar charts
- Recurring expense detection
- Budget alerts for low savings and rising spending

#### UX & Customization
- Dark/Light theme toggle with live preview
- DPI-aware automatic scaling
- Manual scale override in settings
- Compact layout mode
- Learning corner with financial tips
- Privacy mode toggle

#### Security
- PBKDF2-HMAC-SHA256 password hashing (200,000 iterations)
- Field-level XOR encryption for sensitive data
- SQL injection prevention with parameterized queries
- Configurable encryption pepper via environment variable

#### Architecture
- Modular screen-based UI architecture
- Single-facade business logic pattern
- Theme manager singleton with listener pattern
- Reusable UI component library

#### Testing
- Unit tests for core financial features
- Theme smoke tests
- CI pipeline with GitHub Actions

#### Documentation
- Comprehensive README with screenshots
- Contributing guidelines
- Issue and PR templates
- Repository review documentation

### Security
- Passwords stored with salted PBKDF2-SHA256 hashing
- Transaction data encrypted at rest
- All database queries use parameterized statements
