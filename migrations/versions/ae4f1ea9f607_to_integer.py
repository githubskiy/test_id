"""to integer

Revision ID: ae4f1ea9f607
Revises: 3cf723a32dcb
Create Date: 2023-02-27 19:22:15.894082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae4f1ea9f607'
down_revision = '3cf723a32dcb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    # ### end Alembic commands ###