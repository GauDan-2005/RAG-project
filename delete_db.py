from pymilvus import utility, connections

connections.connect(host="localhost", port="19530")
print("Connected to Milvus!")
utility.drop_collection("website_embeddings")

print("DB droped!")

