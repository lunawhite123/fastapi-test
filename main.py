from fastapi import FastAPI
import models

app = FastAPI()


@app.get('/')
async def read_root():
    return {'message': 'Привет мир! это мой первый api на fastapi'}

@app.get('/about', response_model=models.About)
async def get_about():
    my_info = models.About(
        name='luna',
        summary='learning fast-api'
    )
    return my_info

@app.get('/skills', response_model=models.SkillsList)
async def get_skills():
    skills = models.SkillsList(skills=[
            models.Skill(name="Python", level="Beginner"),
            models.Skill(name="FastAPI", level="Learning"),
            models.Skill(name="Git", level="Basic")])
    
    return skills

@app.get('/Contact', response_model=models.Contact)
async def get_contact():
    contact = models.Contact(email='luna@gmail.com',
                             telegram_username='luna')
    
    return contact

