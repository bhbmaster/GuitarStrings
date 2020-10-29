for KEY in ['C' , 'C#', 'D', 'D#', 'E', 'F', 'F#' , 'G', 'G#', 'A', 'A#', 'B']:
    for SCALE in ['major','minor','dorian','phrygian','minor_pentatonic','major_pentatonic','harmonic_minor','aeolian','minor_blues','locrian','lydian']:
        print(f"Plotting {KEY} key {SCALE} scale")
        plot(KEY,scales[SCALE])
print("Done")