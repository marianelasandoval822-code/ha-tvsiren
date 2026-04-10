from homeassistant.components.switch import SwitchEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coord = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([TvSirenSwitch(coord)])

class TvSirenSwitch(SwitchEntity):
    def __init__(self, coord):
        self.coord = coord
        self._attr_name = "Ha TVSiren Enabled"

    @property
    def is_on(self):
        return self.coord.enabled

    async def async_turn_on(self):
        self.coord.enabled = True

    async def async_turn_off(self):
        self.coord.enabled = False
        await self.coord.stop()