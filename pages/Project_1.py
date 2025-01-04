import streamlit as st
import json
import os

# Настройка страницы
st.set_page_config(
    page_title="Проект 1",
    page_icon="🚀",
    layout="wide"
)

# Функция для загрузки данных
def load_portfolio_data():
    if os.path.exists("data/portfolio_data.json"):
        with open("data/portfolio_data.json", "r", encoding='utf-8') as f:
            return json.load(f)
    return {}

# Загружаем данные
portfolio_data = load_portfolio_data()

# Значения по умолчанию для проекта
default_project = {
    "description": "Веб-приложение с использованием React и FastAPI",
    "image": "static/images/project1.jpg",
    "url": "Project_1",
    "details": {
        "about": "Описание проекта",
        "features": [
            "Особенность 1: Описание",
            "Особенность 2: Описание",
            "Особенность 3: Описание"
        ],
        "tech_stack": {
            "frontend": ["React", "TypeScript", "Material-UI"],
            "backend": ["Python", "FastAPI", "PostgreSQL"],
            "devops": ["Docker", "AWS", "CI/CD"]
        }
    }
}

# Получаем данные проекта с обработкой ошибок
try:
    project_data = portfolio_data.get("projects", {}).get("Проект 1", default_project)
except Exception as e:
    st.error(f"Ошибка при загрузке данных проекта: {str(e)}")
    project_data = default_project

# Добавление CSS
st.markdown("""
    <style>
        .main {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        .stTitle {
            color: #00ff9d !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .stHeader {
            color: #00ccff !important;
        }
        p {
            color: #ffffff !important;
        }
        .tech-stack {
            background-color: #2d2d2d;
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            border: 1px solid #3d3d3d;
        }
        .feature {
            background-color: #2d2d2d;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
            border: 1px solid #3d3d3d;
            transition: transform 0.3s ease;
            word-wrap: break-word;
            white-space: pre-wrap;
            overflow-wrap: break-word;
            max-width: 100%;
        }
        .feature:hover {
            transform: translateY(-5px);
        }
        /* Стили для изображения проекта */
        [data-testid="stImage"] > img {
            border-radius: 15px;
            border: 2px solid #00ccff;
            box-shadow: 0 0 20px rgba(0, 204, 255, 0.3);
            max-width: 100%;
            height: auto;
        }
        .project-links {
            display: flex;
            gap: 1rem;
            margin: 1rem 0;
        }
        .project-link {
            display: inline-block;
            padding: 0.5rem 1rem;
            background-color: #2d2d2d;
            color: #00ccff !important;
            text-decoration: none;
            border-radius: 5px;
            border: 1px solid #3d3d3d;
            transition: all 0.3s ease;
        }
        .project-link:hover {
            background-color: #3d3d3d;
            transform: translateY(-2px);
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }
        .github-link {
            background-color: #24292e;
        }
        .website-link {
            background-color: #2d2d2d;
        }
    </style>
""", unsafe_allow_html=True)

# Заголовок проекта
st.title(f"Проект 1: {project_data['description']}")

# Основное изображение проекта
st.image(project_data["image"], use_column_width=True)

# Описание проекта
st.header("О проекте")
st.write(project_data["details"]["about"])

# Добавляем ссылки на проект
if "links" in project_data:
    st.markdown('<div class="project-links">', unsafe_allow_html=True)
    
    if project_data["links"].get("github"):
        st.markdown(
            f'<a href="{project_data["links"]["github"]}" target="_blank" class="project-link github-link">🔗 GitHub</a>',
            unsafe_allow_html=True
        )
    
    if project_data["links"].get("website"):
        st.markdown(
            f'<a href="{project_data["links"]["website"]}" target="_blank" class="project-link website-link">🌐 Веб-сайт</a>',
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Технический стек
st.header("Технический стек")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<div class="tech-stack">🔧 Frontend:<br>• ' + '<br>• '.join(project_data["details"]["tech_stack"]["frontend"]) + '</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="tech-stack">⚙️ Backend:<br>• ' + '<br>• '.join(project_data["details"]["tech_stack"]["backend"]) + '</div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="tech-stack">🛠️ DevOps:<br>• ' + '<br>• '.join(project_data["details"]["tech_stack"]["devops"]) + '</div>', unsafe_allow_html=True)

# Ключевые особенности
st.header("Ключевые особенности")
for feature in project_data["details"]["features"]:
    st.markdown(f'<div class="feature">{feature}</div>', unsafe_allow_html=True)

# Добавляем кнопку возврата на главную
if st.button("← Вернуться на главную"):
    st.switch_page("portfolio.py") 