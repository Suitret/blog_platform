# Simple Blog Platform

This is a Python-based blog platform built with Flask, allowing users to create, edit, view, and delete blog posts. It includes user authentication (login/register) to manage posts securely. Data is stored persistently in a SQLite database using SQLAlchemy, and the front-end is rendered with Jinja2 templates styled with CSS.

## Features
- Create, edit, and delete blog posts with title, content, and category.
- View all posts on the homepage or individual posts by ID.
- User authentication (register, login, logout) to restrict post management to logged-in users.
- Persistent storage using SQLite.
- Input validation for posts and user credentials.
- Responsive design with basic CSS styling.

## File Structure
```
blog_platform/
├── main.py              # Entry point to run the Flask app
├── models.py           # Defines User and Post models with SQLAlchemy
├── routes.py           # API routes for posts and authentication
├── database.py         # SQLite database connection and initialization
├── auth.py             # User authentication logic
├── utils.py            # Helper functions for validation and formatting
├── templates/           # Jinja2 HTML templates
│   ├── index.html      # Homepage listing all posts
│   ├── post.html       # View/edit individual post
│   ├── login.html      # Login page
│   └── register.html   # Registration page
├── static/             # Static assets
│   └── style.css       # CSS for styling
├── config.py           # Configuration settings
└── README.md           # Project documentation
```

## Setup Instructions
1. **Prerequisites**:
   - Python 3.6 or higher.
   - Install required dependencies:
     ```bash
     pip install flask flask-sqlalchemy werkzeug
     ```

2. **Installation**:
   - Clone or download the project files to a `blog_platform` directory.
   - Install dependencies as shown above.

3. **Running the Application**:
   - Navigate to the `blog_platform` directory.
   - Run the following command:
     ```bash
     python main.py
     ```
   - Open a browser and visit `http://localhost:5000` to access the platform.

4. **Data Storage**:
   - Posts and user data are stored in `blog.db` (SQLite database) in the project directory.
   - The database is created automatically on first run.

## Usage
- **Register/Login**: Create an account or log in to manage posts.
- **Create Post**: Use the form on the homepage (when logged in) to add a new post with title, content, and category.
- **Edit/Delete Post**: View a post and, if logged in as the author, edit or delete it.
- **View Posts**: Browse all posts on the homepage or view individual posts by clicking their titles.
- **Logout**: Log out to end the session.

## Example Data
Posts are stored in the `posts` table in `blog.db` with columns: `id`, `title`, `content`, `category`, `author_id`, `created_at`. Users are stored in the `users` table with columns: `id`, `username`, `password_hash`.

## Development Notes
- Built with Flask for routing and Jinja2 for templating.
- Uses SQLAlchemy for ORM-based database operations.
- Passwords are hashed using Werkzeug's security module.
- Basic CSS provides a clean, responsive interface.
- Input validation ensures required fields and secure authentication.

## Future Improvements
- Add post filtering by category or date.
- Implement comment functionality for posts.
- Add user profiles and avatars.
- Enhance styling with a CSS framework like Bootstrap.
- Add pagination for the post list.

## License
This project is licensed under the MIT License.