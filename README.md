# BlogBit: A Blog Application

This project aims to create a Django-based blog application that fulfills the following requirements:
1. Design the blog data schema
2. Create a Django application that allows users to:
    - Login
    - Signup
    - Write down any blog from the Django admin website
    - Build list and detail views of blogs
    - Add pagination (To display 5 blogs on a page)
    - Implement tagging functionality and searching based on tags and blogs

## Requirements
1. Environment variables:
   - DJANGO_KEY
   - DB_NAME
   - DB_USER
   - DB_PASSWORD
   - DB_HOST

## Getting Started
To get started with the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Alok5102R/BlogApp.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database schema according to the blog data schema design.
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser to access the Django admin:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the Django admin interface at `http://127.0.0.1:8000/admin/` and log in using the superuser credentials created in step 5.

## Project Structure
- **blog/**: Contains the Django application code for the blog functionality.
- **templates/**: Contains HTML templates for rendering the blog views.
- **static/**: Contains static files such as CSS, JavaScript, and images.
- **requirements.txt**: Lists the Python dependencies required for the project.

## Application Preview

<img align="center" src="https://github.com/Alok5102R/BlogApp/blob/master/static/img/blogregister.jpg" alt="blogregister">
<img align="center" src="https://github.com/Alok5102R/BlogApp/blob/master/static/img/bloglogin.jpg" alt="bloglogin">
<img align="center" src="https://github.com/Alok5102R/BlogApp/blob/master/static/img/bloghome1.jpg" alt="bloghome1">
<img align="center" src="https://github.com/Alok5102R/BlogApp/blob/master/static/img/bloghome2.jpg" alt="bloghome2">
<img align="center" src="https://github.com/Alok5102R/BlogApp/blob/master/static/img/blogsearch.jpg" alt="blogsearch">

## Features
- User authentication: Allows users to sign up and log in.
- Blog creation: Users can write and publish their blogs.
- Blog listing and detail views: Displays a list of blogs with pagination support and allows users to view individual blog posts.
- Tagging functionality: Allows users to tag their blog posts and search for blogs based on tags.

## Contributions
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
