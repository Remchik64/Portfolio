import streamlit as st
import json
import os
from PIL import Image
import io

# Настройка страницы
st.set_page_config(page_title="Админ панель", page_icon="⚙️", layout="wide")

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

# Остальной код админ-панели... 