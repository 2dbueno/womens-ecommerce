# e-commerce
# 👗 Women's E-commerce Platform

## 📖 Project Description

This project is a comprehensive e-commerce platform designed for women, developed using modern and robust technologies. It utilizes **Vue.js** for the front-end, **Python** and **Django** for the back-end, and **PostgreSQL** as the database management system, offering an intuitive and efficient shopping experience.

### 🌟 Key Features

- **User  Registration and Authentication**: 
  - Allows users to register, log in, and manage their accounts securely.
  
- **Product Catalog**: 
  - Displays products with filters by category, price, and popularity, enabling users to easily find what they want.
  
- **Shopping Cart**: 
  - Functionality to add, remove, and edit products in the cart, with automatic total calculation.
  
- **Payment Processing**: 
  - Integration with payment gateways to facilitate secure transactions.
  
- **Order Management**: 
  - Users can view their order history and the status of their purchases.
  
- **Product Administration**: 
  - Admin panel for managing products, categories, and orders, allowing store administrators to keep the catalog updated.
  
- **Responsiveness**: 
  - Responsive design that ensures an optimized shopping experience on both mobile and desktop devices.

### 🛠️ Technologies Used

- **Front-end**: 
  - **Vue.js**: A progressive framework for building user interfaces, providing an interactive and dynamic experience.
  
- **Back-end**: 
  - **Python**: A versatile and powerful programming language used for server-side development.
  - **Django**: A high-level web framework that promotes rapid and clean development with a robust and secure architecture.

- **Database**: 
  - **PostgreSQL**: A relational database management system known for its robustness and support for complex queries.

### 🚀 How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/womens-ecommerce.git
   cd womens-ecommerce
    ```

2. **Set up the environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate  # For Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Database Configuration:**
    # Create a PostgreSQL database and configure the credentials in the Django settings file.

5. **Migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Start the server:**
    ```bash
    python manage.py runserver
    ```

7. **Start the Front-end:**
    ```bash
    cd frontend  # Navigate to the front-end folder
    npm install
    npm run serve
    ```

### 🤝 Contributions
Contributions are welcome! Feel free to open issues or pull requests for improvements and new features.

### 📄 License
This project is licensed under the MIT License. See the [MIT](LICENSE) file for more details.
