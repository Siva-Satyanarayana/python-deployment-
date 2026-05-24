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

    app.run(host='0.0.0.0', port=5000)
