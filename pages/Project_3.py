import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Проект 3",
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
st.title("Проект 3: Название проекта")

# Основное изображение проекта
st.image("static/images/project3.jpg", use_column_width=True)

# Описание проекта
st.header("О проекте")
st.write("""
Здесь подробное описание третьего проекта. 
Расскажите о технических вызовах и их решениях.
""")

# Технический стек
st.header("Технический стек")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="tech-stack">🔧 ML/AI:<br>• TensorFlow<br>• PyTorch<br>• Scikit-learn</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="tech-stack">⚙️ Данные:<br>• PostgreSQL<br>• Redis<br>• Elasticsearch</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="tech-stack">🛠️ Инфраструктура:<br>• Kubernetes<br>• Terraform<br>• Prometheus</div>', unsafe_allow_html=True)

# Ключевые особенности
st.header("Ключевые особенности")
features = [
    "🤖 Особенность 1: Машинное обучение и предиктивная аналитика",
    "📊 Особенность 2: Обработка больших данных в реальном времени",
    "🔄 Особенность 3: Автоматическая масштабируемость"
]

for feature in features:
    st.markdown(f'<div class="feature">{feature}</div>', unsafe_allow_html=True)

# Результаты и метрики
st.header("Результаты")
metrics_col1, metrics_col2 = st.columns(2)

with metrics_col1:
    st.metric(label="Точность модели", value="95%", delta="↑5%")
    st.metric(label="Обработка данных", value="1M+/день", delta="↑25%")

with metrics_col2:
    st.metric(label="Экономия ресурсов", value="40%", delta="↑15%")
    st.metric(label="ROI", value="300%", delta="↑50%")

# Ссылки
st.header("Ссылки")
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="tech-stack">🔗 Документация: <a href="#" style="color: #00ff9d;">docs.project3.com</a></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="tech-stack">📦 API: <a href="#" style="color: #00ff9d;">api.project3.com</a></div>', unsafe_allow_html=True) 