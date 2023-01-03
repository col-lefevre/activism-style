# MISC
def getShortStyle():
    return ['edu', 'emp', 'org', 'phi', 'pro']

def getLongStyle():
    return ['Educator', 'Empath', 'Organizer', 'Philanthropist', 'Protestor']

def convertShortToLong(styleShort):
    return getLongStyle()[getShortStyle().index(styleShort)]

# CONTENT -> /
# Get short, snappy descriptions for index
def getStyleBlurb():
    styleBlurbs = [\
        ['edu', convertShortToLong('edu'), "Educators are ready at a moment's notice to share resources and information related to reproductive rights"],\
        ['emp', convertShortToLong('emp'), "Empaths help those seeking reproductive care, whether by lending a sympathetic ear or offering a ride to a local clinic"],\
        ['org', convertShortToLong('org'), "Organizers ensure activist events related to reproductive rights, such as abortion access, are successful and run smoothly"],\
        ['phi', convertShortToLong('phi'), "Philanthropists support reproductive rights by increasing the resources of abortion funds and other pro-choice organizations"],\
        ['pro', convertShortToLong('pro'), "Protestors visibly share their opinions on reproductive rights like abortion access and ensure their voices are heard"]\
    ]
    return styleBlurbs


# CONTENT -> /quiz
# Get question text for Q1-12
def getQDesc(qNum):
    qDescs = [\
        (1, "explain controversial issues"), \
        (1, "openly support causes important to you in public"), \
        (1, "plan support out of the public view"), \
        (1, "provide resources and information to other advocates"), \
        (1, "help people one-on-one"), \
        (2, "your privacy and/or anonymity"), \
        (2, "your time constraints"), \
        (2, "interactions with people who disagree with your beliefs"), \
        (2, "judgment from your peers and/or family about your beliefs"), \
        (3, "donate money"), \
        (3, "donate your time or supplies/resources"), \
        (3, "share information to educate or inform the public or other advocates")\
    ]
    return f'As an activist, you would {qDescVerb(qDescs[qNum-1][0])} {qDescs[qNum-1][1]}.'

def qDescVerb(prefixNum):
    if prefixNum == 1:
        return 'like to'
    elif prefixNum == 2:
        return 'worried about'
    elif prefixNum == 3:
        return 'find it easy to'

# Get likert scale labels
def getQLabels(qNum):
    qLabels = [\
        ["strongly agree", "agree", "neutral", "disagree", "strongly disagree"] \
    ]
    if 1 <= qNum <= 12:
        return qLabels[0]

# Calculate style rankings
def getStyleRanks(answerList):
    styleTally = [[x, 0] for x in getShortStyle()]
    totalWeights = 0

    answerWeighting = {\
                "q1": {\
                    "1": {\
                        "edu": "2",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "2",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "3": {\
                        "edu": "0 ",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "2",\
                        "pro": "1"\
                    }\
                }, "q2": {\
                    "1": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "2": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "2",\
                        "pro": "0"\
                    }\
                }, "q3": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "2"\
                    }\
                }, "q4": {\
                    "1": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "3": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "1"\
                    }\
                }, "q5": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "2"\
                    }\
                }, "q6": {\
                    "1": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "2"\
                    }\
                }, "q7": {\
                    "1": {\
                        "edu": "2",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "2"\
                    }\
                }, "q8": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "2",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "2"\
                    }\
                }, "q9": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "2",\
                        "pro": "2"\
                    }\
                }, "q10": {\
                    "1": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "2": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "2",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }\
                }, "q11": {\
                    "1": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "2": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "2",\
                        "pro": "0"\
                    }, "4": {\
                        "edu": "2",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "5": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
                    }\
                }, "q12": {\
                    "1": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "3": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "1"\
                    }\
                }\
    }

    # Tally answers
    for i, key in enumerate(answerWeighting.keys()):
        for j, entry in enumerate(styleTally):
            weighting = int(answerWeighting[key][str(answerList[i])][entry[0]])
            styleTally[j][1] += weighting
            totalWeights += weighting

    # Convert to percentage & full styles
    styleList = getLongStyle()
    for i, entry in enumerate(styleTally):
        styleTally[i].append(styleList[i])
        entry[1] = int(round(entry[1]*100/totalWeights, 0))
        
    # Sort
    return sorted(styleTally, key=lambda x: x[1], reverse=True)

