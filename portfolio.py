import streamlit as st

# Настройка конфигурации страницы
st.set_page_config(
    page_title="Моё Портфолио",
    page_icon="🚀",
    layout="wide"
)

# Добавление CSS для стилизации
st.markdown("""
    <style>
        /* Основной фон страницы */
        .main {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        
        /* Стили для заголовков */
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
        
        .stSubheader {
            color: #00ccff !important;
            margin-bottom: 1rem;
        }
        
        /* Стили для блоков */
        div[data-testid="stHorizontalBlock"] {
            background-color: #2d2d2d;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            margin: 1rem 0;
            border: 1px solid #3d3d3d;
        }
        
        /* Стили для текста */
        p {
            color: #ffffff !important;
            font-size: 1.1rem !important;
            line-height: 1.6 !important;
        }
        
        /* Стили для списков */
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        li {
            color: #ffffff !important;
            margin-bottom: 0.5rem;
            padding: 0.5rem;
            background-color: #3d3d3d;
            border-radius: 5px;
            transition: all 0.3s ease;
        }
        
        li:hover {
            background-color: #4d4d4d;
            transform: translateX(10px);
        }
        
        /* Стили для изображений */
        img {
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease;
        }
        
        img:hover {
            transform: scale(1.02);
        }
        
        /* Стили для контактов */
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
    </style>
""", unsafe_allow_html=True)

# Заголовок портфолио
st.title("Портфолио Разработчика / Продакт Менеджера")

# Создаем две колонки в разделе "О себе"
col1, col2 = st.columns([1, 2])

with col1:
    # Добавление фотографии
    st.image("static/images/profile.jpg", caption="Ваше имя", use_column_width=True)

with col2:
    # Раздел о себе
    st.header("О себе")
    st.write("""
    Здесь вы можете написать краткую информацию о себе, вашем опыте и навыках.
    Расскажите свою историю, что вас мотивирует и какие у вас цели.
    """)

# Раздел проектов
st.header("Проекты")
# Создаем сетку для проектов
proj_col1, proj_col2, proj_col3 = st.columns(3)

projects = {
    "Проект 1": {
        "description": "Веб-приложение с использованием React и FastAPI",
        "image": "static/images/project1.jpg",
        "url": "Project_1"
    },
    "Проект 2": {
        "description": "Мобильное приложение на Vue.js и Node.js",
        "image": "static/images/project2.jpg",
        "url": "Project_2"
    },
    "Проект 3": {
        "description": "ML-проект с использованием TensorFlow и Kubernetes",
        "image": "static/images/project3.jpg",
        "url": "Project_3"
    }
}

for (proj_col, (project, details)) in zip([proj_col1, proj_col2, proj_col3], projects.items()):
    with proj_col:
        st.subheader(project)
        st.image(details["image"], use_column_width=True)
        st.write(details["description"])
        if st.button("Подробнее 🔍", key=f"btn_{details['url']}"):
            st.switch_page(f"pages/{details['url']}.py")

# Раздел навыков
st.header("Навыки")
skill_col1, skill_col2 = st.columns(2)

with skill_col1:
    st.subheader("Технические навыки")
    tech_skills = ["Python", "JavaScript", "React", "SQL"]
    for skill in tech_skills:
        st.write(f"• {skill}")

with skill_col2:
    st.subheader("Soft skills")
    soft_skills = ["Управление проектами", "Анализ данных", "Коммуникация", "Лидерство"]
    for skill in soft_skills:
        st.write(f"• {skill}")

# Раздел контактов
st.header("Контакты")
contact_col1, contact_col2, contact_col3 = st.columns(3)

with contact_col1:
    st.markdown('<div class="contact-info">📧 Email: example@example.com</div>', unsafe_allow_html=True)
with contact_col2:
    st.markdown('<div class="contact-info">💼 LinkedIn: your-linkedin</div>', unsafe_allow_html=True)
with contact_col3:
    st.markdown('<div class="contact-info">🌐 GitHub: your-github</div>', unsafe_allow_html=True)
