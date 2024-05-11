"""user_saved_item_column_rename

Revision ID: 42e2acc932d1
Revises: 4d1f984bedec
Create Date: 2024-05-06 23:00:35.548534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42e2acc932d1'
down_revision = '4d1f984bedec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_item_saved', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_user_item_saved_saved_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_user_item_saved_item_id', 'item', ['item_id'], ['id'])
        batch_op.drop_column('saved_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_item_saved', schema=None) as batch_op:
        batch_op.add_column(sa.Column('saved_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint('fk_user_item_saved_item_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_user_item_saved_saved_id', 'item', ['saved_id'], ['id'])
        batch_op.drop_column('item_id')

    # ### end Alembic commands ###