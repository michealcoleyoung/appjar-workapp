from appJar import gui
import pyperclip

def submit(btn):
    id = app.getEntry("ID")
    name = app.getEntry("Name")
    telephone = app.getEntry("Telephone")
    drug = app.getEntry("Drug")
    inquiry = app.getEntry("Inquiry")
    call_notes = app.getTextArea("Notes")

    if app.getRadioButton("choice") == "Yes":
        text = f"{drug}; {inquiry}; Med D: {call_notes}"
    else:
        text = f"{drug}; {inquiry};: {call_notes}"

    # if call notes is too lengthy this will decrease the amount of info in the database
    if len(call_notes) > 15:
        call_notes = call_notes[:15:] + "........"

    # for each submission an additional row is created
    app.addTableRow("History", [id, name, telephone, drug, inquiry, call_notes])

    pyperclip.copy(text)
    app.setTextArea("Notes Submitted", text)


def clear(btn):
    app.clearAllEntries()
    app.clearAllTextAreas()

def title(btn):
    # if addresses are in lowercase this will place it in title case
    text = app.getEntry("Text")
    app.setEntry("Text", text.title())

def lower(btn):
    # if email is present this will place it in lower case
    text = app.getEntry("Text")
    app.setEntry("Text", text.lower())


# establishes gui size and design
app = gui('Work Tool', useTtk=True)
app.setTtkTheme("winnative")
app.setSize("800x800")

# starts tabbed frame
app.startTabbedFrame("MAIN")    # start tabbed frame

app.startTab("Call Notes")

app.addLabel("Member ID:")
app.addEntry("ID")
app.addLabel("Callers Name:")
app.addEntry("Name")
app.addLabel("Telephone Number:")
app.addEntry("Telephone")
app.addLabel("Name of drug:")
app.addEntry("Drug")
app.addLabel("Reason for call")
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

app.addButtons(["SUBMIT", "CLEAR"], [submit, clear])

app.addLabel("Completed Notes:")
app.addTextArea("Notes Submitted")

app.addLabel("Text Converter:")
app.addEntry("Text")
app.setEntryDefault("Text", "Enter text to convert")
app.addButtons(["Title Case", "lower case"], [title, lower])

app.stopTab()

app.startTab("History")
# when all of the information in call notes is completed this tab creates a table with that data
app.addTable("History",
                 [['ID', 'Name', 'Telephone', 'Drug', 'Inquiry', 'Call Notes']])
app.stopTab()

app.stopTabbedFrame()  # stop tabbed frame


app.go()