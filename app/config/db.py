from motor.motor_asyncio import AsyncIOMotorClient
import os

# MongoDB client initialization
client: AsyncIOMotorClient = None

def init_db():
    global client
    client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    # Set the default database name
    return client.get_database('your_database_name')  # Replace 'your_database_name' with your actual database name

db = init_db()
