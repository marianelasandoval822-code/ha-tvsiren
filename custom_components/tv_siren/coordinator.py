from homeassistant.helpers.event import async_track_state_change_event
from homeassistant.core import callback
from .const import CONF_TVS, CONF_ALARM, CONF_URL

class TvSirenCoordinator:
    def __init__(self, hass, config):
        self.hass = hass
        self.tvs = [x.strip() for x in config[CONF_TVS].split(",")]
        self.alarm = config[CONF_ALARM]
        self.url = config[CONF_URL]
        self.enabled = True

    async def async_setup(self):
        async_track_state_change_event(
            self.hass,
            [self.alarm],
            self._changed
        )

    @callback
    async def _changed(self, event):
        new_state = event.data.get("new_state")
        if not new_state:
            return

        if new_state.state == "triggered" and self.enabled:
            await self.play()

        if new_state.state == "disarmed":
            await self.stop()

    async def play(self):
        await self.hass.services.async_call(
            "media_player", "turn_on",
            {"entity_id": self.tvs}
        )

        await self.hass.services.async_call(
            "media_player", "volume_set",
            {"entity_id": self.tvs, "volume_level": 1.0}
        )

        await self.hass.services.async_call(
            "media_player", "play_media",
            {
                "entity_id": self.tvs,
                "media_content_id": self.url,
                "media_content_type": "video/mp4",
            }
        )

    async def stop(self):
        await self.hass.services.async_call(
            "media_player", "turn_off",
            {"entity_id": self.tvs}
        )