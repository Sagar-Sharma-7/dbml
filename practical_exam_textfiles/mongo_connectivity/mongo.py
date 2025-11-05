from pymongo import MongoClient

# Connect to MongoDB 
client = MongoClient("mongodb://localhost:27017/") 
db = client["connectivity"] 
collection = db["students"]

# Insert a document 
def insert_document(): 
    name = input("Enter name: ") 
    age = int(input("Enter age: ")) 
    city = input("Enter city: ")
    
    doc = {"name": name, "age": age, "city": city} 
    result = collection.insert_one(doc) 
    print(f"Inserted with ID: {result.inserted_id}")

# Find documents 
def find_documents(): 
    print("\nAll documents in collection:") 
    for doc in collection.find(): 
        print(doc)

# Update a document 
def update_document(): 
    name = input("Enter the name to update: ") 
    new_age = int(input("Enter new age: ")) 
    
    result = collection.update_one( 
        {"name": name}, 
        {"$set": {"age": new_age}}
    ) 
    
    if result.modified_count > 0: 
        print("Document updated.")
    else: 
        print("No matching document found.")

# Delete a document 
def delete_document(): 
    name = input("Enter the name to delete: ") 
    
    result = collection.delete_one({"name": name}) 
    
    if result.deleted_count > 0: 
        print("Document deleted.")
    else: 
        print("No matching document found.")

# Main menu loop 
def main(): 
    while True: 
        print("\n--- MongoDB Menu ---") 
        print("1. Insert Document") 
        print("2. Find Documents") 
        print("3. Update Document")
        print("4. Delete Document") 
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1': 
            insert_document()
        elif choice == '2': 
            find_documents()
        elif choice == '3': 
            update_document()
        elif choice == '4': 
            delete_document()
        elif choice == '5': 
            print("Exiting program.") 
            break
        else: 
            print("Invalid choice. Try again.")

if __name__ == "__main__": 
    main()