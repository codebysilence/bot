from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import func

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base


class SentMessage(Base):

    __tablename__ = "sent_messages"

    id: Mapped[int] = mapped_column(primary_key=True)

    verse_uuid: Mapped[str] = mapped_column(
        ForeignKey("verses.uuid")
    )

    chat_id: Mapped[int] = mapped_column(
        ForeignKey("chats.id")
    )

    sent_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
