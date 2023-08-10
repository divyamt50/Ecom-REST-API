# E-Commerce REST API with Django

This project is an e-commerce REST API built using Django. It provides endpoints for managing products, users, orders, and more.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Product management (CRUD operations)
- Shopping cart functionality
- Order placement and history
- User profiles and settings

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ecommerce-rest-api.git
   cd ecommerce-rest-api
   ```
## Installation

1. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure your database settings in `settings.py`.

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

To interact with the API, you can use tools like `curl`, Postman, or your favorite API testing tool.

## API Endpoints

Here are some of the main API endpoints:

- **GET /api/products/**: Get a list of all products.
- **GET /api/products/<product_id>/**: Get details about a specific product.
- **POST /api/cart/add/**: Add a product to the shopping cart.
- **GET /api/cart/**: Get the contents of the shopping cart.
- **POST /api/orders/create/**: Place a new order.
- ...

For a complete list of endpoints and their descriptions, refer to the [API Documentation](api_documentation.md).

## Authentication

Authentication is required for most endpoints. You can authenticate using the token-based authentication provided by Django REST framework. Include the token in the request headers:

```http
Authorization: Token your_token_here
```
