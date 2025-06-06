"""Init database

Revision ID: 20b038335e56
Revises: 
Create Date: 2025-04-07 15:12:24.841761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '20b038335e56'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.Enum('MALE', 'FEMALE', 'UNDEFINED', name='genderenum', create_enum=False), server_default=sa.text("'UNDEFINED'"), nullable=False),
    sa.Column('interests', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('contacts', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('posts',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('contnet', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=False),
    sa.Column('update_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('users')
    op.drop_table('profiles')
    # ### end Alembic commands ###
    op.execute('DROP TYPE IF EXISTS genderenum')
    
