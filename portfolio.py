import streamlit as st
import json
import os

# Настройка конфигурации страницы
st.set_page_config(
    page_title="Моё Портфолио",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"  # Автоматически открываем боковое меню
)

# Функция для загрузки данных
def load_portfolio_data():
    if os.path.exists("data/portfolio_data.json"):
        with open("data/portfolio_data.json", "r", encoding='utf-8') as f:
            return json.load(f)
    return {
        "about": "Здесь вы можете написать краткую информацию о себе, вашем опыте и навыках.",
        "projects": {
            "Проект 1": {
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
            },
            "Проект 2": {
                "description": "Мобильное приложение на Vue.js и Node.js",
                "image": "static/images/project2.jpg",
                "url": "Project_2",
                "details": {
                    "about": "Описание проекта",
                    "features": [
                        "Особенность 1: Описание",
                        "Особенность 2: Описание",
                        "Особенность 3: Описание"
                    ],
                    "tech_stack": {
                        "frontend": ["Vue.js", "Vuex", "Tailwind CSS"],
                        "backend": ["Node.js", "Express", "MongoDB"],
                        "devops": ["Git", "Jest", "Webpack"]
                    }
                }
            },
            "Проект 3": {
                "description": "ML-проект с использованием TensorFlow",
                "image": "static/images/project3.jpg",
                "url": "Project_3",
                "details": {
                    "about": "Описание проекта",
                    "features": [
                        "Особенность 1: Описание",
                        "Особенность 2: Описание",
                        "Особенность 3: Описание"
                    ],
                    "tech_stack": {
                        "frontend": ["TensorFlow.js", "React", "D3.js"],
                        "backend": ["Python", "TensorFlow", "Flask"],
                        "devops": ["Docker", "Kubernetes", "MLflow"]
                    }
                }
            }
        },
        "contacts": {
            "email": "example@example.com",
            "linkedin": "your-linkedin",
            "github": "your-github"
        }
    }

# Загрузка данных
portfolio_data = load_portfolio_data()

# Добавление CSS для стилизации
st.markdown("""
    <style>
        .main {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        .stTitle {
            color: #00ff9d !important;
            font-size: 3rem !important;
            padding-bottom: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .stHeader {
            color: #00ff9d !important;
            padding-top: 2rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }
        div[data-testid="stHorizontalBlock"] {
            background-color: #2d2d2d;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            margin: 1rem 0;
            border: 1px solid #3d3d3d;
        }
        p {
            color: #ffffff !important;
            font-size: 1.1rem !important;
            line-height: 1.6 !important;
        }
        .contact-info {
            background-color: #3d3d3d;
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            transition: all 0.3s ease;
        }
        .contact-info:hover {
            background-color: #4d4d4d;
            transform: translateY(-5px);
        }
        /* Стили для изображения профиля */
        [data-testid="stImage"] > img {
            border-radius: 15px;
            border: 3px solid #00ff9d;
            box-shadow: 0 0 20px rgba(0, 255, 157, 0.3);
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        /* Стили для бокового меню */
        [data-testid="stSidebar"] {
            background-color: #2d2d2d;
            border-right: 1px solid #3d3d3d;
            padding: 1rem;
        }
        [data-testid="stSidebar"] .stTitle {
            font-size: 1.5rem !important;
            padding-bottom: 1rem;
        }
        /* Стили для ссылок в боковом меню */
        .css-1oe5cao {
            color: #00ff9d !important;
        }
        .css-1oe5cao:hover {
            color: #00ccff !important;
        }
    </style>
""", unsafe_allow_html=True)

# Заголовок портфолио
st.title("Портфолио Разработчика / Продакт Менеджера")

# Создаем две колонки в разделе "О себе"
col1, col2 = st.columns([1, 2])

with col1:
    # Добавление фотографии
    st.image("static/images/profile.jpg", use_column_width=True)

with col2:
    # Раздел о себе
    st.header("О себе")
    st.write(portfolio_data["about"])

# Раздел контактов
st.header("Контакты")
contact_col1, contact_col2, contact_col3 = st.columns(3)

with contact_col1:
    st.markdown(f'<div class="contact-info">📧 Email: {portfolio_data["contacts"]["email"]}</div>', unsafe_allow_html=True)
with contact_col2:
    st.markdown(f'<div class="contact-info">💼 LinkedIn: {portfolio_data["contacts"]["linkedin"]}</div>', unsafe_allow_html=True)
with contact_col3:
    st.markdown(f'<div class="contact-info">🌐 GitHub: {portfolio_data["contacts"]["github"]}</div>', unsafe_allow_html=True)

# Добавляем заголовок в боковое меню
st.sidebar.title("Навигация")

# Добавляем кнопку для перехода в админ-панель в конец бокового меню
st.sidebar.markdown("---")  # Разделитель
st.sidebar.title("Управление")
if st.sidebar.button("Редактировать портфолио ⚙️"):
    st.switch_page("pages/Admin.py")
