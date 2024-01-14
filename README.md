# Django Product Catalog Project

This Django project, named "product_catalog," is designed to manage and showcase products through a web application. Below is a brief overview of the project structure and key components:

## Project Structure

- **Database:** The project utilizes both PostgreSQL and MongoDB databases to store different types of data.
- **Models:** Two models are defined - a PostgreSQL model for users and a MongoDB model for products. These models are used to create database tables for storing user and product information.
- **Managers:** Custom model managers (`PostgresModelManager` and `MongoDBModelManager`) are implemented to facilitate database operations for PostgreSQL and MongoDB, respectively.
- **Serializers:** Serializers are defined for User and Product models using Django Rest Framework to convert complex data types to native Python datatypes for rendering into JSON.

# Database Setup

## PostgreSQL Database

### Create a Database
```sql
-- Create a database (if not exists)
CREATE DATABASE mydatabase;

-- Connect to the database
\c mydatabase;

-- Create the users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## MongoDB Database
```mongodb
// Switch to your desired database
use mydatabase

// Create a collection for products
db.createCollection("products")

// Insert a sample product
db.products.insertOne({
   name: "Test Product",
   description: "This is a sample product.",
   price: 29.99,
   stock_quantity: 50,
   created_at: new ISODate(),
})

//sample Product Document

{
  "_id": ObjectId("5f00a8da14323a45f85661b5"),
  "name": "Test Product",
  "description": "This is a sample product.",
  "price": 29.99,
  "stock_quantity": 50,
  "created_at": ISODate("2024-01-14T12:00:00Z"),
}
```

## REST API Endpoints

The project implements REST API views for user and product operations, including listing, creating, and retrieving functionalities. Two main API endpoints are provided: `/api/users/` for managing users and `/api/products/` for managing products. The project also includes custom error handling for better user feedback.


## Dependencies

The project relies on Django (version 5.0.1), Djongo, and Django Rest Framework. Ensure these packages are installed in your environment.

## Run the Project

To run the project, execute Django's `manage.py` commands, such as `python manage.py runserver`.

## Database Configuration

The project is configured to use both PostgreSQL and MongoDB databases. Modify the database settings in `settings.py` based on your requirements.

## Testing

The project includes basic error handling in API views. Extensive testing is recommended before deploying it to a production environment.
