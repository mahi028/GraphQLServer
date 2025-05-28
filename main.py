# python.exe -m pip install --upgrade pip
from application import create_app
from application.dummy import create_dummy_data
from application.models import db, User

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Check if data already exists
        if User.query.count() == 0:
            create_dummy_data()
            print("Dummy data created successfully!")
    
    app.run(debug=True)
