# from pymongo import MongoClient
# from werkzeug.security import generate_password_hash
# import os

# def store_user_data(first_name, last_name, phone, email, password):
#     try:
#         # Connect to MongoDB Atlas
#         mongo_uri = os.getenv("MONGO_URI") 
#         client = MongoClient(mongo_uri)
        
#         # Select the database and collection
#         db = client["TENCOWRY"]
#         collection = db["TenCowry_eCommerce"]

#         # Hash the password
#         hashed_password = generate_password_hash(f"a{password}z")

#         # Create a document to insert
#         user_data = {
#             "first_name": first_name,
#             "last_name": last_name,
#             "phone": phone,
#             "email": email,
#             "password": hashed_password
#         }

#         # Insert the document into the collection
#         result = collection.insert_one(user_data)

#         # Print the inserted document's ID
#         print(f"User data inserted with ID: {result.inserted_id}")

#     except Exception as e:
#         print(f"Error: {e}")

#     finally:
#         # Close the MongoDB connection
#         if client:
#             client.close()

# # Example usage
# store_user_data("John", "Doe", "07038157217", "onyebuchisamson36@gmail.com", "")


# from flask import Flask, request
# from flask_bcrypt import generate_password_hash, check_password_hash
# from pymongo import MongoClient
# import os

# app = Flask(__name__)

# # Connect to MongoDB Atlas (replace the placeholders with your actual connection string and database information)
# mongo_uri = os.getenv("MONGO_URI") 
# client = MongoClient(mongo_uri)
# db = client['TENCOWRY']  
# registered_emails_collection = db['TenCowry_eCommerce']

# # Route for changing the password
# @app.route('/change_password', methods=['POST'])
# def change_password():
#     # Extract parameters from raw JSON in the request body
#     data = request.get_json()

#     email = data.get('email')
#     old_password_attempt = data.get('old_password')
#     new_password = data.get('new_password')

#     # Find the user based on the provided email
#     user = registered_emails_collection.find_one({"email": email})

#     print("User document:", user)

#     if user and 'password_hash' in user:
#         if check_password_hash(user["password_hash"], old_password_attempt):
#             # If the user exists and the old password is correct, update the password hash
#             new_password_hash = generate_password_hash(f"a{new_password}z")
#             registered_emails_collection.update_one({"email": email}, {"$set": {"password_hash": new_password_hash}})
#             return "Password changed successfully."
    
#     print("Login attempt failed.")
#     return "Invalid email or password.", 401



from werkzeug.security import generate_password_hash,check_password_hash
#print(generate_password_hash("P1ain-text-user-passw@rd", "sha256"))

print(check_password_hash("sha256$lTsEjTVv$c794661e2c734903267fbc39205e53eca607f9ca2f85812c95020f", "P1ain-text-user-passw@rd"))
