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
