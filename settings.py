# Import libraries:
import bcrypt

# MongoDB address:
MONGODB_HOST = 'mongodb://localhost:27017/'
MONGODB_ATLAS = ''


# Common password:
TMP_PASSWORD = bcrypt.hashpw("123456".encode(), bcrypt.gensalt()).decode().encode()