from app import app, db
import models
import auth
import tests
db.create_all()

if __name__ == '__main__':
    app.run()
