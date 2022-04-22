from app import app, db
import models
import auth
import tests
import routes
db.create_all()

if __name__ == '__main__':
    app.run()
