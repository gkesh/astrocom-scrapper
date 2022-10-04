from api import db
from logger.workers import warn


NAME = "API_MODELS"

class ReusableDocument():
    @classmethod
    def get_or_create(cls, **props):
        """
        Get or Create

        Common functionality among some models
        where it is used by comic and may be shared
        among multiple, hence it is checked first
        if it is already created before saving
        """
        try:
            obj = cls.objects.get(**props)
        except Exception:
            warn(NAME, f"{cls.__name__} not found, creating...")
            obj = cls(**props)
        obj.save()
        return obj
