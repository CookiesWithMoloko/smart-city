from app import app, db
import models
import hashlib
db.create_all()

if __name__ == '__main__':
    app.run()
