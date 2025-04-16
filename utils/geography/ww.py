import pycountry
import pytz
import pycountry_convert as pc
from datetime import datetime
from typing import List, Optional, Dict, Literal
from transformations.validation.metaclass_type_checker import TypeChecker


class WWTimezones(metaclass=TypeChecker):

    def get_timezones_by_country_code(self, country_code: str) -> Optional[List[str]]:
        country = pycountry.countries.get(alpha_2=country_code.upper())
        return pytz.country_timezones.get(country.alpha_2) if country else None

    def get_countries_in_timezone(self, timezone_name: str) -> List[str]:
        return [
            code for code, tz_list in pytz.country_timezones.items()
            if timezone_name in tz_list
        ]

    def get_current_time_in_country(self, country_code: str, int_tz: int = 0) -> Optional[str]:
        timezones = self.get_timezones_by_country_code(country_code.upper())
        if not timezones:
            return None
        tz = pytz.timezone(timezones[int_tz])
        return datetime.now(tz).isoformat(sep=" ")

    def get_country_from_timezone(self, timezone_name: str) -> List[str]:
        return self.get_countries_in_timezone(timezone_name)

    @property
    def get_all_timezones_grouped(self) -> Dict[str, List[str]]:
        return pytz.country_timezones


class WWGeography(metaclass=TypeChecker):

    def get_country_details(self, country_code: str) -> Optional[Dict[str, str]]:
        country = (
            pycountry.countries.get(alpha_2=country_code.upper())
            or pycountry.countries.get(alpha_3=country_code.upper())
        )
        if not country:
            return None
        return {
            "name": country.name,
            "alpha_2": country.alpha_2,
            "alpha_3": country.alpha_3,
            "official_name": getattr(country, "official_name", ""),
        }

    def bl_valid_country_code(self, country_code: str) -> bool:
        return bool(
            pycountry.countries.get(alpha_2=country_code.upper()) or
            pycountry.countries.get(alpha_3=country_code.upper())
        )

    def get_country_flag_emoji(self, country_code: str) -> Optional[str]:
        if self.bl_valid_country_code(country_code.upper()) == False:
            return None
        return "".join(chr(ord(c) + 127397) for c in country_code.upper())

    def get_country_details_by_name(self, name: str) -> Optional[Dict[str, str]]:
        country = pycountry.countries.search_fuzzy(name)
        if country:
            return self.get_country_details(country[0].alpha_2)
        return None

    def get_continent_by_country_code(self, country_code: str) -> Optional[str]:
        if self.bl_valid_country_code(country_code) == False:
            return None
        try:
            continent_code = pc.country_alpha2_to_continent_code(country_code.upper())
            return pc.convert_continent_code_to_continent_name(continent_code)
        except (KeyError, ValueError):
            return None

    def get_continent_code_by_country_code(self, country_code: str) \
        -> Literal["AF", "AS", "EU", "NA", "SA", "OC", "AN"]:
        if not self.bl_valid_country_code(country_code):
            return None
        try:
            return pc.country_alpha2_to_continent_code(country_code.upper()).upper()
        except (KeyError, ValueError):
            return None
