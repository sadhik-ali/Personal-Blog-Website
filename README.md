# 📝 Personal Blog Website (Django)

A full-featured personal blog website built using Django framework. This platform allows authors to publish posts with rich content, categorize them, tag them, and enable users to comment. Admin panel is customized for advanced content management.

---

## 🔥 Features

* 📟 Create, read, update, delete blog posts
* 🗒️ Categories and tags for posts
* 🖼️ Featured image support
* 💬 Commenting system with spam protection
* 🎨 Fully responsive front-end
* 📊 Custom Django Admin panel
* ⚙️ Django messages + SweetAlert for clean UX

---

## 📂 Project Structure

```
blog/
├── blog/                  # Project configuration
├── posts/                 # Blog app (views, models, forms, admin, etc.)
│   ├── templates/blog/    # All HTML templates
│   ├── static/            # Static files (CSS, JS)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
├── media/                 # Uploaded media files
├── manage.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sadhik-ali/Personal-Blog-Website.git
cd Personal-Blog-Website
```

### 2. Set up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Start Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠 Technologies Used

* Python 3.x
* Django 4.x
* SQLite (can be switched to PostgreSQL)
* Bootstrap 5
* SweetAlert2
* Crispy Forms (optional)

---

## ✨ Screenshots

| Page        | Preview                           |
| ----------- | --------------------------------- |
| Home Page   | ![Home](screenshots/home.png)     |
| Post Detail | ![Detail](screenshots/detail.png) |
| Admin Panel | ![Admin](screenshots/admin.png)   |

*(Upload these images to a `screenshots/` folder in your repo.)*

---

## 💡 Features In-Depth

### ✅ Blog Posts

* Title, slug, content, featured image
* Author, created date
* SEO-friendly URLs (`/post/your-title/`)

### ✅ Categories & Tags

* Group posts by category or multiple tags
* Dynamic pages for each category/tag

### ✅ Comments

* User-friendly comment form
* Success alert with SweetAlert
* Stored securely in the database

### ✅ Admin Panel

* Custom admin for managing posts, comments, categories
* Inline editing, filter by author, etc.

---

## 🧪 Testing

To run tests:

```bash
python manage.py test
```


## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

---

## 📧 Contact

Developed by \[Your Name]
📩 Email: [sadhikali0867@gmail.com](mailto:sadhikali0867@gmail.com)
📸 Instagram: [@sadhiqq__ali](https://www.instagram.com/sadhiqq__ali/)

---
