from src.config.settings import settings


print("APP:", settings.APP_NAME)

print("ENV:", settings.ENVIRONMENT)

print("JSON STORE:", settings.JSON_STORE_DIR)

print("DB:", settings.DATABASE_PATH)

print("KEY EXISTS:", bool(settings.GROQ_API_KEY))