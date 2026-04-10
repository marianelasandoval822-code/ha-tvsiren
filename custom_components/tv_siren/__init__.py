from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN
from .coordinator import TvSirenCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data.setdefault(DOMAIN, {})

    coord = TvSirenCoordinator(hass, entry.data)
    await coord.async_setup()

    hass.data[DOMAIN][entry.entry_id] = coord

    await hass.config_entries.async_forward_entry_setups(entry, ["switch", "button"])
    return True