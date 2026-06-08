# 🎼 fleet-sheet-music

> *MIDI → printable sheet music for the fleet*

Converts Standard MIDI Format 1 files into printable sheet music via LilyPond. Every MIDI file from any fleet ensign becomes a publishable score.

```bash
pip install music21
python lib/sheet.py path/to/file.mid "My Title" > score.ly
lilypond score.ly  # produces score.pdf
```

## Architecture
```
MIDI → music21 parse → LilyPond source → PDF/PNG sheet music
```

## Ennsign: **Nota** — Fleet Notation Officer
**Summon:** `/ensign nota render path/to/file.mid`