# CONTENT -> /style
# Get style desc
def getStyleInfo(styleName):
    styleInfo = {\
        'edu': {'title': convertShortToLong('edu'), 'adj': ['curious', 'questioning', 'perceptive'],\
            'desc': "As an Educator, you make an impact through the power of your knowledge. Educators are ready at a moment's notice to share resources and information related to reproductive rights. You could spread information about abortion access to friends in person, or you could spread that information virtually to your social media followers. "},\
        'emp': {'title': convertShortToLong('emp'), 'adj': ['compassionate', 'relatable', 'caring'],\
            'desc': "As an Empath, you make an impact through your compassion. Empaths help those seeking reproductive care, whether by lending a sympathetic ear or offering a ride to a local clinic. You could listen to stories of those who have had difficulty accessing an abortion or other reproductive care, or you could share stories, with permission, to inspire others to get involved."},\
        'org': {'title': convertShortToLong('org'), 'adj': ['creative', 'coordinated', 'strategic'],\
            'desc': "As an Organizer, you make an impact by working behind the scenes. Organizers ensure activist events related to reproductive rights, such as abortion access, are successful and run smoothly. You could start your own activism event for reproductive rights, or you could help existing organizers and events manage their events."},\
        'phi': {'title': convertShortToLong('phi'), 'adj': ['resourceful', 'generous', 'benevolent'],\
            'desc': "As a Philanthropist, you make an impact by providing resources. Philanthropists support reproductive rights by increasing the resources of abortion funds and other pro-choice organizations. You could donate money to activist organizations, clinics, and abortion funds, or you could offer resources such as venues for events."},\
        'pro': {'title': convertShortToLong('pro'), 'adj': ['fearless', 'passionate', 'confident'],\
            'desc': "As a Protestor, you make an impact by publicly advocating for reproductive rights. Protestors visibly share their opinions on reproductive rights like abortion access and ensure their voices are heard. You could attend local protests and marches to support issues like abortion access in your local community, or you could travel to larger protests to support the broader cause."}\
        }
    return styleInfo[styleName]

# Get intro text for a style
def getStyleIntro(styleName, quizStatus, styleRanks):
    styleIntro = {x: 'Your activism style could also be' for x in getShortStyle()}
    if quizStatus:
        for i, adj in enumerate(['primary', 'secondary', 'tertiary']):
            styleIntro[styleRanks[i]] = f'Your {adj} activism style is'
    else:
        for k in styleIntro.keys():
            styleIntro[k] = 'Your activism style could be'
    return styleIntro[styleName]

# Get carousel order for style page
def getStyleNav(styleName, quizStatus, styleRanks):
    if quizStatus:
        orderList = styleRanks
    else:
        orderList = getShortStyle() #alphabetical order
    
    currentIndex = orderList.index(styleName)
    navDict = {'current': currentIndex, 'prev': 'disabled', 'next': 'disabled'}
    
    if currentIndex != 0:
        navDict['prev'] = orderList[currentIndex - 1]
    if currentIndex != 4:
        navDict['next'] = orderList[currentIndex + 1]

    return navDict

# Calculate map desc orientation
def getMapOrient(posNum):
    if posNum in [1, 2, 5, 6, 9, 10]:
        return 'right'
    elif posNum in [3, 4, 7, 8, 11, 12]:
        return 'left'

# Get community map img positions
def getMapPos(styleName):
    posNum = {a: b for a, b in zip(getShortStyle(), [[1, 7, 10], [3, 5, 12], [1, 8], [4, 9], [2, 7, 9]])}
    posOrientList = []
    for num in posNum[styleName]:
        posOrientList.append([num, getMapOrient(num)])
    return posOrientList

# Get map desc text    
def getMapDesc(styleName):
    mapDescDict = {\
        'edu': \
            ['I created a social media page to share questions that concerned people can ask their local legislator',\
            'I shared my beliefs on abortion access to my social media followers',\
            "I educated the public as a speaker for a reproductive rights event"],\
        'emp': \
            ['I offer to give women rides to abortion clinics in or out of state',\
            "I listen to peoples' stories, so they have a space to share without being judged",\
            "I support abortion journeys by aiding abortion seekers as a volunteer"],\
        'org': \
            ["I made flyers to advertise a local bakery's fundraiser sale",\
            'I used my marketing experience to help a local advocacy organization recruit volunteers'],\
        'phi': \
            ['I donated to a local abortion fund to support women in my community',\
            'As a local business owner, I signed an open letter urging lawmakers to support access to abortion'],\

        'pro': \
            ["I attended a women's rights march to protest bodily autonomy being restricted",\
            'I help interview potential protest supporters to make sure they are trustworthy',\
            "I actively prevent pro-life supporters from harassing people going to Planned Parenthood"]
    }
    return mapDescDict[styleName]


