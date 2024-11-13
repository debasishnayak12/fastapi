## SETUSER AND GETUSER (01_BASEAPI)
-- inside 01_BASEAPI folder create main.py file in which route and methods will mention.
-- There also create 3 more files database.py,models.py,schemas.py
-- create virtual environment 01_baseapi and activate it.
-- install requirements.txt file .
-- Inside database.py create connection to database using sqlalchemy.
-- inside models.py create a class User to connect with table.
-- schemas.py is for pydantic validation
#SETUSER(route='/setuser')
-- inside schemas.py create a class UserCreate inside that mention the fields need to be insert  .
-- if data inserted the response will be {"status":"true","message":"Inserted Successfully }.
-- If failed to insert response will be {"status":"false","message":"Failed }.
#GETUSER(route='/getuser')
-- inside schemas.py create a class UserRequest inside that mention the uder  id ,using this id 
    filter data inside main.py .
-- if get user data the response will be {"status":"true","message":"Getuser Successfully,"user":{userdata} }. 
-- If failed to get response will be {"status":"false","message":"Failed }.

##To make exe file of main.py 
--install pyinstaller 
-- run (pyinstaller --onefile --hidden-import=main --hidden-import=uvicorn --hidden-import=fastapi main.py)
