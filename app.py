from flask import Flask, render_template_string

app = Flask(__name__)

portfolio = """

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Kashaf Shaikh | Portfolio</title>

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:'Poppins',sans-serif;
            scroll-behavior:smooth;
        }

        body{
            background:#0b1120;
            color:white;
            overflow-x:hidden;
        }

        /* Navbar */

        nav{
            width:100%;
            padding:20px 10%;
            display:flex;
            justify-content:space-between;
            align-items:center;
            position:fixed;
            top:0;
            z-index:1000;
            background:rgba(10,15,30,0.8);
            backdrop-filter:blur(10px);
        }

        nav h1{
            color:#7dd3fc;
            font-size:28px;
            font-weight:700;
        }

        nav ul{
            display:flex;
            list-style:none;
        }

        nav ul li{
            margin-left:25px;
        }

        nav ul li a{
            color:#cbd5e1;
            text-decoration:none;
            transition:0.3s;
            font-size:15px;
        }

        nav ul li a:hover{
            color:#7dd3fc;
        }

        /* Hero */

        .hero{
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            text-align:center;
            padding:20px;
            background:radial-gradient(circle at top,#1e293b,#020617);
        }

        .hero-content{
            max-width:850px;
        }

        .hero h2{
            font-size:72px;
            font-weight:700;
            background:linear-gradient(to right,#7dd3fc,#38bdf8);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
        }

        .hero h3{
            margin-top:15px;
            font-size:28px;
            color:#e2e8f0;
            font-weight:400;
        }

        .hero p{
            margin-top:25px;
            color:#94a3b8;
            line-height:1.8;
            font-size:18px;
        }

        .hero-buttons{
            margin-top:40px;
        }

        .btn{
            display:inline-block;
            padding:14px 32px;
            margin:10px;
            border-radius:12px;
            text-decoration:none;
            transition:0.3s;
            font-weight:600;
        }

        .btn-primary{
            background:#38bdf8;
            color:black;
        }

        .btn-primary:hover{
            transform:translateY(-4px);
            box-shadow:0 10px 25px rgba(56,189,248,0.4);
        }

        .btn-secondary{
            border:1px solid #334155;
            color:white;
        }

        .btn-secondary:hover{
            background:#1e293b;
        }

        /* Sections */

        section{
            padding:100px 10%;
        }

        .section-title{
            text-align:center;
            font-size:42px;
            margin-bottom:60px;
            color:#7dd3fc;
        }

        /* About */

        .about{
            display:grid;
            grid-template-columns:1fr 1fr;
            gap:35px;
        }

        .card{
            background:rgba(30,41,59,0.6);
            border:1px solid rgba(255,255,255,0.08);
            backdrop-filter:blur(10px);
            padding:35px;
            border-radius:24px;
            transition:0.3s;
        }

        .card:hover{
            transform:translateY(-8px);
            box-shadow:0 12px 30px rgba(0,0,0,0.4);
        }

        .card h3{
            margin-bottom:20px;
            color:#7dd3fc;
            font-size:24px;
        }

        .card p, li{
            color:#cbd5e1;
            line-height:1.9;
        }

        ul{
            padding-left:20px;
        }

        /* Skills */

        .skills{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(160px,1fr));
            gap:20px;
        }

        .skill{
            background:#111827;
            padding:22px;
            text-align:center;
            border-radius:18px;
            border:1px solid rgba(255,255,255,0.05);
            transition:0.3s;
            font-weight:500;
        }

        .skill:hover{
            transform:translateY(-6px);
            background:#1e293b;
            color:#7dd3fc;
        }

        /* Projects */

        .projects{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
            gap:30px;
        }

        .project{
            background:#111827;
            padding:30px;
            border-radius:24px;
            transition:0.3s;
            border:1px solid rgba(255,255,255,0.05);
        }

        .project:hover{
            transform:translateY(-8px);
            box-shadow:0 12px 25px rgba(0,0,0,0.5);
        }

        .project h3{
            color:#7dd3fc;
            margin-bottom:18px;
            font-size:24px;
        }

        .project p{
            color:#cbd5e1;
            line-height:1.8;
        }

        /* Contact */

        .contact{
            text-align:center;
        }

        .contact p{
            margin-top:15px;
            color:#cbd5e1;
            font-size:18px;
        }

        /* Footer */

        footer{
            text-align:center;
            padding:30px;
            background:#020617;
            color:#94a3b8;
            margin-top:40px;
        }

        /* Responsive */

        @media(max-width:900px){

            .hero h2{
                font-size:48px;
            }

            .hero h3{
                font-size:22px;
            }

            .about{
                grid-template-columns:1fr;
            }

            nav{
                flex-direction:column;
            }

            nav ul{
                margin-top:15px;
            }

        }

    </style>

</head>

<body>

    <!-- Navbar -->

    <nav>

        <h1>Kashaf</h1>

        <ul>

            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>

        </ul>

    </nav>

    <!-- Hero -->

    <section class="hero">

        <div class="hero-content">

            <h2>Kashaf Shaikh</h2>

            <h3>
                Third Year Engineering Student
            </h3>

            <p>
                Passionate Full Stack Developer and AI Enthusiast focused on
                building scalable web applications, machine learning systems,
                and modern software solutions.
            </p>

            <div class="hero-buttons">

                <a href="#projects" class="btn btn-primary">
                    View Projects
                </a>

                <a href="#contact" class="btn btn-secondary">
                    Contact Me
                </a>

            </div>

        </div>

    </section>

    <!-- About -->

    <section id="about">

        <h2 class="section-title">About Me</h2>

        <div class="about">

            <div class="card">

                <h3>Profile</h3>

                <p>
                    I am a Third Year Engineering student with strong interest in
                    Full Stack Development, Artificial Intelligence, Machine Learning,
                    and Backend Development.
                </p>

                <br>

                <p>
                    I completed a Web Development Internship at CodeSoft where
                    I worked on real-world frontend and backend applications.
                </p>

            </div>

            <div class="card">

                <h3>Highlights</h3>

                <ul>

                    <li>Completed Web Development Internship at CodeSoft</li>
                    <li>Built AI-based and Full Stack Projects</li>
                    <li>Solved 60+ DSA Problems</li>
                    <li>Strong knowledge of SQL and MongoDB</li>
                    <li>Interested in scalable software systems</li>

                </ul>

            </div>

        </div>

    </section>

    <!-- Skills -->

    <section id="skills">

        <h2 class="section-title">Technical Skills</h2>

        <div class="skills">

            <div class="skill">Python</div>
            <div class="skill">Java</div>
            <div class="skill">Flask</div>
            <div class="skill">HTML</div>
            <div class="skill">CSS</div>
            <div class="skill">JavaScript</div>
            <div class="skill">SQL</div>
            <div class="skill">MongoDB</div>
            <div class="skill">Machine Learning</div>
            <div class="skill">DSA</div>

        </div>

    </section>

    <!-- Projects -->

    <section id="projects">

        <h2 class="section-title">Projects</h2>

        <div class="projects">

            <div class="project">

                <h3>Revogue AI</h3>

                <p>
                    AI-powered sustainable fashion platform with intelligent
                    recommendations and smart wardrobe management.
                </p>

            </div>

            <div class="project">

                <h3>Hospital Management System</h3>

                <p>
                    Full Stack web application developed using Flask and SQL
                    for managing hospital operations efficiently.
                </p>

            </div>

            <div class="project">

                <h3>Auto Tax Calculator</h3>

                <p>
                    AI-driven tax prediction and calculation platform using
                    trading data and country-wise tax rules.
                </p>

            </div>

            <div class="project">

                <h3>Language Translation System</h3>

                <p>
                    Real-time NLP and Machine Learning based face-to-face
                    translation application.
                </p>

            </div>

        </div>

    </section>

    <!-- Contact -->

    <section id="contact">

        <h2 class="section-title">Contact</h2>

        <div class="card contact">

            <p>Email : kashaf@example.com</p>

            <p>LinkedIn : linkedin.com/in/kashaf</p>

            <p>GitHub : github.com/kashaf</p>

        </div>

    </section>

    <!-- Footer -->

    <footer>

        <p>
            © 2026 Kashaf Shaikh | Portfolio Website
        </p>

    </footer>

</body>

</html>

"""

@app.route('/')
def home():
    return render_template_string(portfolio)

if __name__ == '__main__':
    app.run(debug=True)