import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    return ["Amin", "Marce", "Miranda"]

@app.get("/superheroesDC")
def get_superheroes():
    return ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]

@app.get("/superheroesMarvel")
def get_superheroes_marvel():
    return ["Spider-Man", "Iron Man", "Thor", "Hulk", "Black Widow", "Doctor Strange", "Black Panther", "Captain America"]

@app.get("/lord-of-the-rings/warriors")
def get_lotr_warriors():
    return ["Frodo", "Sam", "Gandalf", "Aragorn", "Legolas", "Gimli", "Boromir", "Gollum", "El anillo"]

@app.get("/star-wars/warriors")
def get_starwars_warriors():
    return ['Obiwan', 'el pelón del sable morado', 'Darth Vader', 'El de la colita de caballo', 'Yoda']

@app.get("/warriorsGOT")
def get_warriors_got():
    return ["Jon Snow", "Daenerys Targaryen", "Arya Stark", "Tyrion Lannister", "Cersei Lannister", "Jaime Lannister", "Bran Stark", "Sansa Stark"]