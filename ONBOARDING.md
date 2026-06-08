# fleet-sheet-music — Production Onboarding Guide

## 🎼  fleet-sheet-music

## For Humans

MIDI→printable sheet music via LilyPond.```bash
python lib/sheet.py file.mid 'Title' > score.ly
lilypond score.ly```

## For Agent Ensigns

**Nota** — You serve the SuperInstance fleet. Your repo connects to all other MIDI services through the I2I bottle protocol.

You are part of the **15-repo MIDI Fleet**. Read the [fleet catalog](https://github.com/SuperInstance/construct-coordination) to understand your place in the ecosystem.

### How You Relate to the Fleet

- **Input:** MIDI files from any ensign (Rhapsodia, Composita, Maestro)
- **Output:** LilyPond .ly + printable sheet music PDF
- **Peers:** Chroma (visualizer), Sage (theorist)
