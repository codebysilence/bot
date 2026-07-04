from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base


class Verse(Base):

    __tablename__ = "verses"

    uuid: Mapped[str] = mapped_column(
        String(64),
        primary_key=True,
    )

    surah_name: Mapped[str]

    surah_number: Mapped[int]

    verse_number: Mapped[int]

    verse_text: Mapped[str] = mapped_column(Text)

    translation: Mapped[str] = mapped_column(Text)

    period: Mapped[str]
