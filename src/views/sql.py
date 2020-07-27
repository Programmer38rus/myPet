import sqlalchemy as sa
from db import metadata

import os

file_name = "../views/base.sqlite"

data = "sqlite:///" + file_name

if os.path.exists(file_name):
	print('File is ready...')

else:
    engine = sa.create_engine(data)
    metadata.create_all(engine)

    print('*** Data is created ***')
