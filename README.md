# Ha TVSiren

Turn your TVs into a siren system using Home Assistant.

This integration supports the following TVs/devices:
<img width="200" height="200" alt="image" src="https://i.postimg.cc/bYZgLYzL/81Os-Em-GZ1d-L.jpg" /> <img width="200" height="200" alt="image" src="https://i.postimg.cc/pddzTkrg/1cf728b4-7764-4e94-993f-8c18902d998a.webp" />
<img width="200" height="200" alt="image" src="https://i.postimg.cc/br12MBVP/chromecast-4k-pagweb7.png" />


> [!WARNING]
> *  Apple TV is not supported and will never be supported, don't bother creating an issue about when the Apple TV is gonna be supported.
> *  Roku TV devices have not been tested
> *  Other TVs may have limited support depending on media playback capabilities


> [!NOTE]
> This integration is currently in prerelease. Features may change, and bugs may be present.

---

## Features

* Play a siren video on multiple TVs
* Trigger automatically from an alarm panel
* Enable/disable toggle
* Manual test button
* Upload a siren file directly (auto-saved to `/www`)
* Automatic max volume on trigger

---

## How It Works

When your alarm panel enters the **triggered** state, Ha TVSiren will:

1. Turn on selected TVs
2. Set volume to maximum
3. Play the configured siren video

When the alarm is disarmed, TVs will turn off automatically.

---

## Installation (HACS)

1. Open HACS
2. Go to **Integrations**
3. Click the ⋮ menu → **Custom repositories**
4. Add your repository URL
5. Select category: **Integration**
6. Install **Ha TVSiren**
7. Restart Home Assistant

---

## Configuration
> [!IMPORTANT]
> HACS doesn't set up the integration for you. You have to do it manually.
> After installation:
> 1. Go to **Settings → Devices & Services**
> 2. Click **Add Integration**
> 3. Search for **Ha TVSiren**

### You will be asked to:

* Select TVs (`media_player` entities)
* Select an alarm panel
* Provide a siren video (since HA doesn't support moving files):

  * Upload file (recommended)
  * OR enter a direct URL

---

## Siren File

If you upload a file, it will be saved to:

/config/www/tv_siren/siren.mp4

Accessible as:

/local/tv_siren/siren.mp4

---

## Supported Devices

Works best with:

* Chromecast
* Android TV
* Fire TV

---

## Entities Created

* Switch → Enable/disable TV siren
* Button → Manually trigger siren

---

## Notes

* TVs must support remote media playback
* Video must be in a supported format (MP4 recommended)
* Network access to Home Assistant is required

---

## Future Plans

* UI entity selectors (no manual typing)
* Per-TV volume control
* Resume previous media after alarm
* Multiple siren profiles

---

## Contributing

Pull requests and suggestions are welcome.

---

## License
Apache License

---

## Support

If you like this project, consider starring the repository.
