from app import app, db

import routes
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
