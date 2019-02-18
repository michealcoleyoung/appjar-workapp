from appJar import gui
import pyperclip

def submit(btn):

    name = app.getEntry("Name")
    telephone = app.getEntry("Telephone")
    drug = app.getEntry("Drug")
    inquiry = app.getEntry("Inquiry")
    call_notes = app.getTextArea("Notes")


    text = f"{drug}; {inquiry}: {call_notes}"

    # copies submitted text
    pyperclip.copy(text)
    app.setTextArea("Notes Submitted", text)


    # table creation with submitted data

    # for each submission an additional row is created
    app.addTableRow("History", [name, telephone, drug, inquiry, call_notes])
    app.getTableEntries("History")

    app.clearAllEntries()
    app.clearAllTextAreas()

def retrieve(btn):
    app.getTableEntries("History")



app = gui('Work Tool', useTtk=True)
app.setTtkTheme('winnative')

app.addEntry("Name")
app.addEntry("Telephone")
app.addEntry("Drug")
app.addEntry("Inquiry")
app.addLabel("Does the patient have MedD:")
app.addRadioButton("choice", "Yes")
app.addRadioButton("choice", "No")
app.addLabel("Call Notes:")
app.addTextArea("Notes")

app.setEntryDefault("Name", "Name")
app.setEntryDefault("Telephone", "Telephone Number")
app.setEntryDefault("Drug", "Drug")
app.setEntryDefault("Inquiry", "Reason For Call")

app.addButton("SUBMIT", submit)
app.addTextArea("Notes Submitted")

app.addTable("History",
                 [['Name', 'Telephone', 'Drug', 'Inquiry', 'Call Notes']])

app.button("GET DATA", retrieve)



app.go()