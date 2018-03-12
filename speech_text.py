import speech_recognition as sr
import detect_text

subscription_key_vision = "9c47fc0301fe4e3696b44818e1721da0" 
r = sr.Recognizer()
m = sr.Microphone()

def detect_face():
	return

def analyse(text):
	text = text.encode("utf-8")
	print("str = ",(text))
	if("rahul" in text.lower()):
		detect_text.localize_text(subscription_key_vision, "https://3.bp.blogspot.com/-lmL864sF8A4/WGph86k0eEI/AAAAAAAAEE4/34SkurmxHXI2bqupRoeGO2makaYFkPQngCLcB/s1600/je2.png", "Rahul")
	elif("sayan" in text.lower()):
		detect_face()	

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
                analyse(value)
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
