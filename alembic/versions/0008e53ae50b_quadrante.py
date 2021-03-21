"""quadrante

Revision ID: 0008e53ae50b
Revises: 40544db61e1e
Create Date: 2021-03-16 07:44:38.102223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0008e53ae50b'
down_revision = '40544db61e1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('perfil',
    sa.Column('survey_id', sa.String(length=20), nullable=False),
    sa.Column('respondent_id', sa.String(length=20), nullable=False),
    sa.Column('cnt', sa.Integer(), nullable=False),
    sa.Column('question_1', sa.String(length=255), nullable=True),
    sa.Column('question_2', sa.String(length=255), nullable=True),
    sa.Column('question_3', sa.String(length=255), nullable=True),
    sa.Column('question_4', sa.String(length=255), nullable=True),
    sa.Column('question_5', sa.String(length=255), nullable=True),
    sa.Column('question_6', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('survey_id', 'respondent_id', 'cnt')
    )
    op.create_table('quadrante',
    sa.Column('survey_id', sa.String(length=20), nullable=False),
    sa.Column('respondent_id', sa.String(length=20), nullable=False),
    sa.Column('question_7', sa.String(length=255), nullable=True),
    sa.Column('question_8', sa.String(length=255), nullable=True),
    sa.Column('question_14', sa.String(length=255), nullable=True),
    sa.Column('question_15', sa.String(length=255), nullable=True),
    sa.Column('question_17', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('survey_id', 'respondent_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quadrante')
    op.drop_table('perfil')
    # ### end Alembic commands ###
