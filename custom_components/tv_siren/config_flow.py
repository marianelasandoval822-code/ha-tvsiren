import voluptuous as vol
import base64
import os
from homeassistant import config_entries
from .const import DOMAIN, CONF_TVS, CONF_ALARM, CONF_URL, CONF_FILE

class TvSirenConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        if user_input is not None:

            file_data = user_input.get(CONF_FILE)
            url = user_input.get(CONF_URL)

            if file_data:
                raw = base64.b64decode(file_data)

                path = self.hass.config.path("www/tv_siren/siren.mp4")
                os.makedirs(os.path.dirname(path), exist_ok=True)

                with open(path, "wb") as f:
                    f.write(raw)

                url = "/local/tv_siren/siren.mp4"

            user_input[CONF_URL] = url
            user_input.pop(CONF_FILE, None)

            return self.async_create_entry(title="Ha TVSiren", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_TVS): str,
                vol.Required(CONF_ALARM): str,
                vol.Optional(CONF_URL): str,
                vol.Optional(CONF_FILE): str,
            }),
        )