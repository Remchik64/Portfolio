import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Проект 2",
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
st.title("Проект 2: Название проекта")

# Основное изображение проекта
st.image("static/images/project2.jpg", use_column_width=True)

# Описание проекта
st.header("О проекте")
st.write("""
Здесь подробное описание второго проекта. 
Опишите уникальные особенности и преимущества вашего решения.
""")

# Технический стек
st.header("Технический стек")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="tech-stack">🔧 Frontend:<br>• Vue.js<br>• Vuex<br>• Tailwind CSS</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="tech-stack">⚙️ Backend:<br>• Node.js<br>• Express<br>• MongoDB</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="tech-stack">🛠️ Инструменты:<br>• Git<br>• Jest<br>• Webpack</div>', unsafe_allow_html=True)

# Ключевые особенности
st.header("Ключевые особенности")
features = [
    "📱 Особенность 1: Адаптивный дизайн и кроссплатформенность",
    "🔒 Особенность 2: Безопасность и шифрование данных",
    "⚡ Особенность 3: Высокая производительность"
]

for feature in features:
    st.markdown(f'<div class="feature">{feature}</div>', unsafe_allow_html=True)

# Результаты и метрики
st.header("Результаты")
metrics_col1, metrics_col2 = st.columns(2)

with metrics_col1:
    st.metric(label="Скорость загрузки", value="1.2s", delta="-30%")
    st.metric(label="Активные пользователи", value="5K+", delta="↑20%")

with metrics_col2:
    st.metric(label="Рейтинг", value="4.8/5", delta="↑0.3")
    st.metric(label="Доступность", value="99.5%", delta="↑3%")

# Ссылки
st.header("Ссылки")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="tech-stack">🔗 Демо: <a href="#" style="color: #00ff9d;">project2-demo.com</a></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="tech-stack">📦 GitHub: <a href="#" style="color: #00ff9d;">github.com/project2</a></div>', unsafe_allow_html=True) 