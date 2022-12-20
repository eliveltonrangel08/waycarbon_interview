"""first db model

Revision ID: 67a6c44e361b
Revises: 
Create Date: 2022-12-19 20:23:43.233529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67a6c44e361b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_enabled', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('nickname', sa.String(length=255), nullable=True),
    sa.Column('area', sa.String(length=255), nullable=True),
    sa.Column('code_number', sa.String(length=128), nullable=True),
    sa.Column('address_street', sa.String(length=128), nullable=True),
    sa.Column('address_number', sa.String(length=128), nullable=True),
    sa.Column('address_neighborhood', sa.String(length=128), nullable=True),
    sa.Column('address_code', sa.String(length=64), nullable=True),
    sa.Column('address_city', sa.String(length=128), nullable=True),
    sa.Column('address_country', sa.String(length=128), nullable=True),
    sa.Column('contact', sa.String(length=64), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_id'), 'company', ['id'], unique=False)
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=False)
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('alias', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('settings', sa.JSON(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_role_id'), 'role', ['id'], unique=False)
    op.create_index(op.f('ix_role_name'), 'role', ['name'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('activitylog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('json_data', sa.JSON(), nullable=True),
    sa.Column('user_ip', sa.String(length=64), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('logged_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['logged_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_activitylog_id'), 'activitylog', ['id'], unique=False)
    op.create_index(op.f('ix_activitylog_type'), 'activitylog', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_activitylog_type'), table_name='activitylog')
    op.drop_index(op.f('ix_activitylog_id'), table_name='activitylog')
    op.drop_table('activitylog')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_role_name'), table_name='role')
    op.drop_index(op.f('ix_role_id'), table_name='role')
    op.drop_table('role')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_index(op.f('ix_company_id'), table_name='company')
    op.drop_table('company')
    # ### end Alembic commands ###
