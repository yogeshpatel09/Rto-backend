from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection URL and Database name
MONGODB_URL = "mongodb+srv://yogesh:Yogesh12@cluster0.kv5a1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Update with your MongoDB URL
DB_NAME = "your_database_name"  # Update with your database name

# Create a client and get the database
client = AsyncIOMotorClient(MONGODB_URL)
db = client[DB_NAME]  # Database connection

# MongoDB collections
product_collection = db.get_collection("products")
