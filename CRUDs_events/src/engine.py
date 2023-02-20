from sqlalchemy import create_engine

# initializing of db engine

path_to_file = "db_info"
with open(path_to_file, encoding='utf-8') as f:
    db_info = []
    for line in f:
        db_info.append(eval(line.replace('\n','')))
db_name = db_info[0]
db_user = db_info[1]
db_pass = db_info[2]
db_host = db_info[3]
db_port = db_info[4]

db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)
