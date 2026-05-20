from flask import Blueprint, render_template_string

main = Blueprint("main", __name__)

@main.route("/")
def home():

    html = """

<!DOCTYPE html>
<html lang="es">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Meteora IA</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        html{
            scroll-behavior:smooth;
        }

        body{
            font-family:'Inter', sans-serif;
            background:#020617;
            color:white;
            overflow-x:hidden;
        }

        body::before{
            content:'';
            position:fixed;
            width:700px;
            height:700px;
            background:radial-gradient(circle, rgba(56,189,248,0.15) 0%, rgba(2,6,23,0) 70%);
            top:-200px;
            right:-200px;
            z-index:-1;
        }

        body::after{
            content:'';
            position:fixed;
            width:600px;
            height:600px;
            background:radial-gradient(circle, rgba(139,92,246,0.12) 0%, rgba(2,6,23,0) 70%);
            bottom:-200px;
            left:-200px;
            z-index:-1;
        }

        header{
            position:fixed;
            top:0;
            width:100%;
            z-index:1000;
            backdrop-filter:blur(12px);
            background:rgba(2,6,23,0.75);
            border-bottom:1px solid rgba(255,255,255,0.06);
        }

        .nav-container{
            max-width:1300px;
            margin:auto;
            padding:20px 40px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }

        .logo{
            font-size:28px;
            font-weight:800;
            background:linear-gradient(to right,#38bdf8,#8b5cf6);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
        }

        nav{
            display:flex;
            align-items:center;
            gap:35px;
        }

        nav a{
            text-decoration:none;
            color:#cbd5e1;
            font-size:15px;
            transition:0.3s;
        }

        nav a:hover{
            color:white;
        }

        .auth-buttons{
            display:flex;
            gap:15px;
            margin-left:20px;
        }

        .login-btn{
            padding:10px 20px;
            border:1px solid rgba(255,255,255,0.12);
            border-radius:12px;
            color:white;
            text-decoration:none;
            transition:0.3s;
        }

        .login-btn:hover{
            background:rgba(255,255,255,0.06);
        }

        .register-btn{
            padding:10px 22px;
            border-radius:12px;
            background:linear-gradient(to right,#38bdf8,#8b5cf6);
            color:white;
            text-decoration:none;
            font-weight:600;
            transition:0.3s;
        }

        .register-btn:hover{
            transform:translateY(-2px);
            opacity:0.92;
        }

        .hero{
            min-height:100vh;
            display:flex;
            align-items:center;
            justify-content:center;
            padding:120px 40px 80px;
        }

        .hero-content{
            max-width:950px;
            text-align:center;
        }

        .hero-badge{
            display:inline-block;
            padding:10px 18px;
            border-radius:999px;
            background:rgba(56,189,248,0.1);
            border:1px solid rgba(56,189,248,0.25);
            color:#38bdf8;
            margin-bottom:30px;
            font-size:14px;
        }

        .hero h1{
            font-size:72px;
            line-height:1.05;
            margin-bottom:30px;
            font-weight:800;
        }

        .gradient-text{
            background:linear-gradient(to right,#38bdf8,#8b5cf6);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
        }

        .hero p{
            font-size:20px;
            line-height:1.8;
            color:#cbd5e1;
            max-width:850px;
            margin:auto;
        }

        .hero-buttons{
            margin-top:45px;
            display:flex;
            justify-content:center;
            gap:20px;
            flex-wrap:wrap;
        }

        .primary-btn{
            padding:16px 32px;
            border-radius:14px;
            text-decoration:none;
            background:linear-gradient(to right,#38bdf8,#8b5cf6);
            color:white;
            font-weight:600;
            transition:0.3s;
        }

        .primary-btn:hover{
            transform:translateY(-3px);
        }

        .secondary-btn{
            padding:16px 32px;
            border-radius:14px;
            text-decoration:none;
            border:1px solid rgba(255,255,255,0.12);
            color:white;
            transition:0.3s;
        }

        .secondary-btn:hover{
            background:rgba(255,255,255,0.05);
        }

        .section{
            max-width:1300px;
            margin:auto;
            padding:120px 40px;
        }

        .section-title{
            font-size:52px;
            margin-bottom:25px;
            text-align:center;
            font-weight:800;
        }

        .section-subtitle{
            text-align:center;
            color:#94a3b8;
            max-width:800px;
            margin:0 auto 70px;
            line-height:1.8;
            font-size:18px;
        }

        .cards{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
            gap:30px;
        }

        .card{
            background:rgba(15,23,42,0.8);
            border:1px solid rgba(255,255,255,0.06);
            border-radius:28px;
            padding:40px;
            transition:0.4s;
            position:relative;
            overflow:hidden;
        }

        .card::before{
            content:'';
            position:absolute;
            width:250px;
            height:250px;
            background:radial-gradient(circle, rgba(56,189,248,0.15) 0%, rgba(0,0,0,0) 70%);
            top:-100px;
            right:-100px;
        }

        .card:hover{
            transform:translateY(-8px);
            border-color:rgba(56,189,248,0.35);
        }

        .card h3{
            font-size:26px;
            margin-bottom:22px;
            color:white;
        }

        .card p{
            color:#cbd5e1;
            line-height:1.9;
            margin-bottom:30px;
        }

        .card-button{
            display:inline-block;
            padding:12px 22px;
            border-radius:12px;
            background:rgba(56,189,248,0.12);
            color:#38bdf8;
            text-decoration:none;
            transition:0.3s;
        }

        .card-button:hover{
            background:rgba(56,189,248,0.22);
        }

        .about-box{
            background:rgba(15,23,42,0.75);
            border:1px solid rgba(255,255,255,0.06);
            border-radius:30px;
            padding:60px;
            line-height:2;
            color:#cbd5e1;
            font-size:18px;
        }

        footer{
            border-top:1px solid rgba(255,255,255,0.06);
            text-align:center;
            padding:40px;
            color:#94a3b8;
            margin-top:80px;
        }

        @media(max-width:900px){

            .hero h1{
                font-size:48px;
            }

            nav{
                display:none;
            }

            .section-title{
                font-size:38px;
            }

            .about-box{
                padding:35px;
            }

        }

    </style>

</head>

<body>

    <header>

        <div class="nav-container">

            <div class="logo">
                Meteora IA
            </div>

            <nav>

                <a href="#capacitaciones">Capacitaciones</a>
                <a href="#meteora">Meteora</a>
                <a href="#carlos">Carlos Nieblas</a>

                <div class="auth-buttons">

                    <a href="#" class="login-btn">
                        Iniciar Sesión
                    </a>

                    <a href="#" class="register-btn">
                        Crear Cuenta
                    </a>

                </div>

            </nav>

        </div>

    </header>

    <section class="hero">

        <div class="hero-content">

            <div class="hero-badge">
                Plataforma Profesional de AI & Machine Learning
            </div>

            <h1>
                Aprende
                <span class="gradient-text">
                    Databricks, ML y MLOps
                </span>
                con enfoque empresarial
            </h1>

            <p>
                Capacitación avanzada orientada a ingenieros, científicos de datos
                y profesionales que buscan dominar arquitecturas modernas de
                inteligencia artificial, Machine Learning y plataformas empresariales.
            </p>

            <div class="hero-buttons">

                <a href="#capacitaciones" class="primary-btn">
                    Explorar Programas
                </a>

                <a href="#meteora" class="secondary-btn">
                    Conocer Meteora
                </a>

            </div>

        </div>

    </section>

    <section class="section" id="capacitaciones">

        <h2 class="section-title">
            Programas de Capacitación
        </h2>

        <p class="section-subtitle">
            Entrenamientos diseñados para acelerar el crecimiento profesional
            en tecnologías de inteligencia artificial y plataformas modernas de datos.
        </p>

        <div class="cards">

            <div class="card">

                <h3>Databricks Fundamentals</h3>

                <p>
                    Aprende Spark, notebooks, Delta Lake, arquitectura lakehouse,
                    procesamiento distribuido y fundamentos de plataformas modernas
                    de datos empresariales.
                </p>

                <a href="#" class="card-button">
                    Ver Programa
                </a>

            </div>

            <div class="card">

                <h3>Machine Learning Engineer</h3>

                <p>
                    Entrenamiento práctico en feature engineering, entrenamiento
                    de modelos, MLflow, evaluación de modelos y despliegue
                    de soluciones AI productivas.
                </p>

                <a href="#" class="card-button">
                    Ver Programa
                </a>

            </div>

            <div class="card">

                <h3>MLOps & AI Platform Engineering</h3>

                <p>
                    Construcción profesional de plataformas ML empresariales,
                    CI/CD para modelos, automatización, observabilidad
                    y gobierno de inteligencia artificial.
                </p>

                <a href="#" class="card-button">
                    Ver Programa
                </a>

            </div>

        </div>

    </section>

    <section class="section" id="meteora">

        <h2 class="section-title">
            ¿Qué es Meteora IA?
        </h2>

        <div class="about-box">

            <p>
                Meteora IA es una plataforma especializada en capacitación avanzada
                en Inteligencia Artificial, Machine Learning, MLOps y arquitecturas
                modernas de datos empresariales.
            </p>

            <br>

            <p>
                Nuestro objetivo es democratizar el acceso a formación profesional
                de alto nivel mediante contenido práctico, enfocado en escenarios
                reales de la industria tecnológica moderna.
            </p>

            <br>

            <p>
                La plataforma está diseñada para acelerar el crecimiento de ingenieros,
                desarrolladores y científicos de datos que buscan construir soluciones
                escalables de AI y plataformas de Machine Learning empresariales.
            </p>

        </div>

    </section>

    <section class="section" id="carlos">

        <h2 class="section-title">
            Carlos Nieblas
        </h2>

        <div class="about-box">

            <p>
                Carlos Nieblas es ingeniero especializado en Machine Learning,
                arquitecturas AI y plataformas modernas de datos empresariales.
            </p>

            <br>

            <p>
                Su experiencia se enfoca en construcción de soluciones AI,
                MLOps, automatización, ingeniería de plataformas y tecnologías
                modernas como Databricks, Spark y MLflow.
            </p>

            <br>

            <p>
                A través de Meteora IA busca compartir conocimiento práctico
                y profesional para impulsar el desarrollo de talento tecnológico
                en Latinoamérica.
            </p>

        </div>

    </section>

    <footer>
        © 2026 Meteora IA · AI Engineering · Machine Learning · Databricks
    </footer>

</body>

</html>

    """

    return render_template_string(html)