# DPDZeroAssignment

This is a take home assessment for creating backend system for DPDZero. This readme will guide you yo setting up this project easily.

## DB Setup
> We are using MySQL DB. Download MySQL and create a Schema with the name `users` and a tables with the name `users` and `key_value_data`.
>`users` table has columns as below:
>>`id` - Integer (PK, NN, AI)
>>`username` - String (VARCHAR) (NN, UQ)
>>`email` - String (NN, UQ)
>>`password` - String (NN)
>>`age'` - Integer 
>>`gender` - String
>>*NNN = Non Nullable, UQ: Uniqe, PK = Pimary Key, AI= Auto Increment
>`key_value_data` has following columns:
>>`id` - INT (PK, NN, AI)
>>`key` - String (UQ, NN)
>>`value` - String (NN)


## Setup
> 1. Python 3.7+ required and PIP required.
> 2. Install all the requirements with the following command `pip install -r requirements.txt`
> 3. Run backend.py first and then tests.py with command `python backend.py` or `python tests.py`
