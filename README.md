
# 🍽️ Tastee.lk – Restaurant Website

![Tastee.lk Home Page](https://i.imgur.com/WtUxTv3.jpeg)

Tastee.lk is a full-featured, responsive restaurant web application built with **Python Django**, **HTML**, **Tailwind CSS**, **JavaScript**, and **MySQL**. This platform offers a smooth and engaging user experience, combining a modern frontend, robust backend, and a clean admin dashboard. Ideal for restaurants to showcase their menu, manage orders, and engage with customers online.

---

## 🚀 Features

- 🔐 User Authentication (Login/Register)
- 🏠 Home Page with Image Slider and Category Highlights
- 📋 Menu Browsing with Category-Based Filtering
- ❤️ Add to Favourites Functionality
- 🛒 Cart and Food Ordering Workflow
- 📄 Dish Detail Pages with Images and Descriptions
- 🛠️ Admin Panel with Jazzmin Theme for Easy Management
- 🖼️ Image Upload and Display via Pillow
- 📦 Modular Template Structure with Reusable UI Components

---

## 🧰 Technologies Used

### Backend
- **Python 3**
- **Django**
- **MySQL**

### Frontend
- **HTML5**
- **Tailwind CSS**
- **CSS3**
- **JavaScript**

### Packages & Tools
- `pipenv` – Python package management
- `django-admin` – Django project and app management
- `mysqlclient` – MySQL database connector
- `pillow` – Image processing
- `jazzmin` – Customized Django admin interface

---

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/WINODH-PRSANNA/tastee.lk.git
   cd tastee.lk
   ```

2. **Set up virtual environment**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Configure the database**
   Update `settings.py` with your MySQL credentials.

4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   - Frontend: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributions

Feel free to fork this repository and contribute via pull requests. All contributions and suggestions are welcome!

---

## 📬 Contact

For any inquiries or feedback, reach out via [winodh.prasanna.blog@gmail.com].
