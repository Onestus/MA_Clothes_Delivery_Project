"""initial

Revision ID: 8dedd5b7ba2c
Revises: 
Create Date: 2024-01-04 15:57:57.312661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dedd5b7ba2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payments',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('order_id', sa.UUID(), nullable=True),
    sa.Column('receiver', sa.String(), nullable=False),
    sa.Column('sum', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payments_id'), 'payments', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_payments_id'), table_name='payments')
    op.drop_table('payments')
    # ### end Alembic commands ###