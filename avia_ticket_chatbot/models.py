from pony.orm import Database, Required, Json

from settings import DB_CONFIG

db = Database()
db.bind(**DB_CONFIG)


class UserState(db.Entity):
    """Состояние пользователя внури сценария"""

    user_id = Required(str, unique=True)
    scenario_name = Required(str)
    step_name = Required(str)
    context = Required(Json)


class Registration(db.Entity):
    """Заявка на регистрацию"""

    phone = Required(str)
    places = Required(str)
    route = Required(str)
    comment = Required(str)
    name = Required(str)
    email = Required(str)


db.generate_mapping(create_tables=True)
