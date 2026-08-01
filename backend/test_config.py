from app.config import settings

print("=" * 50)
print("Application Configuration")
print("=" * 50)

print(f"App Name      : {settings.APP_NAME}")
print(f"Version       : {settings.APP_VERSION}")
print(f"Environment   : {settings.ENVIRONMENT}")
print(f"Host          : {settings.HOST}")
print(f"Port          : {settings.PORT}")
print(f"Database URL  : {settings.DATABASE_URL}")
print(f"Redis URL     : {settings.REDIS_URL}")
print(f"AI Service    : {settings.AI_SERVICE_URL}")
