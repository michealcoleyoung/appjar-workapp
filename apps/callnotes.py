from appJar import gui
import pyperclip

def submit(btn):

    id = app.getEntry("ID")
    name = app.getEntry("Name")
    telephone = app.getEntry("Telephone")
    drug = app.getEntry("Drug")
    inquiry = app.getEntry("Inquiry")
    call_notes = app.getTextArea("Notes")

    text = f"{drug}; {inquiry}: {call_notes}"

    # if call notes is too lengthy this will decrease the amount of info in the database
    if len(call_notes) > 15:
        call_notes = call_notes[:15:] + "........"

    # for each submission an additional row is created
    app.addTableRow("History", [id, name, telephone, drug, inquiry, call_notes])

    app.clearAllEntries()
    app.clearAllTextAreas()

    pyperclip.copy(text)
    app.setTextArea("Notes Submitted", text)


app = gui('Work Tool', useTtk=True)
app.setTtkTheme('winnative')

app.addEntry("ID")
app.addEntry("Name")
app.addEntry("Telephone")
app.addEntry("Drug")
app.addEntry("Inquiry")
app.addLabel("Does the patient have MedD:")
app.addRadioButton("choice", "Yes")
app.addRadioButton("choice", "No")
app.addLabel("Call Notes:")
app.addTextArea("Notes")

app.setEntryDefault("ID", "Member ID")
app.setEntryDefault("Name", "Name")
app.setEntryDefault("Telephone", "Telephone Number")
app.setEntryDefault("Drug", "Drug")
app.setEntryDefault("Inquiry", "Reason For Call")

app.addButton("SUBMIT", submit)
app.addTextArea("Notes Submitted")

app.addTable("History",
                 [['ID', 'Name', 'Telephone', 'Drug', 'Inquiry', 'Call Notes']])


app.go()