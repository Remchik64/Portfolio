import streamlit as st
import json
import os

# Настройка страницы
st.set_page_config(
    page_title="Проект 2",
    page_icon="🚀",
    layout="wide"
)

# Стили
st.markdown("""
    <style>
        /* Скрываем предупреждения */
        .stDeployButton {display:none;}
        .viewerBadge_container__1QSob {display:none;}
        div[data-testid="stDecoration"] {display:none;}
        div[data-baseweb="notification"] {display:none;}
        div[class="stAlert"] {display:none;}
        
        /* Мягкие неоновые рамки для изображений */
        .element-container img {
            border-radius: 5px;
            box-shadow: 0 0 5px #4d94ff,
                       0 0 10px #4d94ff;
            margin: 10px 0;
            transition: all 0.3s ease;
        }
        
        .element-container img:hover {
            box-shadow: 0 0 8px #4d94ff,
                       0 0 15px #4d94ff;
        }
    </style>
""", unsafe_allow_html=True)

# Функция для безопасной загрузки изображения
def safe_load_image(image_path, default_content=None):
    try:
        if os.path.exists(image_path):
            return open(image_path, 'rb').read()
        return default_content
    except:
        return default_content

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
}

# Получаем данные проекта с обработкой ошибок
try:
    project_data = portfolio_data.get("projects", {}).get("Проект 2", default_project)
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
        .carousel-container {
            position: relative;
            width: 100%;
            margin: 2rem 0;
        }
        .carousel-nav {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 1rem;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }
        .carousel-nav:hover {
            background: rgba(0, 0, 0, 0.9);
        }
        .carousel-prev {
            left: 1rem;
        }
        .carousel-next {
            right: 1rem;
        }
        .carousel-indicator {
            text-align: center;
            margin-top: 1rem;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Заголовок проекта
st.title(f"Проект 2: {project_data['description']}")

# Карусель изображений
st.markdown('<div class="carousel-container">', unsafe_allow_html=True)

# Получаем список изображений
images = project_data.get("images", [project_data["image"]])

# Проверяем и корректируем индекс, если он выходит за пределы
if 'current_image_index' not in st.session_state or st.session_state.current_image_index >= len(images):
    st.session_state.current_image_index = 0

# Кнопки навигации
col1, col2, col3 = st.columns([1, 10, 1])

with col1:
    if st.button("◀", key="prev") and len(images) > 1:
        st.session_state.current_image_index = (st.session_state.current_image_index - 1) % len(images)

with col2:
    # Показываем текущее изображение
    current_image = images[st.session_state.current_image_index]
    image_content = safe_load_image(current_image)
    if image_content:
        st.image(image_content, use_container_width=True)
    else:
        st.info("Изображение недоступно")
    
    # Индикатор изображений
    if len(images) > 1:
        st.markdown(
            f'<div class="carousel-indicator">{st.session_state.current_image_index + 1} / {len(images)}</div>',
            unsafe_allow_html=True
        )

with col3:
    if st.button("▶", key="next") and len(images) > 1:
        st.session_state.current_image_index = (st.session_state.current_image_index + 1) % len(images)

st.markdown('</div>', unsafe_allow_html=True)

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

# Описание проекта
st.header("О проекте")
st.write(project_data["details"]["about"])

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