import streamlit as st
import json
import os
from PIL import Image
import shutil
import time

# Настройка страницы
st.set_page_config(
    page_title="Админ панель",
    page_icon="⚙️",
    layout="wide"
)

# Функция проверки пароля
def check_password():
    """Возвращает `True` если пароль корректный."""
    def password_entered():
        """Проверяет введенный пароль."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Удаляем пароль из session_state
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # Первый запуск, показываем форму ввода
        st.text_input(
            "Пожалуйста, введите пароль для доступа к админ-панели", 
            type="password",
            on_change=password_entered,
            key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Пароль неверный, показываем форму снова
        st.text_input(
            "Пожалуйста, введите пароль для доступа к админ-панели", 
            type="password",
            on_change=password_entered,
            key="password"
        )
        st.error("😕 Пароль неверный")
        return False
    else:
        # Пароль верный
        return True

# Проверяем пароль перед показом контента
if not check_password():
    st.stop()  # Не показываем остальной контент

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
            "github": "your-github",
            "resume": "https://hh.ru/resume/your-resume"
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
            if img.mode != 'RGB':
                img = img.convert('RGB')
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
        st.rerun()
    
    if selected_project:
        project = portfolio_data["projects"][selected_project]
        
        # Редактирование описания
        project["description"] = st.text_area(
            "Краткое описание проекта",
            project["description"]
        )
        
        # Добавляем поля для ссылок
        st.subheader("Ссылки на проект")
        if "links" not in project:
            project["links"] = {
                "github": "",
                "website": ""
            }
        
        project["links"]["github"] = st.text_input(
            "Ссылка на GitHub",
            project["links"].get("github", ""),
            placeholder="https://github.com/username/repository"
        )
        
        project["links"]["website"] = st.text_input(
            "Ссылка на сайт проекта",
            project["links"].get("website", ""),
            placeholder="https://example.com"
        )
        
        # Загрузка изображений проекта
        st.subheader("Изображения проекта")
        
        # Инициализируем список изображений, если его нет
        if "images" not in project:
            project["images"] = [project.get("image", "static/images/project1.jpg")]
        
        # Инициализируем состояние для управления изображениями
        if "images_to_remove" not in st.session_state:
            st.session_state.images_to_remove = []
        
        # Показываем текущие изображения
        st.write("Текущие изображения проекта:")
        cols = st.columns(3)
        
        for idx, img_path in enumerate(project["images"]):
            if os.path.exists(img_path):
                with cols[idx % 3]:
                    st.image(img_path, width=200)
                    if st.button(f"🗑️ Удалить", key=f"delete_img_{selected_project}_{idx}"):
                        st.session_state.images_to_remove.append(idx)
                        st.rerun()
        
        # Удаляем отмеченные изображения
        if st.session_state.images_to_remove:
            for idx in reversed(sorted(st.session_state.images_to_remove)):
                if idx < len(project["images"]):
                    # Удаляем файл, если он существует
                    img_path = project["images"][idx]
                    if os.path.exists(img_path):
                        try:
                            os.remove(img_path)
                        except:
                            pass
                    project["images"].pop(idx)
            st.session_state.images_to_remove = []
        
        # Загрузка нового изображения
        new_image = st.file_uploader(
            "Добавить новое изображение",
            type=['jpg', 'png', 'jpeg'],
            key=f"project_images_{selected_project}"
        )
        
        if new_image:
            try:
                os.makedirs("static/images", exist_ok=True)
                # Генерируем уникальное имя файла
                timestamp = int(time.time())
                image_path = f"static/images/project{selected_project[-1]}_{timestamp}.jpg"
                
                with Image.open(new_image) as img:
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    img = resize_image_with_aspect_ratio(img, (800, 450))
                    img.save(image_path, quality=95)
                
                # Добавляем новое изображение в список
                project["images"].append(image_path)
                st.success("✅ Изображение успешно добавлено!")
            except Exception as e:
                st.error(f"Ошибка при загрузке изображения: {str(e)}")
        
        # Для совместимости со старым кодом
        project["image"] = project["images"][0] if project["images"] else "static/images/project1.jpg"

        # Редактирование деталей проекта
        st.subheader("Детали проекта")
        project["details"]["about"] = st.text_area(
            "Подробное описание",
            project["details"]["about"]
        )
        
        # Редактирование особенностей
        st.subheader("Особенности проекта")
        
        # Кнопка для добавления новой особенности
        if st.button("➕ Добавить особенность"):
            project["details"]["features"].append("Новая особенность: Описание")
            st.rerun()
        
        # Отображаем каждую особенность с возможностью удаления
        features_to_remove = []
        for i, feature in enumerate(project["details"]["features"]):
            col1, col2 = st.columns([8, 1])
            with col1:
                project["details"]["features"][i] = st.text_input(
                    f"Особенность {i+1}",
                    feature,
                    key=f"feature_{selected_project}_{i}"
                )
            with col2:
                if st.button("🗑️", key=f"delete_{selected_project}_{i}"):
                    features_to_remove.append(i)
        
        # Удаляем отмеченные особенности
        if features_to_remove:
            for index in reversed(features_to_remove):
                project["details"]["features"].pop(index)
            st.rerun()
        
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
    
    # Email с проверкой формата
    portfolio_data["contacts"]["email"] = st.text_input(
        "Email",
        portfolio_data["contacts"]["email"],
        placeholder="example@example.com"
    )
    
    # GitHub с добавлением префикса
    github_username = portfolio_data["contacts"]["github"].replace("https://github.com/", "")
    github_username = st.text_input(
        "GitHub username",
        github_username,
        placeholder="username"
    )
    portfolio_data["contacts"]["github"] = f"https://github.com/{github_username}" if github_username else ""
    
    # LinkedIn с добавлением префикса
    linkedin_username = portfolio_data["contacts"]["linkedin"].replace("https://linkedin.com/in/", "")
    linkedin_username = st.text_input(
        "LinkedIn username",
        linkedin_username,
        placeholder="username"
    )
    portfolio_data["contacts"]["linkedin"] = f"https://linkedin.com/in/{linkedin_username}" if linkedin_username else ""
    
    # Ссылка на резюме
    portfolio_data["contacts"]["project"] = st.text_input(
        "Ссылка на проект",
        portfolio_data["contacts"].get("project", ""),
        placeholder="https://example.com/your-project"
    )

# Кнопка сохранения
if st.button("Сохранить все изменения", type="primary"):
    try:
        # Обновляем данные
        portfolio_data["about"] = about_text
        
        # Создаем директории, если они не существуют
        os.makedirs("data", exist_ok=True)
        os.makedirs("static/images", exist_ok=True)
        
        # Сохраняем данные в JSON
        save_portfolio_data(portfolio_data)
        
        # Показываем сообщение об успехе
        st.success("✅ Данные успешно сохранены!")
        
    except Exception as e:
        st.error(f"❌ Ошибка при сохранении данных: {str(e)}")
        st.info("ℹ️ Пожалуйста, проверьте права доступа к файлам и попробуйте снова.")

# Кнопка возврата на главную
if st.button("← Вернуться на главную"):
    st.switch_page("portfolio.py") 