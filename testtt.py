from fastapi import FastAPI, Depends, HTTPException 
from fastapi.security import HTTPBasicCredentials 
 
app = FastAPI() 
 
# Replace these with your actual username and password 
USERNAME = "zhassulan_d0711@ptr.nis.edu.kz" 
PASSWORD = "z123456!!" 
 
def authenticate_basic_auth(credentials: HTTPBasicCredentials = Depends()): 
    if credentials.username != USERNAME or credentials.password != PASSWORD: 
        raise HTTPException(status_code=401, detail="Invalid credentials") 
    return True 
 
 
@app.get("/transmit-data") 
async def transmit_data(authorized: bool = Depends(authenticate_basic_auth)): 
    # Your logic to transmit data to Microsoft service goes here 
    return "ok"