from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, MilvusException, db, utility

# # Connect to Milvus
connections.connect(host="localhost", port="19530")
print("Connected to Milvus!")

# Check if the database exists
db_name = "rag_application"
try:
    existing_databases = db.list_database()
    if db_name in existing_databases:
        print(f"Database '{db_name}' already exists.")

        # Use the database context
        db.using_database(db_name)

        # Drop all collections in the database
        collections = utility.list_collections()
        for collection_name in collections:
            collection = Collection(name=collection_name)
            collection.drop()
            print(f"Collection '{collection_name}' has been dropped.")

        db.drop_database(db_name)
        print(f"Database '{db_name}' has been deleted.")
    else:
        print(f"Database '{db_name}' does not exist.")
    database = db.create_database(db_name)
    print(f"Database '{db_name}' created successfully.")
except MilvusException as e:
    print(f"An error occurred: {e}")