<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--     <title>AR Food Menu - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f8f9fa;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: monospace;
        }
        img {
            max-width: 100%;
            height: auto;
            margin: 10px 0;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style> -->
</head>
<body>
    <h1>AR Food Menu</h1>
    <p><strong>Description:</strong> AR Food Menu is an innovative platform that enhances restaurant experiences using Augmented Reality (AR). Users can explore 3D visualizations of menu items before ordering, making the dining experience more interactive and immersive.</p>
    <p>This project utilizes cutting-edge technologies, including AWS S3 for storing AR models and images, JWT for secure authentication, Razorpay for payments, and a robust backend built with Django and Django REST Framework. The frontend is designed with React.js and Next.js, ensuring a seamless and dynamic user experience.</p>
    
  <h2>Features</h2>
    <ul>
        <li>Augmented Reality (AR) food preview with 3D models</li>
        <li>Secure authentication using JWT tokens</li>
        <li>Cloud storage with AWS S3 for images and 3D assets</li>
        <li>Interactive and responsive UI using Next.js and React.js</li>
        <li>REST API for seamless communication between frontend and backend</li>
        <li>Online payments using Razorpay</li>
        <li>Optimized for performance and scalability</li>
    </ul>

  <h2>Technologies Used</h2>
  <h3>Frontend</h3>
    <ul>
        <li>HTML, CSS, JavaScript</li>
        <li>React.js, Next.js</li>
    </ul>
    
  <h3>Backend</h3>
    <ul>
        <li>Python, Django, Django REST Framework</li>
        <li>JWT Authentication</li>
    </ul>
    
  <h3>Cloud & Storage</h3>
    <ul>
        <li>AWS S3 (for image and model storage)</li>
    </ul>

  <h2>Screenshots</h2>
    <h3>User Home Page</h3>
    <img src="DineVision/screenshots/WhatsApp Image 2024-11-25 at 10.59.54 PM (1).jpeg" alt="User Home Page">
    <h3>Hotel Owner Home Page</h3>
    <img src="DineVision/screenshots/WhatsApp Image 2024-11-25 at 10.59.55 PM.jpeg" alt="Hotel Owner Home Page">
    <h3>Login Page</h3>
    <img src="DineVision/screenshots/WhatsApp Image 2024-11-25 at 10.59.52 PM.jpeg" alt="Login Page">
    <h3>Payment Page</h3>
    <img src="DineVision/screenshots/WhatsApp Image 2024-11-25 at 10.59.58 PM.jpeg" alt="Payment Page">
    <h3>Add an Food Item</h3>
    <img src="DineVision/screenshots/WhatsApp Image 2024-11-25 at 10.59.54 PM.jpeg" alt="Add Food">    
    <h3>Augmented Reality Food Preview (Cartoon-Styled 3D Model)</h3>
    <img src="DineVision/screenshots/WhatsApp Image 2024-11-25 at 10.59.56 PM.jpeg" alt="Augmented Reality Food Preview">
    <h3>Owner Profile Page</h3>
    <img src="DineVision/screenshots/WhatsApp Image 2024-11-25 at 10.59.53 PM.jpeg" alt="Owner Profile Page">

  <h2>Installation</h2>
    <h3>Backend Setup</h3>
    <pre><code>git clone https://github.com/VISHNURAJESHP/ar-food.git
cd ar-food-menu/backend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver</code></pre>

  <h3>Frontend Setup</h3>
    <pre><code>cd ar-food-menu/frontend
npm install
npm run dev</code></pre>

  <h2>Usage</h2>
    <p>Visit <code>http://localhost:3000</code> for the frontend and <code>http://localhost:8000</code> for the backend API.</p>
    
  <h2>License</h2>
    <p>MIT License</p>
</body>
</html>
