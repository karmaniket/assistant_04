import wikipedia
import PySimpleGUI as av
import pyttsx3
import wolframalpha
client = wolframalpha.Client("WGEVLY-YU4VQR3WU8")

av.theme('Black')
layout =[[av.Text('Give me command sir.'), av.InputText()],[av.Button('Give'), av.Button('Cancel')]]
window = av.Window('PyDa', layout)

engine = pyttsx3.init()
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki = wikipedia.summary(values[0], sentences=2)
        wolfram = next(client.query(values[0]).results).text
        engine.say(wolfram)
        av.PopupNonBlocking("Wolfram Result: "+wolfram,"Wikipedia Result: "+wiki)
    except wikipedia.exceptions.DisambiguationError:
        wolfram = next(client.query(values[0]).results).text
        engine.say(wolfram)
        av.PopupNonBlocking(wolfram)
    except wikipedia.exceptions.PageError:
        wolfram = next(client.query(values[0]).results).text
        engine.say(wolfram)
        av.PopupNonBlocking(wolfram)
    except:
        wiki = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki)
        av.PopupNonBlocking(wiki)

    engine.runAndWait()
    print (values[0])

window.close()