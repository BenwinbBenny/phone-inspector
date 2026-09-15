from dataclasses import dataclass
from typing import Optional

import phonenumbers
from phonenumbers import carrier, geocoder, timezone


@dataclass
class PhoneInfo:
    """Information obtained from a phone number."""

    formatted_number: str
    country_code: int
    national_number: int
    region: Optional[str]
    carrier: str
    location: str
    timezones: tuple[str, ...]
    is_valid: bool
    is_possible: bool


class PhoneAnalyzer:
    """Analyze phone numbers using Google's libphonenumber database."""

    def inspect(self, value: str) -> PhoneInfo:
        """
        Parse and inspect a phone number.

        Args:
            value: Phone number including its international country code.

        Returns:
            PhoneInfo containing available metadata.

        Raises:
            ValueError: If the supplied value cannot be parsed.
        """

        cleaned = value.strip()

        if not cleaned:
            raise ValueError("Please enter a phone number.")

        try:
            parsed = phonenumbers.parse(cleaned, None)
        except phonenumbers.NumberParseException as exc:
            raise ValueError(
                "The phone number could not be parsed. "
                "Use international format, for example: +919876543210"
            ) from exc

        valid = phonenumbers.is_valid_number(parsed)
        possible = phonenumbers.is_possible_number(parsed)

        region = phonenumbers.region_code_for_number(parsed)

        carrier_name = carrier.name_for_number(
            parsed,
            "en",
        )

        location = geocoder.description_for_number(
            parsed,
            "en",
        )

        zones = timezone.time_zones_for_number(parsed)

        return PhoneInfo(
            formatted_number=phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL,
            ),
            country_code=parsed.country_code,
            national_number=parsed.national_number,
            region=region or "Unknown",
            carrier=carrier_name or "Unknown",
            location=location or "Unknown",
            timezones=tuple(zones),
            is_valid=valid,
            is_possible=possible,
        )