# 🛒 Amazon Clone — Full Stack E-Commerce Web Application

<div align="center">

![Amazon Clone](https://img.shields.io/badge/Django-5.1.4-green?logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![GitHub stars](https://img.shields.io/github/stars/Chaitanya8822/amazon?style=social)

**A production-inspired full-stack e-commerce platform built with Django & Bootstrap 5**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Chaitanya8822/amazon)

> 🌐 **Live Demo:** [https://amazon-clone-chaitanya.onrender.com](https://amazon-clone-chaitanya.onrender.com)

</div>

---

## 📸 Screenshots

| Homepage | Products | Cart |
|----------|----------|------|
| ![Home](media/categories/electronics.jpg) | ![Products](media/categories/fashion.jpg) | ![Cart](media/categories/home-kitchen.jpg) |

---

## 🎯 Features

### 👤 User Module
- ✅ User Registration & Login / Logout
- ✅ Personalized Profile Management (name, address, phone)
- ✅ Secure Session Authentication

### 🛍️ Product Module
- ✅ Product Listing with Grid View
- ✅ Product Detail Page with Buy Box
- ✅ Category-wise Filtering (6 categories)
- ✅ Search by Name & Description
- ✅ Sort by Price (Low→High / High→Low) & Newest
- ✅ Discount Badges (% off)
- ✅ Related Products Section

### 🛒 Cart Module
- ✅ Add to Cart (from product list & detail)
- ✅ Remove from Cart
- ✅ Update Quantity (auto-submit)
- ✅ Session-based Cart (no login required to browse)
- ✅ Real-time Cart Count Badge in Navbar

### 📦 Order Module
- ✅ Checkout with Shipping Address Form
- ✅ Cash on Delivery Payment
- ✅ Order History with Status Badges
- ✅ Order Detail with Tracking Timeline
- ✅ Price Snapshot at time of order

### 🧑‍💼 Admin Panel
- ✅ Add/Edit/Delete Products with inline price editing
- ✅ Manage Categories
- ✅ View & Update Order Status
- ✅ Order Items inline view
- ✅ User Profile management

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.10+, Django 5.1.4 |
| **Frontend** | HTML5, CSS3, Bootstrap 5.3, Bootstrap Icons |
| **Database** | SQLite (dev) / PostgreSQL (prod) |
| **Auth** | Django built-in + custom `UserProfile` (signals) |
| **Static Files** | WhiteNoise |
| **Media** | Pillow (ImageField) |
| **Forms** | django-crispy-forms + crispy-bootstrap5 |
| **Deployment** | Render.com / Gunicorn |

---

## 🏗️ Project Architecture (MVT)

```
amazon/
│
├── amazon_project/        ← Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/              ← User auth & profile
│   ├── models.py          → UserProfile (OneToOne with User)
│   ├── views.py           → register, login, logout, profile
│   ├── forms.py           → UserRegisterForm, ProfileUpdateForm
│   └── signals.py         → auto-create UserProfile on User save
│
├── products/              ← Product catalog
│   ├── models.py          → Category, Product (with discount_price)
│   ├── views.py           → home, product_list, product_detail, category_detail
│   └── context_processors.py → injects all_categories globally
│
├── cart/                  ← Session-based shopping cart
│   ├── cart.py            → Cart class (add/remove/update/iter)
│   ├── views.py           → cart_detail, cart_add, cart_remove, cart_update
│   └── context_processors.py → injects cart into all templates
│
├── orders/                ← Checkout & order management
│   ├── models.py          → Order, OrderItem (price snapshot)
│   ├── views.py           → checkout, order_history, order_detail
│   └── forms.py           → CheckoutForm
│
├── templates/             ← All HTML templates
│   ├── base.html          ← Amazon-style navbar, messages, footer
│   ├── home.html          ← Hero, categories, featured, latest
│   ├── accounts/          ← login, register, profile
│   ├── products/          ← product_list, product_detail, category_detail
│   ├── cart/              ← cart.html
│   └── orders/            ← checkout, order_history, order_detail
│
├── static/
│   ├── css/style.css      ← Custom Amazon-inspired styles
│   └── js/main.js         ← Auto-alerts, back-to-top, cart UX
│
├── media/                 ← Uploaded/downloaded images
├── seed_data.py           ← Seeds 6 categories + 20 products
├── download_images.py     ← Downloads product images from picsum
├── Procfile               ← Gunicorn for production
├── render.yaml            ← One-click Render deployment
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+
- pip
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Chaitanya8822/amazon.git
cd amazon
```

### 2. Create & Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Seed Sample Data (Categories + Products)
```bash
python seed_data.py
```

### 6. Download Product Images
```bash
python download_images.py
```

### 7. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 8. Start Development Server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**  
Admin: **http://127.0.0.1:8000/admin/**

---

## 🚀 Deployment (Render.com)

### Option A — One-Click Deploy
Click the button below:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Chaitanya8822/amazon)

### Option B — Manual Deploy to Render
1. Go to [render.com](https://render.com) and create a free account
2. Click **New → Web Service**
3. Connect your GitHub repo: `Chaitanya8822/amazon`
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`
   - **Start Command:** `gunicorn amazon_project.wsgi --log-file -`
5. Add Environment Variables:
   | Key | Value |
   |-----|-------|
   | `SECRET_KEY` | (generate a random key) |
   | `DEBUG` | `False` |
   | `ALLOWED_HOSTS` | `.onrender.com` |
6. Click **Deploy**

---

## 🌐 URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | `home` | Homepage with hero & products |
| `/products/` | `product_list` | All products with search/filter |
| `/products/<slug>/` | `product_detail` | Product detail page |
| `/products/category/<slug>/` | `category_detail` | Category products |
| `/cart/` | `cart_detail` | Shopping cart |
| `/cart/add/<id>/` | `cart_add` | Add to cart (POST) |
| `/cart/remove/<id>/` | `cart_remove` | Remove from cart (POST) |
| `/accounts/register/` | `register_view` | User registration |
| `/accounts/login/` | `login_view` | User login |
| `/accounts/profile/` | `profile_view` | Edit profile |
| `/orders/checkout/` | `checkout` | Place order |
| `/orders/history/` | `order_history` | Past orders |
| `/orders/<id>/` | `order_detail` | Order details |
| `/admin/` | Django Admin | Admin panel |

---

## 📊 Database Models

```
User (Django built-in)
  └─ UserProfile [OneToOne] — phone, address, city, state, pincode

Category — name, slug, description, image
  └─ Product — name, slug, price, discount_price, stock, available, featured

Order (user FK) — status, address fields, paid
  └─ OrderItem — product FK, product_name (snapshot), price (snapshot), qty
```

---

## 🚀 Future Enhancements

- [ ] 💳 Payment Gateway (Razorpay / Stripe)
- [ ] ❤️ Wishlist Feature
- [ ] ⭐ Product Reviews & Ratings
- [ ] 🤖 AI-based Product Recommendations
- [ ] 📄 Pagination for large catalogs
- [ ] 📧 Email notifications for orders
- [ ] 🌐 REST API (Django REST Framework)
- [ ] 📱 Progressive Web App (PWA)

---

## 🧑‍💻 Author

**Chaitanya**  
GitHub: [@Chaitanya8822](https://github.com/Chaitanya8822)

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/Chaitanya8822/amazon?style=for-the-badge&logo=github)](https://github.com/Chaitanya8822/amazon/stargazers)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).