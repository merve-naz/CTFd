"""Add deletion constraint for MultipleChoice

Revision ID: 832425686fda
Revises: 1093835a1051
Create Date: 2020-05-08 14:32:22.370572

"""
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "832425686fda"
down_revision = "80ce0f2ffcf2"
branch_labels = None
depends_on = None


def upgrade(op=None):
    bind = op.get_bind()
    url = str(bind.engine.url)

    try:
        if url.startswith("mysql"):
            op.drop_constraint(
                "multiple_choice_ibfk_1", "multiple_choice", type_="foreignkey"
            )
        elif url.startswith("postgres"):
            op.drop_constraint(
                "multiple_choice_id_fkey", "multiple_choice", type_="foreignkey"
            )
    except sa.exc.InternalError as e:
        print(str(e))

    try:
        op.create_foreign_key(
            None, "multiple_choice", "challenges", ["id"], ["id"], ondelete="CASCADE"
        )
    except sa.exc.InternalError as e:
        print(str(e))


def downgrade(op=None):
    bind = op.get_bind()
    url = str(bind.engine.url)

    try:
        if url.startswith("mysql"):
            op.drop_constraint(
                "multiple_choice_ibfk_1", "multiple_choice", type_="foreignkey"
            )
        elif url.startswith("postgres"):
            op.drop_constraint(
                "multiple_choice_id_fkey", "multiple_choice", type_="foreignkey"
            )
    except sa.exc.InternalError as e:
        print(str(e))

    try:
        op.create_foreign_key(
            "multiple_choice_ibfk_1", "multiple_choice", "challenges", ["id"], ["id"]
        )
    except sa.exc.InternalError as e:
        print(str(e))
