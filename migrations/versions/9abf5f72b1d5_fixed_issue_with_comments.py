"""Fixed issue with comments

Revision ID: 9abf5f72b1d5
Revises: 9b85cce61de8
Create Date: 2024-11-10 02:42:47.040565

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9abf5f72b1d5'
down_revision: Union[str, None] = '9b85cce61de8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###