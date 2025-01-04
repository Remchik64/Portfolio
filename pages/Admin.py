import streamlit as st
import json
import os
from PIL import Image
import shutil

# Настройка страницы
st.set_page_config(
    page_title="Управление портфолио",
    page_icon="⚙️",
    layout="wide"
)

def resize_image_with_aspect_ratio(image, target_size):
    """
    Изменяет размер изображения с сохранением пропорций.
    Добавляет белые поля, если необходимо.
    """
    # Получаем текущие размеры
    width, height = image.size
    aspect = width / height

    # Вычисляем новые размеры с сохранением пропорций
    target_width, target_height = target_size
    target_aspect = target_width / target_height

    if aspect > target_aspect:
        # Изображение шире целевого
        new_width = target_width
        new_height = int(new_width / aspect)
    else:
        # Изображение выше целевого
        new_height = target_height
        new_width = int(new_height * aspect)

    # Изменяем размер с сохранением пропорций
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Создаем новое изображение с целевыми размерами
    new_image = Image.new('RGB', target_size, (45, 45, 45))  # Тёмно-серый фон
    
    # Вычисляем позицию для центрирования
    left = (target_width - new_width) // 2
    top = (target_height - new_height) // 2
    
    # Вставляем изображение по центру
    new_image.paste(image, (left, top))
    
    return new_image

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

# Функция для сохранения данных
def save_portfolio_data(data):
    os.makedirs("data", exist_ok=True)
    with open("data/portfolio_data.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    st.success("Данные успешно сохранены!")

# Загрузка текущих данных
portfolio_data = load_portfolio_data()

# Заголовок
st.title("Управление портфолио")

# Вкладки для разных разделов
tab1, tab2, tab3 = st.tabs(["О себе", "Проекты", "Контакты"])

with tab1:
    st.header("Редактирование раздела 'О себе'")
    about_text = st.text_area("О себе", portfolio_data["about"], height=200)
    profile_image = st.file_uploader("Загрузить фото профиля", type=['jpg', 'png', 'jpeg'])
    
    if profile_image:
        os.makedirs("static/images", exist_ok=True)
        with Image.open(profile_image) as img:
            # Конвертируем в RGB если изображение в другом формате
            if img.mode != 'RGB':
                img = img.convert('RGB')
            # Изменяем размер с сохранением пропорций
            img = resize_image_with_aspect_ratio(img, (400, 400))
            img.save("static/images/profile.jpg", quality=95)
        st.image(profile_image, caption="Новое фото профиля", width=200)

with tab2:
    st.header("Управление проектами")
    
    # Выбор проекта для редактирования
    project_names = list(portfolio_data["projects"].keys())
    selected_project = st.selectbox("Выберите проект для редактирования", project_names)
    
    # Добавление нового проекта
    if st.button("Добавить новый проект"):
        new_project_name = f"Проект {len(project_names) + 1}"
        portfolio_data["projects"][new_project_name] = {
            "description": "Описание нового проекта",
            "image": "static/images/project1.jpg",
            "url": f"Project_{len(project_names) + 1}",
            "details": {
                "about": "Описание проекта",
                "features": ["Особенность 1", "Особенность 2", "Особенность 3"],
                "tech_stack": {
                    "frontend": [],
                    "backend": [],
                    "devops": []
                }
            }
        }
        st.experimental_rerun()
    
    if selected_project:
        project = portfolio_data["projects"][selected_project]
        
        # Редактирование описания
        project["description"] = st.text_area(
            "Краткое описание проекта",
            project["description"]
        )
        
        # Загрузка изображения проекта
        project_image = st.file_uploader(
            f"Изображение для {selected_project}",
            type=['jpg', 'png', 'jpeg'],
            key=f"project_image_{selected_project}"
        )
        
        if project_image:
            os.makedirs("static/images", exist_ok=True)
            with Image.open(project_image) as img:
                # Конвертируем в RGB если изображение в другом формате
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                # Изменяем размер с сохранением пропорций
                img = resize_image_with_aspect_ratio(img, (800, 450))
                img.save(f"static/images/project{selected_project[-1]}.jpg", quality=95)
            st.image(project_image, caption=f"Изображение для {selected_project}", width=400)
        
        # Редактирование деталей проекта
        st.subheader("Детали проекта")
        project["details"]["about"] = st.text_area(
            "Подробное описание",
            project["details"]["about"]
        )
        
        # Редактирование особенностей
        st.subheader("Особенности проекта")
        for i, feature in enumerate(project["details"]["features"]):
            project["details"]["features"][i] = st.text_input(
                f"Особенность {i+1}",
                feature
            )
        
        # Редактирование технического стека
        st.subheader("Технический стек")
        for category in ["frontend", "backend", "devops"]:
            st.write(f"**{category.title()}**")
            tech_stack = st.text_input(
                f"Технологии {category} (через запятую)",
                ", ".join(project["details"]["tech_stack"][category])
            )
            project["details"]["tech_stack"][category] = [
                tech.strip() for tech in tech_stack.split(",") if tech.strip()
            ]

with tab3:
    st.header("Редактирование контактов")
    portfolio_data["contacts"]["email"] = st.text_input("Email", portfolio_data["contacts"]["email"])
    portfolio_data["contacts"]["linkedin"] = st.text_input("LinkedIn", portfolio_data["contacts"]["linkedin"])
    portfolio_data["contacts"]["github"] = st.text_input("GitHub", portfolio_data["contacts"]["github"])

# Кнопка сохранения
if st.button("Сохранить все изменения", type="primary"):
    try:
        # Обновляем данные
        portfolio_data["about"] = about_text
        
        # Создаем директории, если они не существуют
        os.makedirs("data", exist_ok=True)
        os.makedirs("static/images", exist_ok=True)
        
        # Сохраняем данные в JSON
        with open("data/portfolio_data.json", "w", encoding='utf-8') as f:
            json.dump(portfolio_data, f, ensure_ascii=False, indent=4)
        
        # Показываем сообщение об успехе
        st.success("✅ Данные успешно сохранены!")
        
        # Добавляем кнопку для возврата на главную страницу
        if st.button("Вернуться на главную"):
            st.switch_page("portfolio.py")
            
    except Exception as e:
        st.error(f"❌ Ошибка при сохранении данных: {str(e)}")
        st.info("ℹ️ Пожалуйста, проверьте права доступа к файлам и попробуйте снова.") 