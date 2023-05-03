import pandas as pd
import hashlib
import uuid

# Import data
df = pd.read_csv('data.csv')
anonymized_df = df.copy()

# Function to generate a random UUID
def generate_uuid():
    return str(uuid.uuid4())
anonymized_df['Name'] = anonymized_df['Name'].apply(lambda x: generate_uuid())

# Function to hash a phone number using SHA256
def hash_phone_number(phone_number):
    return hashlib.sha256(phone_number.encode('utf-8')).hexdigest()
anonymized_df['PhoneNumber'] = anonymized_df['PhoneNumber'].apply(hash_phone_number)

# Function to hash an address
def hash_address(address):
    return hashlib.sha256(address.encode()).hexdigest()
anonymized_df['Address'] = anonymized_df['Address'].apply(lambda x: hash_address(x))



# save anonymized data
anonymized_df.to_csv('anonymized_data.csv', index=False)
