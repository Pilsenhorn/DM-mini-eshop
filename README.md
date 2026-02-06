
# DM Mini E-shop (Django)

Minimalistic Django-based mini e-shop with landing page and lead collection.
The project is designed as a real-world MVP for a small personal brand, with focus on clean architecture, low friction UX, and future scalability.

---

Features

Landing & Marketing

- Landing page as homepage
- Email lead collection
- Thank you page after submission
- Leads stored separately from users and orders
- Admin overview of collected emails

E-shop Core

- Product types:

  - Digital products
  - Physical products
  - Services
- Orders and order items
- Order status workflow
- Admin management of products and orders

Soft User Registration:

- No mandatory registration for customers
- User account is created automatically during checkout
- No password required at order time
- Prepared for future account activation and order history

UI:

- Django templates
- Tailwind CSS via CDN
- Custom design tokens via CSS variables
- No frontend build process

---

 Architecture Overview:

- Django monolith
  - Templates for frontend
  - Models for business logic
  - Admin for content and order management
- Clear separation of concerns:
  - `leads` – marketing contacts
  - `products` – catalog
  - `orders` – orders and order items
  - `users` – user profiles
- Designed to be easily extended with:
  - Payments
  - Customer dashboards
  - Digital downloads
  - Email automation

---

Project Structure:

denisa_shop/
├─ core/ # Django settings & URLs
├─ leads/ # Landing page & email leads
├─ products/ # Product catalog
├─ orders/ # Orders & checkout logic
├─ users/ # User profiles (soft registration)
├─ templates/ # HTML templates
├─ static/ # CSS (design tokens)
└─ manage.py

Tech Stack:

- Python
- Django
- SQLite (development)
- Tailwind CSS (CDN)
- HTML / CSS
- Git & GitHub