# CONTENT -> /nextsteps
# Get content for next steps
def getNextSteps(stepType, styleName):
    eventInfo = {\
        'Informational Events': {\
            'edu': [('Educators', ' can share important news and local developments with attendees'), ('As an ', 'educator', ',you can be a vital part of conversations at informational events. By sharing important news and local developments with attendees, you can empower others to support reproductive rights in an informed, conscious manner.')],\
            'emp': [('Empaths', ' can listen to the stories of attendees and provide emotional support'), ('As an ', 'empath', ', you can be an important part of community building at informational events. By empathizing with attendees, listening to their stories, and providing emotional support, you can encourage others to share their experiences and be part of a safe, welcoming community.')],\
            'org': [('Organizers', ' can connect likeminded attendees and help them form groups'), ('As an ', 'organizer', ', you can have a big impact on community building at informational events. By connecting likeminded attendees with one another, you can help form powerful groups of local community members interested in reproductive rights activism.')],\
            'phi': [('Philanthropists', ' can encourage others to give by donating to the fundraiser'), ('As a ', 'philanthropist', ', you can be a crucial part of successful informational events. By publicly donating to fundraisers, you can encourage attendees to attend more events and to get more involved in reproductive rights activism, as well as giving event organizers the funds to create more events in the future.')],\
            'pro': [('Protestors', ' can be vocal pro-choice attendees that make others more comfortable'), ('As a ', 'protestor', ', you can make informational events more welcoming and comfortable for potential attendees. By attending and voicing about your pro-choice beliefs, you can make like-minded attendees more willing to share their beliefs and engage with their peers.')]},\
        'Letter Writing Events': {\
            'edu': [('Educators', ' can share information on notable local legislators'), ('As an ', 'educator', ', you can be a crucial part of letter writing events. By sharing important information on current reproductive rights legislation and the legislators responsible, you can help attendees decide the content and recipients of their letters.')],\
            'emp': [("Empaths", " can share stories they've heard to include in letters"), ("As an ", "empath", ", you can have a big impact on letter writing events. By sharing the powerful stories you've heard and have permission to share, you can give attendees persuasive, important stories to include in their letters.")],\
            'org': [('Organizers', ' can help attendees coordinate letter topics and recipients'), ('As an ', 'organizer', ', you can make letter writing events more coordinated and successful. Both helping attendees coordinate letter topics and recipients, you can help the event have a stronger impact on those legislators.')],\
            'phi': [('Philanthropists', ' can fund letter writing materials for virtual attendees'), ('As a ', 'philanthropist', ', you can be a vital part of letter writing events. Even for virtual events, you can fund letter writing materials, compensating attendees for stamps, paper, and other materials they bought for themselves.')],\
            'pro': [('Protestors', ' can explain how to be vocal and passionate about your beliefs in a letter'), ('As a ', 'protestor', ', you can be an important part of letter writing events. As someone comfortable sharing your beliefs publicly, you can help attendees do the same in their letters, helping them feel more comfortable writing to local legislators.')]},\
        'Protests & Marches': {\
            'edu': [('Educators', ' can share recent developments and news to encourage potential activists to attend'), ('As an ', 'educator', ', you can have a big impact on protests. By sharing recent legislative developments, you can encourage potential activists to attend and lend their voices to the cause.')],\
            'emp': [("Empaths", " can create a welcoming protest atmosphere by listening to attendees' experiences"), ("As an ", 'empath' ", you can make a protest more welcoming to potential activists. By listening to and empathizing with attendees' experiences, you can help them become more comfortable sharing their stories and protesting for reproductive rights.")],\
            'org': [('Organizers', ' can help manage the event and advertise it to the local activist community'), ('As an ', 'organizer', ', you can be a vital part of protests. By managing the different parts of the protest and advertising it to the local activist community, you can help the protest run smoothly and have a bigger impact on the fight for reproductive rights.')],\
            'phi': [('Philanthropists', ' can help fund event resources, advertisement, and security'), ('As a ', 'philanthropist', ', you can be an important part of protests. By contributing money and other resources, you can help fund security for protestors, advertisements for potential attendees, and other important elements of a successful protest.')],\
            'pro': [('Protestors', ' can be the vocal, passionate, and active part of the protest'), ('As a ', 'protestor', ', you can be a crucial part of protests. By attending and vocally supporting your beliefs, you make the protest and its values heard by those in your community, and inspire community members to support reproductive rights.')]}\
        }
    methodInfo = {\
        'edu': [\
            ('Organize your resources and information', ('As an ', 'educator', ', you are equipped to share important news and resources with community members. Keeping that news and resources organized will make sharing far easier.')),\
            ('Encourage people to get involved with activism', ('Anyone can be an activist. As an ', 'educator', ', you have the information to demonstrate that, and can use that information to encourage people to get involved.')),\
            ('Share important information however you can', ('As an ', 'educator', ', you have information that others lack. Finding ways to share that information, whether in-person or online, is a great way to support reproductive rights.'))],\
        'emp': [\
            ('Volunteer at local abortion clinics', ("As an ", "empath", ", you excel at listening to others' stories and validating their experiences. Volunteering at local clinics can give you an opportunity to do just that!")),\
            ('Join online support groups for abortion seekers', ('Abortion seekers need support from empathetic listeners. As an ', 'empath', ', you can provide the support they need during this difficult time.')),\
            ('Consider anonymously sharing your experiences', ("As an ", "empath", ", you aren't just good at listening to experiences: you're also great at sharing experiences. Consider sharing your own anonymously to inspire others to get involved!"))],\
        'org': [\
            ('Research local organizations to get involved with', ('As an ', 'organizer', ', you excel at managing complicated networks of people and resources. Local organizations focused on reproductive rights can benefit from your expertise!')),\
            ("Offer to support local businesses' activism work", ('Local businesses are often interested in supporting important causes like reproductive rights but may not be sure how to do so. As an ', 'organizer', ', you have the skills they need!')),\
            ('Get involved with the local protest community', ('Protests are an important part of fighting for reproductive rights. As an ', 'organizer', ', you have a lot of valuable management skills that can help create successful protests.'))],\
        'phi': [\
            ('Donate to abortion clinics in your area', ('Local abortion clinics need both money and resources to continue operating. As a ', 'philanthropist', ', you can donate the needed resources and empower the clinic to continue helping people in need.')),\
            ('Provide local activists with resources', ('Local activists need resources to create events that support reproductive rights. As a ', 'philanthropist', ', you can support their effort and community growth by contributing resources!')),\
            ('Research potential abortion funds to support', ('Beyond clinics, there are also funds that support abortion seekers. As a ', 'philanthropist', ', you can donate money to these funds and help abortion seekers in need.'))],\
        'pro': [\
            ('Publicly and vocally support your beliefs', ('As a ', 'protestor', ', you are more comfortable supporting reproductive rights publicly than others. By supporting publicly, you can inspire others to also support!')),\
            ('Attend protests and marches', ('As a ', 'protestor', ', your comfort with public support makes you a great fit for protests and marches. Attending these vents could be a great for you to support reproductive rights!')),\
            ('Encourage non-protestors to get involved', ("There are many paths to activism for reproductive rights besides protesting. As a ", "protestor", ", you are most often associated with activism—use this to encourage people to get involved as activists. Everyone's talents are welcome!"))]\
        }
    
    returnInfo = []

    if stepType == 'events':
        for key, value in eventInfo.items():
            styleList = getShortStyle()
            styleList.remove(styleName)
            returnInfo.append([key, value[styleName][1], [value[style][0] for style in styleList]])

    elif stepType == 'methods':
        returnInfo = methodInfo[styleName]

    return returnInfo

# Get intro blurb for next steps
def getNextStepsIntro(stepType, styleName):
    indefArticle = None
    if styleName in ['phi', 'pro']:
        indefArticle = 'a'
    else:
        indefArticle = 'an'
    
    actionPhrase = None
    if stepType == 'events':
        actionPhrase = 'to contribute to activism events'
    else:
        actionPhrase = 'to get more involved in activism'

    return f'How {actionPhrase} as {indefArticle} {convertShortToLong(styleName)}:'

# CONTENT -> /about-us
def getTeamInfo():
    teamInfo = [\
        ['ash', 'Aswati Panicker', 'Ph.D. Health Informatics', 'Indiana University | May 2025'],\
        ['colin', 'Colin LeFevre', 'B.S. Informatics', 'Indiana University | May 2024'],\
        ['forum', 'Forum Modi', 'Ph.D. Health Informatics', 'Indiana University | May 2027'],\
        ['nikhil', 'Nikhil Dinesh', 'M.S. Human Computer Interaction & Design', 'Indiana University | May 2023'],\
        ['sitha', 'Sitha Vallabhaneni', 'M.S. Human Computer Interaction & Design', 'Indiana University | May 2023']\
    ]
    return teamInfo