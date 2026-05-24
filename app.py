from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = "secretkey"

# In-memory user storage
users = {
    "admin": "admin123"
}

# Login Page HTML
login_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>

    <style>

        body{
            font-family: Arial;
            background:#f2f2f2;
        }

        .container{
            width:300px;
            margin:100px auto;
            background:white;
            padding:20px;
            border-radius:10px;
            box-shadow:0px 0px 10px gray;
        }

        input{
            width:100%;
            padding:10px;
            margin-top:10px;
        }

        button{
            width:100%;
            padding:10px;
            margin-top:15px;
            background:#0095f6;
            color:white;
            border:none;
            cursor:pointer;
        }

        a{
            text-decoration:none;
        }

    </style>

</head>

<body>

<div class="container">

    <h2>Instagram Login</h2>

    <form method="POST">

        <input type="text"
               name="username"
               placeholder="Username"
               required>

        <input type="password"
               name="password"
               placeholder="Password"
               required>

        <button type="submit">
            Login
        </button>

    </form>

    <br>

    <a href="/register">
        Create Account
    </a>

</div>

</body>
</html>
"""

# Register Page HTML
register_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>

    <style>

        body{
            font-family: Arial;
            background:#f2f2f2;
        }

        .container{
            width:300px;
            margin:100px auto;
            background:white;
            padding:20px;
            border-radius:10px;
            box-shadow:0px 0px 10px gray;
        }

        input{
            width:100%;
            padding:10px;
            margin-top:10px;
        }

        button{
            width:100%;
            padding:10px;
            margin-top:15px;
            background:green;
            color:white;
            border:none;
            cursor:pointer;
        }

    </style>

</head>

<body>

<div class="container">

    <h2>Create Account</h2>

    <form method="POST">

        <input type="text"
               name="username"
               placeholder="Username"
               required>

        <input type="password"
               name="password"
               placeholder="Password"
               required>

        <button type="submit">
            Register
        </button>

    </form>

    <br>

    <a href="/login">
        Login
    </a>

</div>

</body>
</html>
"""

# Dashboard HTML
dashboard_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>

    <style>

        body{
            font-family: Arial;
            background:#fafafa;
            text-align:center;
            margin-top:100px;
        }

        a{
            text-decoration:none;
            background:red;
            color:white;
            padding:10px 20px;
        }

    </style>

</head>

<body>

<h1>Welcome USERNAME</h1>

<br><br>

<a href="/logout">
    Logout
</a>

</body>
</html>
"""

# Home
@app.route('/')
def home():

    if 'username' in session:
        return redirect('/dashboard')

    return redirect('/login')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:

            session['username'] = username

            return redirect('/dashboard')

        else:
            return "<h2>Invalid Username or Password</h2>"

    return login_page

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        users[username] = password

        return redirect('/login')

    return register_page

# Dashboard
@app.route('/dashboard')
def dashboard():

    if 'username' not in session:
        return redirect('/login')

    return dashboard_page.replace(
        "USERNAME",
        session['username']
    )

# Logout
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')

# Main
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000```python
from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = "secretkey"

# Fake Data
posts = [
    {
        "user": "devops_master",
        "caption": "Docker + Jenkins Deployment 🚀",
        "likes": 120
    },
    {
        "user": "python_dev",
        "caption": "Flask Application Running Successfully ❤️",
        "likes": 98
    },
    {
        "user": "cloud_engineer",
        "caption": "AWS + Docker Swarm + CI/CD 🔥",
        "likes": 210
    }
]

# Home Website
@app.route('/')
def home():

    posts_html = ""

    for post in posts:

        posts_html += f"""

        <div style='
            background:white;
            margin-top:20px;
            border-radius:15px;
            padding:20px;
            box-shadow:0px 0px 10px rgba(0,0,0,0.1);
        '>

            <div style='display:flex;align-items:center;'>

                <img
                src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png'
                width='50'
                height='50'
                style='border-radius:50%;margin-right:10px;'>

                <h3>@{post['user']}</h3>

            </div>

            <img
            src='https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1200&auto=format&fit=crop'
            width='100%'
            style='
                margin-top:15px;
                border-radius:10px;
                height:300px;
                object-fit:cover;
            '>

            <h4 style='margin-top:15px;'>

                ❤️ {post['likes']} Likes

            </h4>

            <p>

                <b>@{post['user']}</b>
                {post['caption']}

            </p>

        </div>

        """

    return f"""

    <!DOCTYPE html>

    <html>

    <head>

        <title>InstaClone</title>

    </head>

    <body style='
        margin:0;
        font-family:Arial;
        background:#f2f2f2;
    '>

        <!-- Navbar -->

        <div style='
            background:white;
            padding:15px 40px;
            display:flex;
            justify-content:space-between;
            align-items:center;
            box-shadow:0px 0px 10px rgba(0,0,0,0.1);
            position:sticky;
            top:0;
        '>

            <h2 style='color:#E1306C;'>

                InstaClone 🚀

            </h2>

            <div>

                <a href='/'
                   style='
                   margin-right:20px;
                   text-decoration:none;
                   color:black;
                   font-weight:bold;
                   '>

                   Home

                </a>

                <a href='/about'
                   style='
                   margin-right:20px;
                   text-decoration:none;
                   color:black;
                   font-weight:bold;
                   '>

                   About

                </a>

                <a href='/contact'
                   style='
                   text-decoration:none;
                   color:black;
                   font-weight:bold;
                   '>

                   Contact

                </a>

            </div>

        </div>

        <!-- Feed -->

        <div style='
            width:600px;
            margin:auto;
            margin-top:30px;
            margin-bottom:50px;
        '>

            {posts_html}

        </div>

    </body>

    </html>

    """

# About Page
@app.route('/about')
def about():

    return """

    <html>

    <body style='
        font-family:Arial;
        background:#f2f2f2;
        text-align:center;
        padding-top:100px;
    '>

        <h1>About InstaClone 🚀</h1>

        <p>

            This project is built using Python Flask
            for DevOps Deployment Practice.

        </p>

        <a href='/'>
            Back Home
        </a>

    </body>

    </html>

    """

# Contact Page
@app.route('/contact')
def contact():

    return """

    <html>

    <body style='
        font-family:Arial;
        background:#f2f2f2;
        text-align:center;
        padding-top:100px;
    '>

        <h1>Contact Page 📞</h1>

        <p>Email: devops@instaclone.com</p>

        <a href='/'>
            Back Home
        </a>

    </body>

    </html>

    """

# Run App
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
```
)
