from app import app, db
import models

db.create_all()

if __name__ == '__main__':
    app.run()
