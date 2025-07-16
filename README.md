# 📝 Flask Task Manager

A minimal web-based task manager built with **Flask**, allowing you to create, update, and delete tasks. Tasks are timestamped and stored in a local SQLite database.

## 🚀 Live App

👉 [Deployed on Render](https://flaskintro-3se6.onrender.com/)

-----------------------

## 📁 Project Structure

flaskintro/
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Procfile # For Render deployment
├── .gitignore # Ignore unnecessary files/folders
├── instance/
│ └── test.db # SQLite database (auto-generated)
├── static/
│ └── css/
│ └── main.css # Styling
├── templates/
│ ├── base.html
│ ├── index.html
│ └── update.html # For editing existing tasks


----------------------

## 🛠️ Features

- ✅ Create, update, and delete tasks
- 🕓 Timestamp every task on creation
- 🗃️ SQLite as the backend database
- 🎨 Styled with basic CSS
- 🌐 Deployed on Render

----------------------

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flaskintro.git
cd flaskintro
2. Set Up a Virtual Environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Application Locally
python app.py
Open your browser at: http://localhost:5000

📦 Deployment (Render)
Push your code to GitHub
Create a new Web Service on Render.com
Connect your repo & choose:
Build Command: pip install -r requirements.txt
Start Command: python app.py
Add instance/ and env/ to .gitignore

🧹 .gitignore (included)
gitignore
__pycache__/
env/
instance/
*.py[cod]
.vscode/

🧑‍💻 Author
Kartik – Built using Flask & deployed using Render