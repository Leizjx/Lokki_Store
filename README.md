# LOKKI Phone Store

A Django-based e-commerce website for selling mobile phones.

## Features

- **Product Management**
  - Browse phones by brands
  - Detailed product information
  - Product search functionality
  - Product images and specifications

- **Shopping Cart**
  - Add/remove items
  - Update quantities
  - View cart summary
  - Free shipping for orders over $500

- **User Management**
  - User registration and authentication 
  - Personal profile management
  - Order history tracking
  - Shopping cart persistence

- **Checkout Process**
  - Shipping information collection
  - Multiple payment methods
  - Order confirmation
  - Order status tracking

## Installation

1. Clone the repository:
```sh
git clone <repository-url>
cd phone_store
```

2. Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```sh
pip install -r requirements.txt
```

4. Apply database migrations:
```sh
python manage.py migrate
```

5. Create a superuser:
```sh
python manage.py createsuperuser
```

6. Run the development server:
```sh
python manage.py runserver
```

## Project Structure

```
phone_store/
├── manage.py
├── media/
│   ├── brands/      # Brand logos
│   └── phones/      # Product images
├── phone_store/     # Project settings
└── store/           # Main application
    ├── models.py    
    ├── views.py
    ├── urls.py
    └── templates/   # HTML templates
```

## Technologies Used

- Django
- Bootstrap 5
- Font Awesome
- SQLite3
- HTML/CSS/JavaScript

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
