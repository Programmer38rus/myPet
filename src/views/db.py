import sqlalchemy as sa

metadata = sa.MetaData()

family = sa.Table('Family', metadata,
                  sa.Column('id', sa.Integer, primary_key=True),
                  sa.Column('name', sa.Text),
                  sa.Column('age', sa.Integer)
                  )

print('loading db file...')