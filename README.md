# Ex.07 Software Product Company Website
## Date:

## AIM:
To develop a static company website to display the softwares and services provided by the company.

## DESIGN STEPS:

### Step 1:
Requirement collection.

### Step 2:
Creating the layout using HTML and CSS.

### Step 3:
Updating the sample content.

### Step 4:
Choose the appropriate style and color scheme.

### Step 5:
Validate the layout in various browsers.

### Step 6:
Validate the HTML code.

### Step 7:
Publish the website in the given URL.

## PROGRAM:
```home.html
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title> Code Crafters </title>
        <style type="text/css">
            * {
                margin: 0;
                padding: 0;
                font-family: Arial, Helvetica, sans-serif;
            }
            .banner {
                width: 100%;
                height: 100vh;
                background-image: linear-gradient(rgba(0,0,0,0.75),rgba(0,0,0,0.75)),url(background.jpg);
                background-size: cover;
                background-position: center;
            }
            .navbar {
                width: 85%;
                margin: auto;
                padding: 35px 0;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            body {
                background: -webkit-linear-gradient(bottom, #2dbd6e, #a6f77b);
                background-repeat: no-repeat;
            }
            .logo {
                color: #6fa1f8;
                font-size: 35px;
                font-weight: 700;
                letter-spacing: 1px;
            }
            span {
                color: white;
            }
            form {
                width: 300px;
                height: 40px;
                display: flex;
                background: rgba(255, 255, 255, 0.2);
                padding: 1px 1px;
                font-size: 15px;
                border-radius: 10px;
                backdrop-filter: blur(4px) saturate(180%);
            }
            form input {
                background: transparent;
                flex: 1;
                border: 0;
                outline: none;
                padding: 12px 20px;
                font-size: 15px;
                color: white;
            } 
            ::placeholder {
                color: white;
            }
            form button {
                border: 0;
                outline: none;
                padding: 5px 20px;
                color: white;
                border-radius: 10px;
                background: #6fa1f8;
                cursor: pointer;
            }
            .navbar li {
                list-style: none;
                display: inline-block;
                margin: 0 20px;
                position: relative;
            }
            .navbar li a {
                text-decoration: none;
                color: white;
                text-transform: uppercase;
            }
            .navbar li:hover {
                border: 1px;
                padding: 10px;
                color: white;
                background-color: #6fa1f8;
                transition: 0.5s; 
                cursor: pointer;
                border-radius: 30px;
            }
            .content {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%,-50%);
                text-align: center;
            }
            .text h2 {
                color: white;
                font-weight: 800;
                font-size: 50px;
                letter-spacing: 3px;
            }
            .text p {
                color: white;
                text-transform: capitalize;
                font-size: 15px;
                margin-bottom: 30px;
                word-spacing: 2px;
                letter-spacing: 1px;
            }
            .login {
                margin: 0px 10px;
                border: 2px solid #6fa1f8;
                padding: 13px 35px;
                letter-spacing: 1px;
                color: white;
                border-radius: 30px;
                background-color: #6fa1f8;
                text-decoration: none;
            }
            .login:hover {
                border: 2px solid #6fa1f8;
                color: #6fa1f8;
                background-color: white;
                transition: 0.5s;
                cursor: pointer;
            } 
            .signup {
                margin: 0px 10px;
                border: 2px solid #6fa1f8;
                padding: 13px 35px;
                letter-spacing: 1px;
                color: white;
                border-radius: 30px;
                background-color: #6fa1f8;
                text-decoration: none;
            }
            .signup:hover {
                border: 2px solid #6fa1f8;
                color: #6fa1f8;
                background-color: white;
                transition: 0.5s;
                cursor: pointer;
            }
            footer {
                background-color: #6fa1f8;
                margin-top: auto;
            }
        </style>
        {%load static%}
    </head>
<body>
    <div class="banner">
        <br>
        <div class="navbar">
            <h1 class="logo">C<span>ode</span>C<span>rafters</span></h1>
            <ul>
                <li><a href="{%url 'h'%}"> Home </a></li>
                <li><a href="http://127.0.0.1:8000/product/"> Products </a></li>
                <li><a href="http://127.0.0.1:8000/people/"> People </a></li>
                <li><a href="http://127.0.0.1:8000/contact/"> Contact </a></li>
            </ul>
            <form action="" method="get">
                <input type="text" placeholder="Enter to Search">
                <button type="submit"> Search </button>
            </form>
        </div>
        <div class="content">
            <div class="text">
                <h2> Software Development Company </h2>
                <br>
                <p> Welcome to CodeCrafters, your gateway to cutting-edge software solutions and innovative web development applications! </p>
                <br>
                <div>
                    <a href="#" class="login"> Log In </a>
                    <a href="#" class="signup"> Sign Up </a>
                </div>
            </div>
        </div>  
    </div>
    <footer>
        <center> Designed by : Naveen Kumar V (212223220068)  </center>
    </footer>
</body>
</html>

product.html
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title> Product Page </title>
        {%load static%}
        <style type="text/css">
            * {
                margin: 0;
                padding: 0;
                font-family: Arial, Helvetica, sans-serif;
            }
            .banner {
                width: 100%;
                height: 100vh;
                background-image: linear-gradient(rgba(0,0,0,0.75),rgba(0,0,0,0.75)),url(background.jpg);
                background-size: cover;
                background-position: center;
            }
            .navbar {
                width: 85%;
                margin: auto;
                padding: 35px 0;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            body {
                background: -webkit-linear-gradient(bottom, #2dbd6e, #a6f77b);
                background-repeat: no-repeat;
            }
            .bg-product {
                border: 1px;
                padding: 10px;
                color: white;
                background-color: #6fa1f8;
                border-radius: 30px;
            }
            .logo {
                color: #6fa1f8;
                font-size: 30px;
                font-weight: 700;
                letter-spacing: 1px;
            }
            span {
                color: white;
            }
            form {
                width: 300px;
                height: 40px;
                display: flex;
                background: rgba(255, 255, 255, 0.2);
                padding: 1px 1px;
                font-size: 15px;
                border-radius: 10px;
                backdrop-filter: blur(4px) saturate(180%);
            }
            form input {
                background: transparent;
                flex: 1;
                border: 0;
                outline: none;
                padding: 12px 20px;
                font-size: 15px;
                color: white;
            } 
            ::placeholder {
                color: white;
            }
            form button {
                border: 0;
                outline: none;
                padding: 5px 20px;
                color: white;
                border-radius: 10px;
                background: #6fa1f8;
                cursor: pointer;
            }
            .navbar li {
                list-style: none;
                display: inline-block;
                margin: 0 20px;
                position: relative;
            }
            .navbar li a {
                text-decoration: none;
                color: white;
                text-transform: uppercase;
            }
            .navbar li:hover {
                border: 1px;
                padding: 10px;
                color: white;
                background-color: #6fa1f8;
                transition: 0.5s; 
                cursor: pointer;
                border-radius: 30px;
            }
            .container {
                background: transparent;
                padding: 10px 5%;
                padding-bottom: 100px;
            }
            .container .box-container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
                gap: 20px;
            }
            .container .box-container .box {
                color: white;
                box-shadow: 0 5px 10px rgba(0,0,0,.2);
                border-radius: 20px;
                background: transparent;
                border: 1px solid white;
                padding: 20px 10px;
            }
            .container .box-container .box img {
                height: 40px;
                border-radius: 10px;
            }
            .container .box-container .box h3 {
                color: #6fa1f8;
                font-size: large;
                padding: 10px 0;
            }
            .container .box-container .box p {
                color: white;
                font-size: small;
                line-height: 1.5;
            }
            footer {
                background-color: #6fa1f8;
                margin-top: auto;
            }
        </style>
    </head>
<body>
    <div class="banner">
        <br>
        <div class="navbar">
            <h1 class="logo">C<span>ode</span>C<span>rafters</span></h1>
            <ul>
                <li><a href="http://127.0.0.1:8000/"> Home </a></li>
                <li><a href="http://127.0.0.1:8000/product" class="bg-product"> Products </a></li>
                <li><a href="http://127.0.0.1:8000/people"> People </a></li>
                <li><a href="http://127.0.0.1:8000/contact"> Contact </a></li>
            </ul>
            <form action="" method="get">
                <input type="text" placeholder="Enter to Search">
                <button type="submit"> Search </button>
            </form>
        </div>
        <div class="container">
            <div class="box-container">
                <div class="box">
                    <img src="{% static 'logo2.png' %}" alt="">
                    <h3> SiteGenie Builder </h3>
                    <p> Simplified drag and drop website creation. </p>
                </div>
                <div class="box">
                    <img src="{% static 'logo3.png' %}" alt="">
                    <h3> DevSync Hub Pro </h3>
                    <p> Efficient version control and sync. </p>
                </div>
                <div class="box">
                    <img src="{% static 'logo4.png' %}" alt="">
                    <h3> CodeLeap Toolkit </h3>
                    <p> Tools for innovative web development. </p>
                </div>
                <div class="box">
                    <img src="{% static 'logo9.png' %}" alt="">
                    <h3> Comtug Software </h3>
                    <p> Robust multi-layered website security. </p>
                </div>
                <div class="box">
                    <img src="{% static 'logo6.png' %}" alt="">
                    <h3> WebFlow Pro Studio </h3>
                    <p> Rapid low-code app creation. </p>
                </div>
                <div class="box">
                    <img src="{% static 'logo10.png' %}" alt="">
                    <h3> Norton Toolkit </h3>
                    <p> Automated testing and debugging. </p>
                </div>
                <div class="box">
                    <img src="{% static 'logo8.png' %}" alt="">
                    <h3> Teamm Code </h3>
                    <p> Streamlined code content management. </p>
                </div>
                <div class="box">
                    <img src="{% static 'logo11.png' %}" alt="">
                    <h3> WideFix </h3>
                    <p> Optimized code correcting tools. </p>
                </div>
                <div class="box">
                    <img src="{% static 'logo12.png' %}" alt="">
                    <h3> Datatech eSolutions </h3>
                    <p> Optimized code efficiency tools. </p>
                </div>

                <div class="box">
                    <img src="{% static 'logo13.png' %}" alt="">
                    <h3> World Soft </h3>
                    <p> Seamless high-traffic handling. </p>
                </div>
                <div class="box">
                    <img src="{% static 'logo14.png' %}" alt="">
                    <h3> MINDTECH </h3>
                    <p> Integrated tools for developers. </p>
                </div>
            </div>
        </div>
    </div>
    <footer>
        <center>Designed by : Naveen Kumar V (212223220068) </center>
    </footer>
</body>
</html>
people.html
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title> people page </title>
        <style type="text/css">
            * {
                margin: 0;
                padding: 0;
                font-family: Arial, Helvetica, sans-serif;
            }
            body {
                background: -webkit-linear-gradient(bottom, #2dbd6e, #a6f77b);
                background-repeat: no-repeat;
            }
            .banner {
                width: 100%;
                height: 100vh;
                background-image: linear-gradient(rgba(0,0,0,0.75),rgba(0,0,0,0.75));
                background-size: cover;
                background-position: center;
            }
            .navbar {
                width: 85%;
                margin: auto;
                padding: 35px 0;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            .bg-people {
                border: 1px;
                padding: 10px;
                color: white;
                background-color: #6fa1f8;
                border-radius: 30px;
            }
            .logo {
                color: #6fa1f8;
                font-size: 40px;
                font-weight: 700;
                letter-spacing: 0px;
            }
            span {
                color: white;
            }
            form {
                width: 300px;
                height: 40px;
                display: flex;
                background: rgba(255, 255, 255, 0.2);
                padding: 1px 1px;
                font-size: 15px;
                border-radius: 10px;
                backdrop-filter: blur(4px) saturate(180%);
            }
            form input {
                background: transparent;
                flex: 1;
                border: 0;
                outline: none;
                padding: 12px 20px;
                font-size: 15px;
                color: white;
            } 
            ::placeholder {
                color: white;
            }
            form button {
                border: 0;
                outline: none;
                padding: 5px 20px;
                color: white;
                border-radius: 10px;
                background: #6fa1f8;
                cursor: pointer;
            }
            .navbar li {
                list-style: none;
                display: inline-block;
                margin: 0 20px;
                position: relative;
            }
            .navbar li a {
                text-decoration: none;
                color: white;
                text-transform: uppercase;
            }
            .navbar li:hover {
                border: 1px;
                padding: 10px;
                color: white;
                background-color: #6fa1f8;
                transition: 0.5s; 
                cursor: pointer;
                border-radius: 30px;
            }
            .image {
                position: relative;
                border: 0;
                top: 70px;
                background: transparent;
            }
            .image table {
                border: 0;
                color: white;
                position: relative;
                left: 150px;
            }
            .image table img {
                height: 140px;
                width: 140px;
                border: 2px solid white;
                padding: 5px;
                border-radius: 50%;
            }
            .image table td {
                color: #6fa1f8;
            }
            footer {
                background-color: #6fa1f8;
                margin-top: auto;
            }
        </style>
    </head>
<body>
    {%load static%}
    <div class="banner">
        <br>
        <div class="navbar">
            <h1 class="logo">C<span>ode</span>C<span>rafters</span></h1>
            <ul>
                <li><a href="{%url 'h'%}"> Home </a></li>
                <li><a href="http://127.0.0.1:8000/product/"> Products </a></li>
                <li><a href="http://127.0.0.1:8000/people/" class="bg-product"> People </a></li>
                <li><a href="http://127.0.0.1:8000/contact/"> Contact </a></li>
            </ul>
            <form action="" method="get">
                <input type="text" placeholder="Enter to Search">
                <button type="submit"> Search </button>
            </form>
        </div>
        <div class="image">
            <table cellspacing="20"> 
                <tr align="center">
                    <td> <img src="{%static "my.jpg"%}"> </td>
                    <td> <img src="{%static "js.jpg"%}"> </td>
                    <td> <img src="{%static "sk.jpg"%}"> </td>
                    <td> <img src="{%static "sri.jpg"%}"> </td>
                    <td> <img src="{%static "pandi.jpg"%}"> </td>
                </tr>
                <tr align="center">
                    <th> Naveen Kumar V</th>
                    <th> Jayaseelan U </th>
                    <th> Siva kumar  </th>
                    <th> Sridhar </th>
                    <th> Pandi Kumar </th>
                </tr>
                <tr align="center">
                    <td> CEO </td>
                    <td> CEO, Co-Founder </td>
                    <td> CTO, Co-Founder </td>
                    <td> Director </td>
                    <td> Asst. Director </td>
                </tr>
            </table>
        </div>
    </div>
    <footer>
        <center> Designed by : Naveen Kumar V (212223220068)  </center>
    </footer>
</body>
</html>
contact.html

<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title> Contact Us Page </title>
        <style type="text/css">
            * {
                margin: 0;
                padding: 0;
                font-family: Arial, Helvetica, sans-serif;
            }
            body {
                background: -webkit-linear-gradient(bottom, #2dbd6e, #a6f77b);
                background-repeat: no-repeat;
            }
            a {
                text-decoration: none;
              }
            .banner {
                width: 100%;
                height: 100vh;
                background-image: linear-gradient(rgba(0,0,0,0.75),rgba(0,0,0,0.75)),url(background.jpg);
                background-size: cover;
                background-position: center;
            }
            .navbar {
                width: 85%;
                margin: auto;
                padding: 35px 0;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            .bg-contact {
                border: 1px;
                padding: 10px;
                color: white;
                background-color: #6fa1f8;
                border-radius: 30px;
            }
            .logo {
                color: #6fa1f8;
                font-size: 30px;
                font-weight: 700;
                letter-spacing: 1px;
            }
            span {
                color: white;
            }
            .navbar form {
                width: 300px;
                height: 40px;
                display: flex;
                background: rgba(255, 255, 255, 0.2);
                padding: 1px 1px;
                font-size: 15px;
                border-radius: 10px;
                backdrop-filter: blur(4px) saturate(180%);
            }
            .navbar form input {
                background: transparent;
                flex: 1;
                border: 0;
                outline: none;
                padding: 12px 20px;
                font-size: 15px;
                color: white;
            } 
            ::placeholder {
                color: white;
            }
            .navbar form button {
                border: 0;
                outline: none;
                padding: 5px 20px;
                color: white;
                border-radius: 10px;
                background: #6fa1f8;
                cursor: pointer;
            }
            .navbar li {
                list-style: none;
                display: inline-block;
                margin: 0 20px;
                position: relative;
            }
            .navbar li a {
                text-decoration: none;
                color: white;
                text-transform: uppercase;
            }
            .navbar li:hover {
                border: 1px;
                padding: 10px;
                color: white;
                background-color: #6fa1f8;
                transition: 0.5s; 
                cursor: pointer;
                border-radius: 30px;
            }
            .box {
                display: flex;
                column-gap: 40px;

                top: 50px;
            }
            .box-1 {
                height: 400px;
                width: 350px;
                border: 3px solid white;
                border-radius: 20px;
                background: transparent;
                position: relative;
                left: 250px;
            }
            .box-2 {
                height: 400px;
                width: 400px;
                border: 3px solid #6fa1f8;
                border-radius: 20px;
                background: transparent;
                position: relative;
                left: 300px;
            }
            .box-1 form {
                display: flex;
                color: white;
                background: transparent;
                padding: 10px;
                font-size: 15px;

                top: 10px;
            }
            .box-1 form input {
                background: transparent;
                display: flex;
                border: 1px solid white;
                border-radius: 10px;
                padding: 8px 30px;
                font-size: 15px;


                top: 20px;
            }
           
            .box-2 h2 {
                color: white;
                position: relative;
                top: 25px;
                left: 50px;
                font-size: 30px;
            }
            .box-2 p {
                color: white;
                position: relative;
                top: 50px;
                padding: 10px 80px;
            }
            .box-2 span {
                color: #6fa1f8;
                font-size: 20px;
            }
            footer {
                background-color: #6fa1f8;
                margin-top: auto;
            }
            label {
                font-family: "Raleway", sans-serif;
                font-size: 10pt;
              }
              #forgot-pass {
                color: #2dbd6e;
                font-family: "Raleway", sans-serif;
                font-size: 10pt;
                margin-top: 3px;
                text-align: right;
              }
              #card {
                background: #fbfbfb;
                border-radius: 5px;
                box-shadow: 1px 2px 8px rgba(0, 0, 0, 0.65);
                height: 380px;
                margin: 0.6rem auto 1rem auto;
                width: 329px;
              }
              #card-content {
                padding: 15px 44px;
              }
              #card-title {
                font-family: "Raleway Thin", sans-serif;
                letter-spacing: 4px;
                padding-bottom: 23px;
                padding-top: 13px;
                text-align: center;
              }
              #signup {
                color: #2dbd6e;
                font-family: "Raleway", sans-serif;
                font-size: 10pt;
                margin-top: 16px;
                text-align: center;
              }
              #submit-btn {
                background: -webkit-linear-gradient(right, #a6f77b, #2dbd6e);
                border: none;
                border-radius: 21px;
                box-shadow: 0px 1px 8px #24c64f;
                cursor: pointer;
                color: white;
                font-family: "Raleway SemiBold", sans-serif;
                height: 42.3px;
                margin: 0 auto;
                margin-top: 50px;
                transition: 0.25s;
                width: 153px;
              }
              #submit-btn:hover {
                box-shadow: 0px 1px 18px #24c64f;
              }
              .form {
                align-items: left;
                display: flex;
                flex-direction: column;
              }
              .form-border {
                background: -webkit-linear-gradient(right, #a6f77b, #2ec06f);
                height: 1px;
                width: 100%;
              }
              .form-content {
                background: #fbfbfb;
                border: none;
                outline: none;
                padding-top: 14px;
              }
              .underline-title {
                background: -webkit-linear-gradient(right, #a6f77b, #2ec06f);
                height: 2px;
                margin: -1.1rem auto 0 auto;
                width: 89px;
              }
              
        </style>
    </head>
<body>
    <div class="banner">
        <br>
        <div class="navbar">
            <h1 class="logo">C<span>ode</span>C<span>rafters</span></h1>
            <ul>
                <li><a href="http://127.0.0.1:8000/"> Home </a></li>
                <li><a href="http://127.0.0.1:8000/product"> Products </a></li>
                <li><a href="http://127.0.0.1:8000/people"> People </a></li>
                <li><a href="http://127.0.0.1:8000/contact" class="bg-contact"> Contact </a></li>
            </ul>
            <form action="" method="get">
                <input type="text" placeholder="Enter to Search">
                <button type="submit"> Search </button>
            </form>
        </div>
        <div class="box">
            <div class="box-1">
                <center>
                        <div id="card">
                            <div id="card-content">
                              <div id="card-title">
                                <h2>LOGIN</h2>
                                <div class="underline-title"></div>
                              </div>
                              <form method="post" class="form">
                                <label for="user-email" style="padding-top:13px; color: black;">
                                    &nbsp;Email
                                  </label>
                                <input id="user-email" class="form-content" type="email" name="email" autocomplete="on" required />
                                <div class="form-border"></div>
                                <label for="user-password" style="padding-top:22px; color:black;">&nbsp;Password
                                  </label>
                                <input id="user-password" class="form-content" type="password" name="password" required />
                                <div class="form-border"></div>
                                <a href="#">
                                  <legend id="forgot-pass">Forgot password?</legend>
                                </a>
                                <input id="submit-btn" type="submit" name="submit" value="LOGIN" />
                                <a href="#" id="signup">Don't have account yet?</a>
                              </form>
                            </div>
                          </div>
                        </center>
                    </div>
            <div class="box-2"> 
                <h2> Contact Information </h2>
                <p> <span>Address</span> ponnamallee , chennai </p>
                <p> <span>Email</span> : codecrafters@gmail.com </p>
                <p> <span>Phone</span> : +91 1234567890</p>
            </div>
        </div>
    </div>
    <footer>
        <center> Designed by : Naveen Kumar V (212223220068)  </center>
    </footer>
</body>
</html>
```

## OUTPUT:
<img width="906" alt="home" src="https://github.com/NaveenKumarV2005/softweb/assets/151476286/de95d2ac-1753-412f-8426-357953f9073d">
<img width="892" alt="product" src="https://github.com/NaveenKumarV2005/softweb/assets/151476286/979da81a-b3cc-48d1-9442-4dacccff685c">
<img width="905" alt="people" src="https://github.com/NaveenKumarV2005/softweb/assets/151476286/5a0e9c34-efd3-4ccb-b4d7-6a72c85cee45">
<img width="905" alt="contack" src="https://github.com/NaveenKumarV2005/softweb/assets/151476286/413b7d66-3bed-4bc6-86c6-89f25aa946ee">

## RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
