# ai-platform-engineering-journey

python -m venv .venv  
.venv\Scripts\activate
.\.venv\Scripts\Activate.ps1

python -m pip install fastapi "uvicorn[standard]" pydantic pytest
python -m pip freeze > requirements.txt
python -m uvicorn app.main:app --reload

