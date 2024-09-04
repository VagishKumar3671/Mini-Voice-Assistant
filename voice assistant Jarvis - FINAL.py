import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import datetime
#import pyaudio #1041
import os


x='yes'

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

hour=int(datetime.datetime.now().hour)
def quarry(hour):
    if (hour>=0 and hour<6):
        speak('good morning sir')
    elif(hour>=6 and hour<9):
        import random
        quote = ['You cannot believe in god until you believe in yourself',
                 'The greatest sin is to think that you are weak',
                 'Do one thing at a Time, and while doing it put your whole Soul into it to the exclusion of all else',
                 'Take risks in your life, If you win, you can lead! If you loose, you can guide',
                 'We are ever free if we would only believe it, only have faith enough',
                 'Arise, awake and stop not till the goal is reached',
                 'The moment you give up is the moment you let someone else win',
                 "A positive mind looks for ways it can be done; a negative mind looks for ways it can't be done",
                 'Every morning we are born again. What we do today matters most',
                 'No one is you and that is your super power',
                 "Sometimes you have to do what's best for you and your life, not what's best for everyone else",
                 "Don't talk, just act. Don't say, just show. Don't promise, just prove",
                 "It's okay to be a glowstick: Sometimes we have to break before we shine",
                 "It's not enough to just start. You have to keep on going too."]
        todayquote = random.choice(quote)
        speak('good morning sir')
        speak('today quote')
        speak(todayquote)
    elif(hour>=9 and hour<12) :
        speak('good morning sir')
    elif (hour>=12 and hour<18):
        speak('good afternoon sir')
    else:
        speak('good evening sir')
quarry(hour)


speak('''HI I AM javis

HOW CAN I HELP YOU .

speak now sir
''')


