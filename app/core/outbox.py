"""Simulated integrations. Nothing is ever sent: messages are stored and shown on `/outbox`.

Every call to `send_message` marks something the real application must integrate for real
(e-mail, Teams, SAP, ...). Record it in README.md under "Needs for the real app".
"""

import uuid
from datetime import UTC, datetime
from typing import Annotated, Literal

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlmodel import Field, Session, SQLModel, col, select

from app.core.db import get_session
from app.core.logger import logger
from app.core.templating import render

Channel = Literal["EMAIL", "TEAMS", "SAP", "OTHER"]


class OutboundMessage(SQLModel, table=True):
    id: str = Field(primary_key=True)
    channel: str
    recipient: str
    subject: str
    body: str
    created_at: datetime


def send_message(
    session: Session, channel: Channel, recipient: str, subject: str, body: str
) -> OutboundMessage:
    message = OutboundMessage(
        id=str(uuid.uuid4()),
        channel=channel,
        recipient=recipient,
        subject=subject,
        body=body,
        created_at=datetime.now(UTC),
    )
    session.add(message)
    session.commit()
    session.refresh(message)
    logger.info(
        "simulated outbound message: channel=%s recipient=%s subject=%s",
        channel,
        recipient,
        subject,
    )
    return message


router = APIRouter(prefix="/outbox")


@router.get("")
def list_messages(
    request: Request, session: Annotated[Session, Depends(get_session)]
) -> HTMLResponse:
    statement = select(OutboundMessage).order_by(col(OutboundMessage.created_at).desc())
    messages = session.exec(statement).all()
    return render(request, "outbox/list.html", {"messages": messages})
