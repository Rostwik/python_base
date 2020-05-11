# запуск тестов в консоли:
python -m unittest

# coverage
coverage run --source=bot,handlers,settings -m unittest
coverage report -m

#create PostgreSQL database
psql -c "create database vk_chat_bot"
psql -d vk_chat_bot
