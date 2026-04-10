from homeassistant.components.button import ButtonEntity

async def async_setup_entry(hass, entry, async_add_entities):
    from .coordinator import TvSirenCoordinator

    coord = hass.data["tv_siren"][entry.entry_id]
    async_add_entities([TvSirenButton(coord)])

class TvSirenButton(ButtonEntity):
    def __init__(self, coord):
        self.coord = coord
        self._attr_name = "Test Ha TVSiren"

    async def async_press(self):
        await self.coord.play()