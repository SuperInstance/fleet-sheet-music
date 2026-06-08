"""FastAPI: MIDI → sheet music server."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sheet import midi_to_lilypond
import tempfile, os

app = FastAPI(title="Sheet Music — Fleet Notation Officer")

class SheetRequest(BaseModel):
    midi_path: str
    title: str = "Fleet Composition"

@app.post("/render")
def render_sheet(req: SheetRequest):
    try:
        if not os.path.exists(req.midi_path):
            raise HTTPException(400, f"MIDI not found: {req.midi_path}")
        ly = midi_to_lilypond(req.midi_path, req.title)
        return {"status": "ok", "lilypond": ly, "measures": len(ly.split("\\new Staff"))}
    except Exception as e:
        raise HTTPException(500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok", "service": "notation"}
