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

        <style>

            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Arial, Helvetica, sans-serif;
            }

            body{
                background:#0f172a;
                color:white;
            }

            header{
                background:#020617;
                padding:20px 40px;
                display:flex;
                justify-content:space-between;
                align-items:center;
                border-bottom:1px solid #1e293b;
            }

            header h1{
                color:#38bdf8;
            }

            nav a{
                color:white;
                text-decoration:none;
                margin-left:20px;
                transition:0.3s;
            }

            nav a:hover{
                color:#38bdf8;
            }

            .hero{
                padding:100px 40px;
                text-align:center;
                background:linear-gradient(to right,#0f172a,#1e293b);
            }

            .hero h2{
                font-size:52px;
                margin-bottom:20px;
            }

            .hero p{
                max-width:800px;
                margin:auto;
                line-height:1.8;
                color:#cbd5e1;
                font-size:18px;
            }

            .button{
                display:inline-block;
                margin-top:30px;
                padding:15px 30px;
                background:#38bdf8;
                color:black;
                text-decoration:none;
                border-radius:10px;
                font-weight:bold;
                transition:0.3s;
            }

            .button:hover{
                background:white;
            }

            .section{
                padding:80px 40px;
                max-width:1200px;
                margin:auto;
            }

            .section-title{
                font-size:38px;
                margin-bottom:50px;
                text-align:center;
                color:#38bdf8;
            }

            .cards{
                display:grid;
                grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
                gap:30px;
            }

            .card{
                background:#1e293b;
                padding:30px;
                border-radius:20px;
                border:1px solid #334155;
                transition:0.3s;
            }

            .card:hover{
                transform:translateY(-5px);
                border-color:#38bdf8;
            }

            .card h3{
                margin-bottom:20px;
                color:#38bdf8;
            }

            .card p{
                color:#cbd5e1;
                line-height:1.7;
            }

            .about{
                background:#111827;
                border-radius:20px;
                padding:40px;
                line-height:1.9;
                color:#d1d5db;
            }

            footer{
                text-align:center;
                padding:30px;
                border-top:1px solid #1e293b;
                margin-top:50px;
                color:#94a3b8;
            }

        </style>

    </head>

    <body>

        <header>
            <h1>Meteora IA</h1>

            <nav>
                <a href="#capacitaciones">Capacitaciones</a>
                <a href="#meteora">Meteora</a>
                <a href="#carlos">Carlos Nieblas</a>
            </nav>
        </header>

        <section class="hero">

            <h2>Capacitación Profesional en IA y Databricks</h2>

            <p>
                Aprende Machine Learning, MLOps, Data Engineering y plataformas modernas
                de inteligencia artificial utilizadas por empresas de alto nivel.
            </p>

            <a class="button" href="#capacitaciones">
                Ver Capacitaciones
            </a>

        </section>

        <section class="section" id="capacitaciones">

            <h2 class="section-title">
                Programas de Capacitación
            </h2>

            <div class="cards">

                <div class="card">
                    <h3>Databricks Fundamentals</h3>

                    <p>
                        Introducción completa a Databricks, Spark, notebooks,
                        Delta Lake y arquitectura moderna de datos.
                        Ideal para iniciar en el ecosistema de Data & AI.
                    </p>
                </div>

                <div class="card">
                    <h3>Machine Learning Engineer</h3>

                    <p>
                        Entrenamiento práctico en pipelines de Machine Learning,
                        feature engineering, entrenamiento de modelos,
                        MLflow y despliegue productivo.
                    </p>
                </div>

                <div class="card">
                    <h3>MLOps & AI Platform Engineering</h3>

                    <p>
                        Implementación profesional de plataformas ML empresariales,
                        CI/CD para modelos, observabilidad, gobierno y automatización
                        de infraestructura AI.
                    </p>
                </div>

            </div>

        </section>

        <section class="section" id="meteora">

            <h2 class="section-title">
                ¿Qué es Meteora IA?
            </h2>

            <div class="about">

                <p>
                    Meteora IA es una iniciativa enfocada en democratizar el acceso
                    a capacitación avanzada en Inteligencia Artificial, Machine Learning,
                    MLOps y plataformas modernas de datos.
                </p>

                <br>

                <p>
                    El objetivo es acelerar el crecimiento profesional de ingenieros,
                    científicos de datos y desarrolladores mediante contenido práctico,
                    profesional y orientado a necesidades reales de la industria.
                </p>

                <br>

                <p>
                    Meteora busca convertirse en una plataforma educativa especializada
                    en tecnologías empresariales de IA, arquitectura de datos y despliegue
                    de soluciones inteligentes escalables.
                </p>

            </div>

        </section>

        <section class="section" id="carlos">

            <h2 class="section-title">
                Carlos Nieblas
            </h2>

            <div class="about">

                <p>
                    Carlos Nieblas es ingeniero especializado en Machine Learning,
                    plataformas de Inteligencia Artificial y tecnologías modernas
                    de datos empresariales.
                </p>

                <br>

                <p>
                    Su experiencia se enfoca en desarrollo de soluciones AI,
                    arquitectura de plataformas ML, automatización y capacitación
                    técnica en tecnologías como Databricks, Spark, MLflow y MLOps.
                </p>

                <br>

                <p>
                    A través de Meteora IA busca compartir conocimiento práctico,
                    profesional y accesible para acelerar el desarrollo de talento
                    tecnológico en Latinoamérica.
                </p>

            </div>

        </section>

        <footer>
            © 2026 Meteora IA - Plataforma de Capacitación en Inteligencia Artificial
        </footer>

    </body>
    </html>
    """

    return render_template_string(html)