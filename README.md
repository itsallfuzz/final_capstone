# News2U - Django News Platform

A multi-user news platform built with Django that allows journalists to
create articles and newsletters, editors to review content, publishers
to distribute content, and readers to subscribe to their favorite
journalists and publishers.

# Features

- **Multi-role users**: Journalists, Editors, Publishers, and
Readers
- **Article workflow for Journalists**: Create → Submit to Editor →
Approve → Publish (independently or via publisher)
- **Newsletter system**: Create newsletters with multiple articles
- **Subscription system**: Readers can subscribe to journalists and
publishers
- **Email notifications**: Subscribers receive emails when content is
approved
- **Associations**: Journalists can submit to various editors and
publishers, Editors can work with various journalists and publishers,
publishers can work with various journalists and editors.
- **Admin approval**: All new users require admin approval before
accessing the system, i.e Journalists, Editors and Publishers need to
be approved by admin (superuser) but readers are immediately active. If
the application is to be monetised, the readers will only be able to
access content after payment.
- **API Endpoint** - Creating API endpoints for subscribing and
retrieving of articles and newsletters (See Planning Folder)


## User Roles

### Admin
- Superuser
- Logs in to Django Admin
- Can view ALL users
- Can view ALL publications
- Can add, edit, delete any content in the application

### Journalist
- Create and edit articles and newsletters
- View draft articles, revise articles and save for later
- Submit content to editors for review
- Publish articles and newsletters independently or through publishers
- View published articles and newsletters
- View subscribers and associated publishers
- Delete articles or newsletters

### Editor
- Review and approve/decline articles and newsletters
- Edit content before approval
- View published articles and newsletters
- Delete articles or newsletters

### Publisher
- Review journalist requests for publication
- Publish articles through their publication house
- Create newsletters
- View associated journalists and editors

### Reader
- Subscribe to journalists and publishers
- Receive email notifications for new content
- View published articles and newsletters

## Installation

### Prerequisites (Install requirements.txt)
- asgiref==3.10.0
- certifi==2025.11.12
- charset-normalizer==3.4.4
- crispy-bootstrap4==2025.6
- Django==4.2.16
- django-crispy-forms==2.5
- djangorestframework==3.16.1
- idna==3.11
- mysqlclient==2.2.7
- oauthlib==3.3.1
- pillow==12.0.0
- requests==2.32.5
- requests-oauthlib==2.0.0
- sqlparse==0.5.3
- urllib3==2.5.0
- Virtual environment (recommended)

### Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure email settings in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

5. Configure Twitter (X) settings and add your details:
```
In news2u/functions/tweet.py add:
CONSUMER KEY & CONSUMER_SECRET
```

6.Configure Django secret key
```bash
python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
```
Copy the generated key and paste it in `settings.py`:
```python
   SECRET_KEY = 'your-secret-key-here'
```

7. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

8. Set up user groups and permissions:
```bash
python manage.py setup_groups
```

9. Create a superuser for the admin role and application control after
migration to MariaDB:
```bash
python manage.py createsuperuser
```

10. Run the development server:
```bash
python manage.py runserver
```

11. Access the application at `http://127.0.0.1:8000/`


12. Run in Docker playground `https://labs.play-with-docker.com/`
Login, create a new instance and run the following commands line by line:
Pull the image from docker hub:
Run the container:
```bash
docker pull lizfuzy/news_app
docker run -p 8000:8000 lizfuzy/news_app
```

Go to Localhost:
'http://localhost:8000'
(Open port and enter 8000)


## Important Setup Notes

## Twitter
Twitter integration is disabled in the Dockerized version due to
interactive authentication requirements. To enable, add your API
keys and uncomment Tweet() in apps.py

## Docker Note
The Dockerised version uses SQLite instead of MariaDB for portability
and ease of deployment. The production version uses MariaDB.

## MariaDB migration
The Docker version uses SQLite instead of MariaDB for portability
and ease of deployment. The production version uses MariaDB and database
should be migrated.

1. **Install MariaDB** in a venv environment on your system as above
2. **Create a database**
   ```bash
      mysql -u root -p
      CREATE DATABASE news_app CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
      CREATE USER 'news_user'@'localhost' IDENTIFIED BY 'your_password';
      GRANT ALL PRIVILEGES ON news_app.* TO 'news_user'@'localhost';
      exit
   ```
   Update database in settings.py
   ```python
      DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'news_app',
            'USER': 'news_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
         }
      }
   ```

4. **Install MySQL client:**
```bash
   pip install mysqlclient
```

5. **Run migrations:**
```bash
   python manage.py migrate
```

6. **Create superuser:**
```bash
   python manage.py createsuperuser
```

**Note:** Data from SQLite will not automatically transfer.
You'll start with a fresh database.

## Usage

### First Steps once app is running

1. **Register an account** - Choose your role (Journalist, Editor,
Publisher, or Reader)
2. **Wait for admin approval** - The admin must approve your account
before you can log in
3. **Log in** and start using the platform based on your role

### For Journalists

1. Create an article from your dashboard
2. Select articles to include in newsletters (optional)
3. Submit to an editor for review
4. After approval, choose to publish independently or via a publisher

### For Editors

1. View pending review requests
2. Review, edit, or approve content
3. Provide feedback to journalists

### For Publishers

1. View articles submitted to your publication
2. Publish approved articles
3. Create newsletters featuring published content

### For Readers

1. Browse available journalists and publishers
2. Subscribe to your favorites
3. Receive email notifications when new content is published


## Key Models

- **CustomUser**: Extended user model with role-based access
- **Journalist**: Journalist profile with bio and interests
- **Editor**: Editor profile with field of interest
- **Publisher**: Publication house profile
- **Article**: News articles with workflow states
- **Newsletter**: Collections of articles

## Technologies Used

- **Backend**: Django 5.2.8
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS, Bootstrap
- **Forms**: Django Crispy Forms
- **Email**: Django email backend with Gmail SMTP
- **API Endpoints**: For readers to subscribe and retrieve publications

## Known Issues

- Email notifications require proper Gmail app password configuration
- Image uploads require media file configuration
- Some features require specific user permissions

## Future Improvements

- Social media integration
- Advanced search functionality
- Article analytics
- Mobile responsiveness improvements
- Real-time notifications

## Author

Created as part of a Django web development course project.
Elizabeth Füzy

=======
