## Описание

Выполнено тестовое задание и **бонусы**:

- Запуск используя Docker
- Использование environment variables
- Просмотр Django Моделей в Django Admin панели
- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
- Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте


## Запуск проекта

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Reancoree/reeshat-test.git
cd project
```
2. Установите зависимости
```bash
pip install -r requirements.txt
```
3. Настройте переменные окружения в .env:
```python
STRIPE_PUBLIC_KEY=your_public_key
STRIPE_SECRET_KEY=your_secret_key
```
4. Запустите с docker:

Укажите переменные в docker-compose.yml

Запустите
```bash
docker-compose up --build
```
5. Перейдите на http://localhost:8000/item/1/ для тестирования

**Проверка решения**: 
- Создайте объекты `Item` через админку.
- Откройте страницу товара, нажмите "Buy" для перехода к оплате.
- Убедитесь, что Stripe Checkout открывается корректно.