while(x=='yes'):
    with sr.Microphone() as source:
        print('''
HI! I AM JARVIS
     HOW CAN I HELP YOU!

     # YouTube
     # Amazon
     # Search
     # Search image
     # Wikipedia
     # Noon
     # Maps
     # Mail
     # Games
     # Play my favourite musics
     # Motivational quotes
     # What is the time? or what is the data? or what is the day?
     # Open Zoom or Excel or Word or Notepad or Python?
     # About me as javis
     # Whatapp 
     
     SPEAK NOW SIR....''')
        audio = r2.listen(source)
        try:
            get = r2.recognize_google(audio)
            print(get)
            pass
        except sr.UnknownValueError:
            print('⚠ ERROR ⚠')
        except sr.RequestError as e:
            print('failed'.format(e))

    if 'youtube' in r2.recognize_google(audio).lower():
        speak('opening youtube in microsoft edge')
        r2 = sr.Recognizer()
        url = '''https://www.youtube.com/results?search_query='''
        with sr.Microphone() as source:
            speak('what show i search in youtube')
            print('search your query:')
            print('\n''Listening.....','\n')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url + get)
            except sr.UnknownValueError:
                print('ERROR')
            except sr.RequestError as e:
                print('failed'.format(e))

        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'time' in r2.recognize_google(audio).lower():
        import calendar
        def findDay(date):
            day, month, year = (int(i) for i in date.split(' '))
            dayNumber = calendar.weekday(year, month, day)
            days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"]
            return (days[dayNumber])
        from datetime import datetime
        now=datetime.now()
        d1= now.strftime("%B %d,%Y")
        now = datetime.now()
        time=now.strftime("%H:%M:%S")
        print('local time:',time,'\n''date:',d1,(findDay(now.strftime("%d %m %Y"))))
        speak('the time is')
        speak(time)
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'date' in r2.recognize_google(audio).lower():
        import calendar
        def findDay(date):
            day, month, year = (int(i) for i in date.split(' '))
            dayNumber = calendar.weekday(year, month, day)
            days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"]
            return (days[dayNumber])
        from datetime import datetime
        now=datetime.now()
        d1= now.strftime("%B %d,%Y")
        now = datetime.now()
        time=now.strftime("%H:%M:%S")
        print('local time:',time,'\n''date:',d1,(findDay(now.strftime("%d %m %Y"))))
        speak(d1)
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'day' in r2.recognize_google(audio).lower():
        from datetime import datetime
        now = datetime.now()
        d1=now.strftime("%d %m %Y")
        import calendar
        def findDay(date):
            day, month, year = (int(i) for i in date.split(' '))
            dayNumber = calendar.weekday(year, month, day)
            days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"]
            return (days[dayNumber])
        day=findDay(d1)
        print(day)
        speak(day)
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break



    elif 'amazon' in r2.recognize_google(audio).lower():
        speak('opening amazon in microsoft edge')
        r2 = sr.Recognizer()
        url = 'https://www.amazon.ae/s?k='
        with sr.Microphone() as source:
            speak('what show i search in amazon')
            print('search your query:')
            print('\n''Listening.....', '\n')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url + get)
            except sr.UnknownValueError:
                print('ERROR')
            except sr.RequestError as e:
                print('failed'.format(e))

        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'search' in r2.recognize_google(audio).lower():
        r2 = sr.Recognizer()
        url = 'https://www.google.com/search?q='
        with sr.Microphone() as source:
            speak('what show i search in google')
            print('search your query:')
            print('\n''Listening.....', '\n')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url + get)
            except sr.UnknownValueError:
                print('ERROR')
            except sr.RequestError as e:
                print('failed'.format(e))

        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'image' in r2.recognize_google(audio).lower():
        speak('opening image from microsoft edge')
        r2 = sr.Recognizer()
        url = 'https://www.google.com/search?safe=strict&hl=EN&tbm=isch&sxsrf=ALeKk00jlXtpGGhwJAvrjhsz9PsFWGkZvg%3A1602959613183&source=hp&biw=1600&bih=789&ei=_TiLX-OzCIT4U4zPhoAK&q='
        with sr.Microphone() as source:
            speak('what show i search in google image')
            print('search your query:')
            print('\n''Listening.....', '\n')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url + get)
            except sr.UnknownValueError:
                print('ERROR')
            except sr.RequestError as e:
                print('failed'.format(e))
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break



    elif 'wikipedia' in r2.recognize_google(audio).lower():
        speak('opening wikipedia from microsoft edge')
        r2 = sr.Recognizer()
        url = 'https://en.wikipedia.org/wiki/'
        with sr.Microphone() as source:
            speak('what show i search in wikipedia')
            print('search your query:')
            print('\n''Listening.....', '\n')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url + get)
            except sr.UnknownValueError:
                print('ERROR')
            except sr.RequestError as e:
                print('failed'.format(e))

        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break


    elif 'noon' in r2.recognize_google(audio).lower():
        speak('opening noon for shopping')
        r2 = sr.Recognizer()
        url = 'https://www.noon.com/uae-en/'
        with sr.Microphone() as source:
            speak('what show i search in noon')
            print('search your query:')
            print('\n''Listening.....', '\n')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url + get)
            except sr.UnknownValueError:
                print('ERROR')
            except sr.RequestError as e:
                print('failed'.format(e))

        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'map' in r2.recognize_google(audio).lower():
        speak('opening google maps')
        r2 = sr.Recognizer()
        url = 'https://www.google.com/maps/place/'
        with sr.Microphone() as source:
            speak('what show i search in google map')
            print('search your query:')
            print('\n''Listening.....', '\n')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url + get)
            except sr.UnknownValueError:
                print('ERROR')
            except sr.RequestError as e:
                print('failed'.format(e))

        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'mail' in r2.recognize_google(audio).lower():
        speak('opening mail')
        r2 = sr.Recognizer()
        url = 'https://mail.google.com/mail/u/0/?tab=rm#inbox'
        with sr.Microphone() as source:
            print('''>>>say what's your choice sir:
                        # compose mail
                        # check send mail
                        # check inbox of your mail
                  ''')
            speak('''say what's your choice sir
            compose mail
            check send mail
            check inbox of your mail
            sir''')
            print('\n''Listening.....', '\n')
            audio=r2.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
                pass
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'compose'in r2.recognize_google(audio):
                import smtplib  # (simple mail transfer protocol library)
                from email.message import EmailMessage
                print('automatic email sender')
                help = smtplib.SMTP('smtp.gmail.com', 587)  # server
                help.starttls()  # tust me the server
                help.login('jackfind31@gmail.com', 'jkisvagishkumar')
                subject = sr.Recognizer()
                text = sr.Recognizer()
                speak('master can you enter the  email id to the sender')
                speak('for the better clarity')
                to = input('Enter the (To email id):')
                print()
                with sr.Microphone() as source:
                    speak('what is the subject of mail master')
                    print('listening...')
                    audio = subject.listen(source)
                    subject = subject.recognize_google(audio)
                    print('subject:', subject, '\n')
                    speak('what is the content of mail master')
                    print('listening...')
                    audio = text.listen(source)
                    text = text.recognize_google(audio)
                    print('content:', text)
                    email = EmailMessage()
                    email['From'] = 'jackfind31@gmail.com'
                    email['To'] = to
                    email['Subject'] = subject
                    email.set_content(text)
                    help.send_message(email)
                    speak('''master the email has been send to server
                     with in a minute the email will be send to person''')
                print('\n''The mail is successfully send to person!!')
                speak('The mail is successfully send to person')

            elif'send'in r2.recognize_google(audio):
                url='https://mail.google.com/mail/u/0/?tab=rm#sent'
                wb.get().open_new(url)
            else:
                url='https://mail.google.com/mail/u/0/?tab=rm#inbox'
                wb.get().open_new(url)
            with sr.Microphone() as source:
                r3 = sr.Recognizer()
                print('\n''''>>> You want continue with me?
                                            say(yes or no)...''')
                speak('You want continue with me')
                print('\n''Listening.....', '\n')
                audio = r3.listen(source)
                try:
                    get = r2.recognize_google(audio)
                    print(get)
                except sr.UnknownValueError:
                    print('⚠ ERROR ⚠')
                except sr.RequestError as e:
                    print('failed'.format(e))
                if 'yes' in r2.recognize_google(audio):
                    continue
                elif 'go ahead' in r2.recognize_google(audio):
                    continue
                else:
                    x = 'no'
                    break

    elif'games' in r2.recognize_google(audio).lower():
        print('WELCOME TO PYCHARM GAMES WITH JARVIS',
              '''
              # gusses the word[jumbled words]
              # gussing game with the number
              
              say your choice:''')
        with sr.Microphone() as source:
            r2=sr.Recognizer()
            speak('''WELCOME TO PYCHARM GAMES WITH JARVIS
                    jumbled words or gusses the word
                    gussing game with the number
                    say your choice''')
            print('\n''Listening.....', '\n')
            audio=r2.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
                pass
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'jumbled words'in r2.recognize_google(audio):
                import random
                import time
                speak('''
                welcome to gussing game
                if you win all the chance 
                you will win 100 dhs
                
                1 chance 10dhs
                2 chance 20 dhs
                3 chance 30 dhs
                
                enter your choice''')
                chance = int(input('''
                WELCOME TO GUSSING GAME
                        #Guessing the words

                [if you win all chance's,you will win 100dhs]

                if u want:
                1chance=10dhs
                2chance=20dhs
                3chance=30dhs

                enter your choice:'''))
                speak('enter you want hint ')
                speak('say yes or no')
                hint = input('''
                enter you want hint(say yes or no):''')
                name = ['motherboard', 'processor', 'memory', 'case', 'sound card', 'monitor', 'mouse', 'keyboard',
                        'graphics processing unit']
                l = ['loading', '', '', '', '', '', '']
                print()
                for i in range(5):
                    time.sleep(.60)
                    print(l[i] + '.' * i, end='')
                print('\n')
                for i in range(chance):
                    print()
                    d = {
                        'motherboard': 'the core of the system. It really is the PC; everything else is connected to it, and it controls everything in the system.',
                        'processor': "the often thought of as the engine of the computer. It's also called the CPU (central processing unit).",
                        'memory': "RAM (for random access memory),which holds all the programs and data the processor is using at a given time.",
                        'case': "chassis that houses the motherboard, power supply, disk drives, adapter cards, and any other physical components in the system.",
                        'sound card': "It enables the PC to generate complex sounds",
                        'monitor': " an output device that displays information in pictorial form.",
                        'mouse': 'a hand-held pointing device that detects two-dimensional motion relative to a surface',
                        'keyboard': ' an input device that allows a person to enter letters, numbers, and other symbols  into a computer. It is one of the most used input devices for computers.',
                        'graphics processing unit': 'also known as a video card'}
                    random_name = random.choice(name)
                    index = name.index(random_name)
                    random_name1 = list(random_name)
                    jumbledword = ''
                    del name[index]
                    for j in range(len(random_name1)):
                        random_namej = random.choice(random_name1)
                        indexj = random_name1.index(random_namej)
                        jumbledword += random_namej
                        del random_name1[indexj]
                    if (hint == 'no') or (hint == 'n') or (hint == 'NO') or (hint == 'N'):
                        print('[' + jumbledword + ']')
                        speak('gusses and enter the word')
                        gusses = input("gusses and enter the word:")
                        gusses = gusses.lower()
                        if (gusses == random_name):
                            memes = random.choice(
                                ['amazing', 'wonderful', 'marvellous', 'great', 'magnificent', 'glorious'])
                            print(memes, '!...', '  ', 'you got a correct answer', '\n', 'your amount:', '100dhs')
                            break
                        else:
                            memes = random.choice(['retry', 're-attempt', 'redo', 'reiterate', 'take another stab'])
                            print(memes, '!...', '  ', 'you got a wrong answer'"\n the answer is:", random_name)
                            continue
                    else:
                        print('[' + jumbledword + ']')
                        print(d[random_name])
                        speak('gusses and enter the word')
                        gusses = input("gusses and enter the word:")
                        gusses = gusses.lower()
                        if (gusses == random_name):
                            memes = random.choice(
                                ['amazing', 'wonderful', 'marvellous', 'great', 'magnificent', 'glorious'])
                            print(memes, '!...', '  ', 'you got a correct answer', '\n', 'your amount:', '100dhs')
                            break
                        else:
                            memes = random.choice(['retry', 're-attempt', 'redo', 'reiterate', 'take another stab'])
                            print(memes, '!...', '  ', 'you got a wrong answer'"\n the answer is:", random_name)
                            continue
            else:
                import random
                speak('''
                WELCOME TO GUSSING GAME OF JSSPS MEGA MA'AM
                                     gussing game with the number
                    if you lose this game this amount will go to mega ma'am trust for her throat
                    if u want
                    1 chance 10dhs
                    2 chance 20dhs
                    3 chance 30dhs
                ''')
                print(
                    '''WELCOME TO GUSSING GAME OF JSSPS MEGA MA'AM
                                     #gussing game with the number
                    if you lose this game this amount will go to [mega ma'am trust] for her throat
                    if u want:
                    1chance=10dhs
                    2chance=20dhs
                    3chance=30dhs
                    ''')
                speak('enter the amount of betting')
                amount = int(input('enter the amount:'))
                speak('enter the number chance')
                x = int(input('Enter the no.s chance:'))
                print('hello u need to gusses the number-[1-10] ')
                speak('hello you need to gusses the number for 1 to 10')
                for i in range(x):
                    user_num = int(input('enter the number:'))
                    random_num = random.randint(1, 10)
                    if (user_num == random_num):
                        memes = random.choice(
                            ['amazing', 'wonderful', 'marvellous', 'great', 'magnificent', 'glorious'])
                        print(memes, '!...', '  ', 'you got a correct answer', '\n', 'your amount:', amount * x)
                        break
                    elif (user_num != random_num):
                        memes = random.choice(['retry', 're-attempt', 'redo', 'reiterate', 'take another stab'])
                        print(memes, '!...', '  ', 'you got a wrong answer')
                        continue
                    else:
                        continue

        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'favourite musics' in r2.recognize_google(audio).lower():
        speak("opening favourite musics from youtube")
        url = "https://www.youtube.com/watch?v=075Z7tJC_-I&list=PLHHoSeYXK1pC_v7TVewAZC2PHTdVu7v5F"
        wb.get().open_new(url)
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'motivational quote' in r2.recognize_google(audio).lower():
        speak('yes sir')
        speak('our wish my order')
        import random
        quote=['You cannot believe in god until you believe in yourself','The greatest sin is to think that you are weak','Do one thing at a Time, and while doing it put your whole Soul into it to the exclusion of all else',
               'Take risks in your life, If you win, you can lead! If you loose, you can guide','We are ever free if we would only believe it, only have faith enough',
               'Arise, awake and stop not till the goal is reached','The moment you give up is the moment you let someone else win',
               "A positive mind looks for ways it can be done; a negative mind looks for ways it can't be done",'Every morning we are born again. What we do today matters most',
               'No one is you and that is your super power',"Sometimes you have to do what's best for you and your life, not what's best for everyone else",
               "Don't talk, just act. Don't say, just show. Don't promise, just prove","It's okay to be a glowstick: Sometimes we have to break before we shine","It's not enough to just start. You have to keep on going too."]
        todayquote=random.choice(quote)
        print(todayquote)
        speak(todayquote)
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break


    elif 'whatsapp' in r2.recognize_google(audio).lower():
        speak('opening whatsapp sir')
        url='https://web.whatsapp.com/'
        wb.get().open_new(url)
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'about you' in r2.recognize_google(audio).lower():
        speak('yes sir')
        import os
        os.startfile('C:\\Users\\gvagi\\Desktop\\Pycharm2\\SPEECH RECOGNITION.txt')
        os.startfile('C:\\Users\\gvagi\\Desktop\\speech to text.txt')
        speak('i was developed from speech to text program from that master got idea that about creating his own Ai so he developed me named jarvis')
        speak('i was inspired from iron man movie')
        speak("since there is no available of raspberry pi we couldn't make like amazon alexa")
        speak('we develop in future')
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'notepad' in r2.recognize_google(audio).lower():
        speak('opening notepad sir')
        path='''C:\\WINDOWS\\system32\\notepad.exe'''
        os.startfile(path)
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'word' in r2.recognize_google(audio).lower():
        speak('opening word sir')
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk')
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break


    elif 'excel' in r2.recognize_google(audio).lower():
        speak('opening excel sir')
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk')
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break


    elif 'python' in r2.recognize_google(audio).lower():
        speak('opening python sir')
        os.startfile('C:\\Users\\gvagi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.6\\IDLE (Python 3.6 64-bit).lnk')
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    elif 'zoom' in r2.recognize_google(audio).lower():
        speak('opening zoom sir')
        os.startfile('C:\\Users\\gvagi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom.lnk')
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break

    else:
        print("”sorry, that’s my not abilities at the moment”")
        speak('sorry that’s not my abilities at the moment')
        with sr.Microphone() as source:
            r3 = sr.Recognizer()
            print('\n''''>>> You want continue with me?
                                        say(yes or no)...''')
            speak('You want continue with me')
            print('\n''Listening.....', '\n')
            audio = r3.listen(source)
            try:
                get = r2.recognize_google(audio)
                print(get)
            except sr.UnknownValueError:
                print('⚠ ERROR ⚠')
            except sr.RequestError as e:
                print('failed'.format(e))
            if'yes'in r2.recognize_google(audio):
                continue
            elif'go ahead'in r2.recognize_google(audio):
                continue
            else:
                x='no'
                break
print()
if (hour>=0 and hour<12):
    wish='have a good day ahead sir'
else:
    wish='have a good evening ahead sir'
print('Ok,thank you for your response')
print(wish)
print('bye sir!!')
speak('''ok thank you for your response''')
speak(wish)
speak('bye sir')

# '''https://www.amazon.ae/s?k='''
# '''https://www.google.com/search?q='''
# '''https://www.google.com/search?safe=strict&hl=EN&tbm=isch&sxsrf=ALeKk00jlXtpGGhwJAvrjhsz9PsFWGkZvg%3A1602959613183&source=hp&biw=1600&bih=789&ei=_TiLX-OzCIT4U4zPhoAK&q=''' -image
# https://en.wikipedia.org/wiki/-wiki
#https://web.whatsapp.com/