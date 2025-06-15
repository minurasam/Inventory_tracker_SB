from fastapi import FastAPI, HTTPException, Depends
from app.models import UserLogin, UserCreate
from app.auth.Pass_Hash import hash_password, verify_password
from app.auth.Fake_database import get_user_by_username, save_user

app = FastAPI()

@app.post("/signup")
async def signup(user: UserCreate):
    # 1. Check if user already exists
    existing_user = get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    # 2. Hash the password
    hashed_pw = hash_password(user.password)

    # 3. Save user
    save_user(user.username, hashed_pw)

    return {"message": "User created successfully"}

@app.post("/login")
async def login(user: UserLogin):
    # 1. Get user from DB
    db_user = get_user_by_username(user.username)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 2. Check password
    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}
