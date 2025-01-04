import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Проект 1",
    page_icon="🚀",
    layout="wide"
)

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
        }
        .feature:hover {
            transform: translateY(-5px);
        }
    </style>
""", unsafe_allow_html=True)

# Заголовок проекта
st.title("Проект 1: Название проекта")

# Основное изображение проекта
st.image("static/images/project1.jpg", use_column_width=True)

# Описание проекта
st.header("О проекте")
st.write("""
Здесь подробное описание проекта, его цели и задачи. 
Расскажите о проблеме, которую решает проект, и почему это важно.
""")

# Технический стек
st.header("Технический стек")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="tech-stack">🔧 Frontend:<br>• React<br>• TypeScript<br>• Material-UI</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="tech-stack">⚙️ Backend:<br>• Python<br>• FastAPI<br>• PostgreSQL</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="tech-stack">🛠️ DevOps:<br>• Docker<br>• AWS<br>• CI/CD</div>', unsafe_allow_html=True)

# Ключевые особенности
st.header("Ключевые особенности")
features = [
    "🎯 Особенность 1: Описание первой ключевой особенности проекта",
    "⚡ Особенность 2: Описание второй ключевой особенности",
    "🎨 Особенность 3: Описание третьей ключевой особенности"
]

for feature in features:
    st.markdown(f'<div class="feature">{feature}</div>', unsafe_allow_html=True)

# Результаты и метрики
st.header("Результаты")
metrics_col1, metrics_col2 = st.columns(2)

with metrics_col1:
    st.metric(label="Пользователи", value="10K+", delta="↑15%")
    st.metric(label="Время отклика", value="0.5s", delta="-20%")

with metrics_col2:
    st.metric(label="Конверсия", value="25%", delta="↑10%")
    st.metric(label="Надежность", value="99.9%", delta="↑5%")

# Ссылки
st.header("Ссылки")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="tech-stack">🔗 Демо: <a href="#" style="color: #00ff9d;">demo.project.com</a></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="tech-stack">📦 GitHub: <a href="#" style="color: #00ff9d;">github.com/project</a></div>', unsafe_allow_html=True) 