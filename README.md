# Coffee Shop Challenge

A Python implementation of a Coffee Shop domain model with Customer, Coffee, and Order relationships.

## Domain Model

The application implements a Coffee Shop domain with three main models:

- **Customer**: Represents a coffee shop customer
- **Coffee**: Represents a type of coffee
- **Order**: Represents a customer's order for a specific coffee

### Relationships

- Coffee has many Orders (one-to-many)
- Customer has many Orders (one-to-many)
- Order belongs to both a Customer and a Coffee (many-to-one)
- Coffee and Customer have a many-to-many relationship through Orders

## Features

### Customer Class

- Name validation (1-15 characters)
- Order tracking
- Unique coffee list retrieval
- Order creation
- Most aficionado calculation (bonus feature)

### Coffee Class

- Name validation (minimum 3 characters)
- Immutable name property
- Order tracking
- Unique customer list retrieval
- Order count
- Average price calculation

### Order Class

- Price validation (1.0-10.0)
- Immutable properties
- Type checking for Customer and Coffee
- Automatic relationship management

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd coffee-shop-challenge
```

2. Install dependencies using pipenv:

```bash
pipenv install
```

## Usage

### Running Tests

```bash
pipenv run pytest
```

### Running the Debug Script

```bash
pipenv run python debug.py
```

## Project Structure

```
coffee-shop-challenge/
├── Pipfile
├── setup.py
├── debug.py
├── coffee_shop_challenge/
│   ├── __init__.py
│   ├── customer.py
│   ├── coffee.py
│   └── order.py
└── tests/
    ├── __init__.py
    ├── customer_test.py
    ├── coffee_test.py
    └── order_test.py
```

## Implementation Details

### Single Source of Truth

- The `Order` class serves as the single source of truth for relationships
- When an Order is created, it automatically updates both the Customer's and Coffee's order lists
- Relationships are maintained through these lists with no duplicate data

### Data Validation

- Customer names must be 1-15 characters
- Coffee names must be at least 3 characters
- Order prices must be between 1.0 and 10.0
- All relationships are type-checked

### Immutability

- Coffee names are immutable after initialization
- Order properties (price, customer, coffee) are immutable
- Customer names can be changed but must meet validation requirements

## Testing

The project includes comprehensive test coverage for:

- Model initialization and validation
- Relationship management
- Property immutability
- Edge cases and error conditions
- Bonus features

## Requirements

- Python 3.8 or higher
- pytest for testing

## License

This project is licensed under the MIT License.
