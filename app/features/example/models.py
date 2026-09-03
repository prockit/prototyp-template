"""Tables of the example feature. Class name = Prisma model name in the rewrite."""

from datetime import datetime

from sqlmodel import Field, SQLModel


class ExampleItem(SQLModel, table=True):
    # id and created_at are set in the service, not by the database, like the productive template.
    id: str = Field(primary_key=True)
    title: str
    description: str
    created_at: datetime
