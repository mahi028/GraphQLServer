from flask import Blueprint
from .models import User, Post, db

index_blueprint = Blueprint('index', __name__)

def create_dummy_data():
    """Create dummy users and posts"""
    users_data = [
        {'username': 'john_doe', 'email': 'john@example.com'},
        {'username': 'jane_smith', 'email': 'jane@example.com'},
        {'username': 'mike_wilson', 'email': 'mike@example.com'},
        {'username': 'sarah_jones', 'email': 'sarah@example.com'},
        {'username': 'alex_brown', 'email': 'alex@example.com'}
    ]
    
    users = []
    for user_data in users_data:
        user = User(**user_data)
        db.session.add(user)
        users.append(user)
    
    db.session.flush()  # Flush to get user IDs
    
    posts_data = [
        # Posts for john_doe
        {'title': 'Getting Started with Python', 'content': 'Python is a great programming language for beginners...', 'user_id': users[0].id},
        {'title': 'Web Development Tips', 'content': 'Here are some tips for web development...', 'user_id': users[0].id},
        {'title': 'Data Science Journey', 'content': 'My journey into data science has been amazing...', 'user_id': users[0].id},
        
        # Posts for jane_smith
        {'title': 'Machine Learning Basics', 'content': 'Understanding the fundamentals of ML...', 'user_id': users[1].id},
        {'title': 'AI in Healthcare', 'content': 'How AI is revolutionizing healthcare...', 'user_id': users[1].id},
        
        # Posts for mike_wilson
        {'title': 'Mobile App Development', 'content': 'Building mobile apps with React Native...', 'user_id': users[2].id},
        {'title': 'DevOps Best Practices', 'content': 'Essential DevOps practices for modern development...', 'user_id': users[2].id},
        {'title': 'Cloud Computing Guide', 'content': 'A comprehensive guide to cloud computing...', 'user_id': users[2].id},
        
        # Posts for sarah_jones
        {'title': 'Frontend Frameworks', 'content': 'Comparing React, Vue, and Angular...', 'user_id': users[3].id},
        {'title': 'CSS Grid Layout', 'content': 'Mastering CSS Grid for modern layouts...', 'user_id': users[3].id},
        
        # Posts for alex_brown
        {'title': 'Database Optimization', 'content': 'Tips for optimizing database performance...', 'user_id': users[4].id},
        {'title': 'API Design Principles', 'content': 'Best practices for designing RESTful APIs...', 'user_id': users[4].id},
        {'title': 'Microservices Architecture', 'content': 'Understanding microservices patterns...', 'user_id': users[4].id}
    ]
    
    for post_data in posts_data:
        post = Post(**post_data)
        db.session.add(post)
    
    db.session.commit()

@index_blueprint.route('/')
def index():
    return '''
    <h1>GraphQL Flask App</h1>
    <a href="/graphql">GraphiQL Interface</a>
    <h3>Example Queries:</h3>
    <pre>
    # Get all users
    {
      allUsers {
        id
        username
        email
        createdAt
      }
    }
    
    # Get user with posts
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
    
    # Get posts by user
    {
      postsByUser(userId: 1) {
        title
        content
        author {
          username
        }
      }
    }
    </pre>

    '''