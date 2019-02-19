from appJar import gui


app = gui('Work Tool', useTtk=True)
app.setTtkTheme('winnative')

app.startTabbedFrame("MAIN")    # start tabbed frame

app.startTab("Call Notes")
# call notes
app.stopTab()

app.startTab("Blurb")
# application blurb
app.stopTab()

app.startTab("Case Converter")
# case converter
app.stopTab()

app.startTab("Call Data")
# call data
app.stopTab()

app.stopTabbedFrame()  # stop tabbed frame


app.go()