# config.py
class Config:
    SECRET_KEY = 'your-secret-key'#ยังไม่ได้ใช้
    JWT_SECRET_KEY = 'your-jwt-secret'#ยังไม่ได้ใช้
    MONGODB_SETTINGS = {
        'db': 'mario_notes',
        'host': 'localhost',
        'port': 27017
    }