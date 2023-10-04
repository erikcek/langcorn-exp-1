from fastapi import FastAPI
from langcorn import create_service

app:FastAPI = create_service("examples.math_chain:chain")
