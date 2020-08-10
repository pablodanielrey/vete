import inject
import inject
from vete.config import configure
inject.configure(configure)

from .db import Sessions
sessions = inject.instance(Sessions)
sessions.generate_database()
