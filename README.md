# DPDZeroAssignment

This is a take home assessment for creating backend system for DPDZero. This readme will guide you to setting up this project easily.

## DB Setup
- We are using MySQL DB. Download MySQL and create a Schema with the name `users` and a tables with the name `users` and `key_value_data`.
-`users` table has columns as below:
  - 1. `id` - Integer (PK, NN, AI)
    2. `username` - String (VARCHAR) (NN, UQ)
    3. `email` - String (NN, UQ)
    4. `password` - String (NN)
    5. `age'` - Integer
    6. `gender` - String
  
  
  > *NNN = Non Nullable, UQ: Uniqe, PK = Pimary Key, AI= Auto Increment

- `key_value_data` has following columns:
  - 1. `id` - INT (PK, NN, AI)
    2. `key` - String (UQ, NN)
    3. `value` - String (NN)


## Code Setup
- 1. replace `nopass19` in `'mysql+mysqlconnector://root:nopass19@localhost:3306/users'` with your password and change the port if needed as well.
- 2. Add your own 'SECRET_KEY' in `SECRET_KEY = "your_secret_key"` . It can be anything.
 
## Running the Code:

1. Python 3.7+ required and PIP required.
2. Install all the requirements with the following command `pip install -r requirements.txt`
3. run the following in terminal : `python backend.py`. Once the backend is up, you can try and run `python tests.py`

 
