from pathlib import Path

from . import Singleton
from django.conf import settings

from ..models import Mod


class ServerService(metaclass=Singleton):
    def __init__(self):
        self._path = settings.SERVER_PATH
        self._available = ...
        self._has_mods = ...

        if self._path is None:
            self._available = False
            return
        else:
            self._available = True

        mods_dir: Path = self._path / 'mods'
        if not mods_dir.exists():
            self._has_mods = False
            return
        else:
            self._has_mods = True

    @property
    def available(self):
        return self._available

    @property
    def has_mods(self):
        return self._has_mods

    @property
    def enabled_mods(self):
        return Mod.objects.filter(active=True)

    @property
    def disabled_mods(self):
        return Mod.objects.filter(active=False)

    @property
    def running(self) -> bool:
        # Necesita implementación adicional en el servidor.
        return False

    @property
    def last_log(self) -> str:
        return '¡No se ha encontrado ningún log!'
