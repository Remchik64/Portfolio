from PIL import Image, ImageDraw, ImageFont
import os

# Создаем директорию, если она не существует
os.makedirs('static/images', exist_ok=True)

# Создаем изображение профиля
profile_img = Image.new('RGB', (400, 400), color='#2d2d2d')
profile_draw = ImageDraw.Draw(profile_img)
profile_draw.text((120, 180), 'PROFILE\nPHOTO', fill='#00ff9d', align='center')
profile_draw.rectangle([50, 50, 350, 350], outline='#00ff9d', width=2)
profile_img.save('static/images/profile.jpg')

# Создаем изображения проектов
for i in range(1, 4):
    project_img = Image.new('RGB', (800, 450), color='#2d2d2d')
    project_draw = ImageDraw.Draw(project_img)
    project_draw.text((350, 200), f'PROJECT {i}', fill='#00ccff', align='center')
    project_draw.rectangle([50, 50, 750, 400], outline='#00ccff', width=2)
    project_img.save(f'static/images/project{i}.jpg')

print("Изображения успешно созданы в папке static/images/") 