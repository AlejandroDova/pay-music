import data
notas = data.notas

def scaleMayor_contructor(scale,note):
    scaleReturn = []
    for x in scale:
        # First add the first note, afte that search in notes cromatic
        for no in notas:
            if note == no["semitono"]:
                if no["nota"] == "":
                    scaleReturn.append(no["sotenido"])
                    break
                else:
                    scaleReturn.append(no["nota"])
                    break
                    
        # sum the note
        note += x
        note = in_range_cromatic(note)
    return scaleReturn

def in_range_cromatic(note):
    if note > 12:
        return note-12
    else:
        return note