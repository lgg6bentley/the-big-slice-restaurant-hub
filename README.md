# The Big Slice Restaurant Hub

![The Big Slice Menu Screenshot]![The Big Slice Menu Screenshot](https://raw.githubusercontent.com/lgg6bentley/the-big-slice-restaurant-hub/main/the_big_slice_menu.png)

## Project Overview

The Big Slice Restaurant Hub is a web application designed to showcase a dynamic menu for a restaurant. This project serves as a practical demonstration of building a RESTful API with Django REST Framework and consuming it with a client-side rendered frontend using plain HTML, CSS (Tailwind CSS), and JavaScript. It provides a clean, responsive display of menu items fetched directly from a backend API.

This project was developed as an MVP (Minimum Viable Product) to demonstrate core web development skills, particularly in backend API development, static file management, and client-side data fetching.

## Features

* **Dynamic Menu Display:** Fetches menu items from a Django REST API and renders them dynamically on the frontend.
* **Custom Logo Integration:** Displays "The Big Slice" brand logo, served as a static file.
* **API-Driven Content:** All menu item details (name, category, description, price, availability) are managed via the Django backend API.
* **Placeholder Image Generation:** Automatically generates a text-based placeholder image for each menu item if a specific image is not provided.
* **Specific Item Image:** Demonstrates custom image handling for a particular menu item ("The Big Pepperoni").
* **Responsive Design:** Utilizes Tailwind CSS for a modern and adaptable user interface across different screen sizes.

## Technologies Used

**Backend:**
* **Python**
* **Django 5.0:** Web framework for the backend logic and API.
* **Django REST Framework:** For building the powerful and flexible RESTful API.
* **SQLite3:** Default database for development.

**Frontend:**
* **HTML5:** Structure of the web page.
* **CSS (Tailwind CSS CDN):** Utility-first CSS framework for rapid styling.
* **JavaScript (Vanilla JS):** For fetching data from the API and dynamically rendering menu items.

**Development Tools:**
* **Git:** Version control.
* **GitHub:** Repository hosting.
* **Virtual Environments:** For managing Python dependencies.

## Installation and Setup

Follow these steps to get a local copy of the project up and running on your machine.

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* Git

### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/lgg6bentley/the-big-slice-restaurant-hub.git](https://github.com/lgg6bentley/the-big-slice-restaurant-hub.git)
    cd the-big-slice-restaurant-hub
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    # (You might need to create this file if you haven't. Run: pip freeze > requirements.txt)
    ```
4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations restaurant_api
    python manage.py migrate
    ```
5.  **Create a superuser (optional, but recommended for admin access):**
    ```bash
    python manage.py createsuperuser
    # Follow the prompts to set username, email, and password.
    ```
6.  **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```
    The backend API will be accessible at `http://127.0.0.1:8000/api/` and the Django Admin at `http://127.0.0.1:8000/admin/`.

### Frontend Access

Once the Django server is running, you can access the menu frontend directly in your browser:

* **Open your browser and navigate to:** `http://127.0.0.1:8000/api/menu_frontend/`

## Usage

* **View Menu:** Open the frontend URL (`http://127.0.0.1:8000/api/menu_frontend/`) to see the dynamically loaded menu items.
* **Manage Menu Items (Admin):** Log in to the Django Admin (`http://127.0.0.1:8000/admin/`) using your superuser credentials to add, edit, or delete menu items. Changes made here will instantly reflect on the public menu page.

## API Endpoints

The project exposes a simple REST API for menu management:

* `GET /api/menu/`: Retrieve a list of all menu items.
* `GET /api/menu/<id>/`: Retrieve details for a specific menu item.
* *(Additional endpoints for POST, PUT, DELETE would be available if full CRUD was exposed, but for a public menu, GET is primary.)*

## Static Files

* Project-level static files (like the logo and `pepperoni_pizza.jpg`) are configured in `settings.py` using `STATICFILES_DIRS`.
* These are served by Django's development server when `DEBUG=True`.

## Future Enhancements (Potential Ideas)

* **Image Uploads:** Implement a robust image upload system for menu items directly through the Django Admin.
* **Ordering System:** Add functionality for customers to add items to a cart and place orders.
* **User Authentication:** Implement user registration and login for specific roles (e.g., staff, customers).
* **Search and Filters:** Add search functionality and filters for menu categories.
* **Deployment:** Prepare the application for production deployment (e.g., using Gunicorn/Nginx, Docker).
* **More Comprehensive Testing:** Add unit and integration tests for both backend and frontend.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details (if you plan to add one).

## Contact

Bentley - https://www.linkedin.com/in/bentley-bond-89b39a375/ - lgg6bentley@gmail.com

Project Link: [https://github.com/lgg6bentley/the-big-slice-restaurant-hub](https://github.com/lgg6bentley/the-big-slice-restaurant-hub)

---
