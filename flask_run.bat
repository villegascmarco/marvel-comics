@ECHO OFF

cls
if not exist venv/ (
    py -m venv venv 
    ECHO Virtual environment "venv" created.
    call .\venv\Scripts\activate

    pip install -r requirements.txt
) 

call .\venv\Scripts\activate

cd %~d0%~p0

set FLASK_DEBUG=1

set FLASK_APP=app/

set FLASK_ENV=venv

flask run