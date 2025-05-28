# GraphQL Flask Server

A simple Flask-based GraphQL server with SQLAlchemy integration, featuring user and post management with a clean modular architecture.

## 🚀 Features

- **GraphQL API** - Modern API with GraphiQL interface for interactive querying
- **SQLAlchemy Integration** - SQLite database with Flask-SQLAlchemy ORM
- **Modular Architecture** - Clean separation of concerns with blueprints
- **Dummy Data** - Pre-populated with sample users and posts
- **CORS Support** - Cross-origin resource sharing enabled
- **Interactive Documentation** - Built-in GraphiQL interface

## 📋 Prerequisites

- Python 3.7+
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mahi028/GraphQLServer.git
   cd GraphQLServer
   ```

2. **Start Virtual environment and Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   python.exe -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Access the application**
   - Web Interface: http://localhost:5000
   - GraphiQL Interface: http://localhost:5000/graphql

## 📊 Database Schema

### User Model
- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `created_at` - Timestamp
- `posts` - One-to-many relationship with posts

### Post Model
- `id` - Primary key
- `title` - Post title
- `content` - Post content
- `created_at` - Timestamp
- `user_id` - Foreign key to user

## 🔍 GraphQL Queries

### Get All Users
```graphql
{
  allUsers {
    id
    username
    email
    createdAt
    posts {
      title
      content
    }
  }
}
```

### Get User by ID
```graphql
{
  user(id: 1) {
    username
    email
    posts {
      title
      content
      createdAt
    }
  }
}
```

### Get User by Username
```graphql
{
  user(username: "john_doe") {
    id
    email
    posts {
      title
      content
    }
  }
}
```

### Get All Posts
```graphql
{
  allPosts {
    id
    title
    content
    createdAt
    author {
      username
      email
    }
  }
}
```

### Get Posts by User ID
```graphql
{
  postsByUser(userId: 1) {
    title
    content
    createdAt
    author {
      username
    }
  }
}
```

## 📁 Project Structure

```
GraphQLApp/
├── application/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # SQLAlchemy models
│   ├── apiGql.py           # GraphQL schema and resolvers
│   └── dummy.py            # Dummy data and routes
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── OpenApiSpec.yaml       # API documentation
└── README.md              # Project documentation
```

## 🧪 Sample Data

The application comes pre-loaded with:
- **5 Users**: john_doe, jane_smith, mike_wilson, sarah_jones, alex_brown
- **13 Posts**: 2-3 posts per user covering various tech topics

## 🌐 API Endpoints

- `GET /` - Web interface with query examples
- `POST /graphql` - GraphQL endpoint
- `GET /graphql` - GraphiQL interactive interface

## 🔧 Configuration

The application uses SQLite by default. To change the database:

1. Update the `SQLALCHEMY_DATABASE_URI` in `application/__init__.py`
2. Install appropriate database drivers
3. Restart the application

## 📚 Dependencies

- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM integration
- **Flask-GraphQL** - GraphQL integration
- **Flask-CORS** - Cross-origin support
- **Graphene** - GraphQL library
- **Graphene-SQLAlchemy** - SQLAlchemy integration for Graphene

## 🚀 Deployment

For production deployment:

1. Set `debug=False` in `main.py`
2. Use a production WSGI server (gunicorn, uWSGI)
3. Configure environment variables for sensitive data
4. Use a production database (PostgreSQL, MySQL)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:
1. Check the GraphiQL interface at `/graphql` for query testing
2. Review the console logs for error messages
3. Ensure all dependencies are properly installed

## 🔗 Related Resources

- [GraphQL Documentation](https://graphql.org/learn/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Graphene-Python Documentation](https://docs.graphene-python.org/)
