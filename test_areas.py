# A simple test script to add a new area to test.metabrainz.org

from musicbrainz_bot.editing import MusicBrainzClient
import musicbrainz_bot.config as cfg
import mechanize


mb = MusicBrainzClient(cfg.MB_USERNAME, cfg.MB_PASSWORD, cfg.MB_SITE)

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.set_debug_redirects(False)
browser.set_debug_http(False)

EXT_LINK_TYPE_ID = "358"  # Hard coded to type id "358" i.e. Wikidata

area_template = {
    "name": None,
    "disambiguation": None,
    "type": None,
    "iso_3166_1": None,
    "iso_3166_2": None,
    "iso_3166_3": None,
    "external_links": {
        "text": [],
        "type": [],
    },
}

area = {
    "name": "test_area_name_type_note_iso_list_ext_link_list with updated method",
    "disambiguation": "disambiguation_test",
    "type": "3",
    "iso_3166_1": None,
    "iso_3166_2": ["ES-X"],
    "iso_3166_3": ["XXAI", "XXAJ"],
    "url": [
        {
            "text": "https://www.wikidata.org/wiki/Q152",
            "link_type_id": EXT_LINK_TYPE_ID,
        },
        {
            "text": "https://www.wikidata.org/wiki/Q1494",
            "link_type_id": EXT_LINK_TYPE_ID,
        },
    ],
    "something": None,
}

edit_note = "Tests new area with name, type, disambiguation, edit note."

area_mbid = mb.add_area(area, edit_note=edit_note)
print(area_mbid)
print("area MBID: " + area_mbid)
print("Link: https://test.musicbrainz.org/area/" + area_mbid)
