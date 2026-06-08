"""MIDI to printable sheet music via LilyPond."""
import json, os, subprocess, tempfile

def midi_to_lilypond(midi_path: str, title: str = "Fleet Composition") -> str:
    """Convert MIDI to LilyPond source using music21."""
    import music21
    
    score = music21.converter.parse(midi_path)
    
    ly_parts = []
    for i, part in enumerate(score.parts):
        notes = part.flat.notes
        ly_notes = []
        for n in notes:
            if n.isRest:
                ly_notes.append(f"r{n.duration.quarterLength}")
            else:
                pn = n.pitch.name.lower().replace('-','')
                octave = n.pitch.octave
                dur = n.duration.quarterLength
                ly_notes.append(f"{pn}{octave}{dur}")
        
        ly = " ".join(ly_notes)
        clef = "treble" if i == 0 else "bass"
        ly_parts.append(f"""
  \\new Staff {{
    \\clef "{clef}"
    {ly}
  }}""")
    
    return f"""\\version "2.22.0"
\\header {{ title = "{title}" }}
\\score {{
  <<{" ".join(ly_parts)} >>
  \\layout {{}}
}}"""

def render_pdf(lilypond_source: str, output_dir: str = ".") -> str:
    """Render LilyPond source to PDF."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.ly', delete=False) as f:
        f.write(lilypond_source)
        ly_path = f.name
    
    result = subprocess.run(['lilypond', '--pdf', f'-o={output_dir}', ly_path],
                          capture_output=True, text=True, timeout=30)
    os.unlink(ly_path)
    
    if result.returncode != 0:
        raise RuntimeError(f"LilyPond error: {result.stderr}")
    
    pdf = os.path.join(output_dir, os.path.basename(ly_path).replace('.ly', '.pdf'))
    return pdf if os.path.exists(pdf) else result.stdout

if __name__ == "__main__":
    import sys
    midi_file = sys.argv[1]
    ly = midi_to_lilypond(midi_file, sys.argv[2] if len(sys.argv) > 2 else "Fleet Composition")
    print(ly)
