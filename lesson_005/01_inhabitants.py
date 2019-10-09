# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import lesson_005.room_1 as room_1
import lesson_005.room_2 as room_2

# Подскажите, пожалуйста, почему, room подчеркнуто красным.


print('В комнате room_1 живут:', ', '.join(room_1.folks))
print('В комнате room_2 живут:', ', '.join(room_2.folks))

#зачет!