from fileinput import filename
import databases, sqlalchemy, shutil
from typing import List
from fastapi import FastAPI, Depends, UploadFile, File
from pydantic import BaseModel, Field
from datetime import datetime

DATABASE_URL = "sqlite:///./store.db"

metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)
artikel = sqlalchemy.Table(
    "artikel",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("nama_jurnal", sqlalchemy.String(500)),
    sqlalchemy.Column("judul_artikel", sqlalchemy.String(500)),
    sqlalchemy.Column("volume_no_tahun", sqlalchemy.String(500)),
    sqlalchemy.Column("jenis_publikasi", sqlalchemy.String(500)),
    sqlalchemy.Column("menjadi_sebagai", sqlalchemy.String(500)),
    sqlalchemy.Column("bukti", sqlalchemy.String(500)),
    sqlalchemy.Column("berkas", sqlalchemy.String(500)),
    sqlalchemy.Column("date_created", sqlalchemy.DateTime())
)
struktural = sqlalchemy.Table(
    "struktural",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("jabatan", sqlalchemy.String(500)),
    sqlalchemy.Column("tahun", sqlalchemy.String(4)),
    sqlalchemy.Column("bukti", sqlalchemy.String(500)),
    sqlalchemy.Column("berkas", sqlalchemy.String(500)),
    sqlalchemy.Column("date_created", sqlalchemy.DateTime())
)
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI(
    docs_url= "/docs",
    redoc_url= "/redocs",
    title= "Artikel dan Struktural API",
    description= "Berikut ini daftar API yang digunakan untuk artikel dan struktural",
    version= "0.0.1",
    openapi_url= "/openapi.json"
)

@app.on_event("startup")
async def connect():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

class RegisterIn_artikel(BaseModel):
    nama_jurnal: str = Field(...)
    judul_artikel: str = Field(...)
    volume_no_tahun: str = Field(...)
    jenis_publikasi: str = Field(...)
    menjadi_sebagai: str = Field(...)
    bukti: str = Field(...)
    berkas: str = Field(...)

class RegisterIn_struktural(BaseModel):
    jabatan: str = Field(...)
    tahun: int = Field(...)
    bukti: str = Field(...)
    berkas: str = Field(...)

class Register_artikel(BaseModel):
    id: int
    nama_jurnal: str
    judul_artikel: str
    volume_no_tahun: str
    jenis_publikasi: str
    menjadi_sebagai: str
    bukti: str
    berkas: str
    date_created: datetime 

class Register_struktur(BaseModel):
    id: int
    jabatan: str
    tahun: int
    bukti: str
    berkas: str
    date_created: datetime 

# artikel
@app.post('/register_artikel/', response_model=Register_artikel, tags= ['artikel'])
async def create(r: RegisterIn_artikel = Depends()):
    query = artikel.insert().values(
        nama_jurnal=r.nama_jurnal,
        judul_artikel = r.judul_artikel,
        volume_no_tahun = r.volume_no_tahun,
        jenis_publikasi = r.jenis_publikasi,
        menjadi_sebagai = r.menjadi_sebagai,
        bukti = r.bukti,
        berkas = r.berkas,
        date_created=datetime.utcnow()
    )
    record_id = await database.execute(query)
    query = artikel.select().where(artikel.c.id == record_id)
    row = await database.fetch_one(query)
    return {**row}

@app.get('/register_artikel/{id}', response_model=Register_artikel, tags= ['artikel'])
async def get_one(id: int):
    query = artikel.select().where(artikel.c.id == id)
    user = await database.fetch_one(query)
    return {**user}

@app.get('/register_artikel/', response_model=List[Register_artikel], tags= ['artikel'])
async def get_all():
    query = artikel.select()
    all_get = await database.fetch_all(query)
    return all_get

@app.put('/register_artikel/{id}', response_model=Register_artikel, tags= ['artikel'])
async def update(id: int, r: RegisterIn_artikel = Depends()):

    query = artikel.update().where(artikel.c.id == id).values(
        nama_jurnal=r.nama_jurnal,
        judul_artikel = r.judul_artikel,
        volume_no_tahun = r.volume_no_tahun,
        jenis_publikasi = r.jenis_publikasi,
        menjadi_sebagai = r.menjadi_sebagai,
        bukti = r.bukti,
        berkas = r.berkas,
        date_created=datetime.utcnow(),
    )
    record_id = await database.execute(query)
    query = artikel.select().where(artikel.c.id == record_id)
    row = await database.fetch_one(query)
    return {**row}

@app.delete("/register_artikel/{id}", response_model=Register_artikel, tags= ['artikel'])
async def delete(id: int):
    query = artikel.delete().where(artikel.c.id == id)
    return await database.execute(query)


# struktural
@app.post('/register_struktural/', response_model=Register_struktur, tags= ['struktural'])
async def create(r: RegisterIn_struktural = Depends()):
    query = struktural.insert().values(
        jabatan=r.jabatan,
        tahun = r.tahun,
        bukti = r.bukti,
        berkas = r.berkas,
        date_created=datetime.utcnow()
    )
    record_id = await database.execute(query)
    query = struktural.select().where(struktural.c.id == record_id)
    row = await database.fetch_one(query)
    return {**row}

@app.get('/register_struktural/{id}', response_model=Register_struktur, tags= ['struktural'])
async def get_one(id: int):
    query = struktural.select().where(struktural.c.id == id)
    user = await database.fetch_one(query)
    return {**user}

@app.get('/register_struktural/', response_model=List[Register_struktur], tags= ['struktural'])
async def get_all():
    query = struktural.select()
    all_get = await database.fetch_all(query)
    return all_get

@app.put('/register_struktural/{id}', response_model=Register_struktur, tags= ['struktural'])
async def update(id: int, r: RegisterIn_struktural = Depends()):
    query = struktural.update().where(struktural.c.id == id).values(
        jabatan=r.jabatan,
        tahun = r.tahun,
        bukti = r.bukti,
        berkas = r.berkas,
        date_created=datetime.utcnow(),
    )
    record_id = await database.execute(query)
    query = struktural.select().where(struktural.c.id == record_id)
    row = await database.fetch_one(query)
    return {**row}

@app.delete("/register_struktural/{id}", response_model=Register_struktur, tags= ['struktural'])
async def delete(id: int):
    query = struktural.delete().where(struktural.c.id == id)
    return await database.execute(query)

#uploadfile 
@app.post('/upload_dokumen', tags= ['uploadData'])
async def upload_file(file: UploadFile = File(...)):
    with open(f'extras/{file.filename}', "wb") as buffer:
        shutil.copyfile(file.file, buffer)
    return {"file_name": file.filename}

@app.post("/upload_img", tags= ['uploadData'])
async def upload_image(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'extras/{img.filename}', "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)
        return {"file_name": img.filename}  