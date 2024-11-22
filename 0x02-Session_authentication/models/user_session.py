#!/usr/bin/env python3
"""
User session module
"""
from models.base import Base


class UserSession(Base):
    """ session object representing user session info
    """
    def _init_(self, *args: list, **kwargs: dict):
        """ Initialize UserSession instance
        """
        super()._init_(*args, **kwargs)
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id", self.id)
