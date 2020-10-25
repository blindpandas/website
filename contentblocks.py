# coding: utf-8


from dataclasses import dataclass

@dataclass
class FeaturedApp:
    name: str
    title: str
    url: str
    logo: str
    lead_text: str


# Site metadata
HERO_TITLE = "Blind Pandas"
HERO_LEAD = "Free & open-source software for the blind and visually impaired."
FEATURED_APPS = (
    FeaturedApp(
        name="bookworm",
        title="Bookworm",
        url="/bookworm",
        logo="/static/images/bookworm128x128.png",
        lead_text="The free, open-source, and universally accessible eBook reader for Windows."
    ),
    FeaturedApp(
        name="audio-themes",
        title="Audio Themes",
        url="/audio-themes",
        logo="/static/images/audio-themes128x128.png",
        lead_text="An add-on for NVDA that creates a virtual audio display using 3D sound."
    ),
    FeaturedApp(
        name="code",
        title="Code",
        url="/code",
        logo="/static/images/code128x128.png",
        lead_text="We also provide programming libraries and utilities for others to build on and improve."
    ),
)

# Main navigation menu
MAIN_NAVIGATION_MENU = (
    ("Blog", "/blog/"),
    ("Bookworm", "/bookworm/"),
    ("Audio Themes", "/audio-themes/"),
    ("Developers", "/dev/"),
    ("About", "/about/"),
)

# Twitter embed
TWITTER_EMBED_URL = "https://twitter.com/mush42"
TWITTER_EMBED_TITLE = "Tweets by Musharraf"
TWITTER_EMBED_WIDTH = 500
TWITTER_EMBED_HEIGHT= 500

# Social links
SOCIAL_LINKS = (
    ("Twitter", "https://twitter.com/mush42/", "twitter fab"),
    ("GitHub", "https://github.com/blindpandas/", "github fab"),
    ("Users Mailing List", "https://groups.io/g/blindpandas-users", "envelope fa"),
)