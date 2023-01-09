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
        ['edu', convertShortToLong('edu'), "Curious, questioning, and perceptive, a voice of clarity on abortion access."],\
        ['emp', convertShortToLong('emp'), "Compassionate, relatable, and caring, a helping hand for abortion seekers."],\
        ['org', convertShortToLong('org'), "Creative, coordinated, and strategic, the behind-the-scenes hero of activist events."],\
        ['phi', convertShortToLong('phi'), "Resourceful, generous, and benevolent, a benefactor of abortion activists."],\
        ['pro', convertShortToLong('pro'), "Fearless, passionate, and confident, a front line champion for abortion access."]\
    ]
    return styleBlurbs

# CONTENT -> /quiz
# Get question text for Q1-12
def getQDesc(qNum):
    qDescs = [\
        (1, "educate people on controversial issues"), \
        (1, "take a stand on causes important to you"), \
        (1, "plan support out of the public view"), \
        (1, "donate money or other resources to causes important to you"), \
        (1, "help people one-on-one"), \
        (2, "your privacy and/or anonymity"), \
        (2, "your time constraints"), \
        (2, "interactions with people who disagree with your activism"), \
        (2, "judgment from your peers and/or family about your activism"), \
        (3, "donate money"), \
        (3, "donate your time or supplies/resources"), \
        (3, "share information to the public or other activists")\
    ]
    return f'As an activist, you would {qDescVerb(qDescs[qNum-1][0])} {qDescs[qNum-1][1]}.'

def qDescVerb(prefixNum):
    if prefixNum == 1:
        return 'like to'
    elif prefixNum == 2:
        return 'be worried about'
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
                        "pro": "1"\
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
                        "pro": "1"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "4": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
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
                        "phi": "1",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "2",\
                        "pro": "0"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "2"\
                    }\
                }, "q4": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }\
                }, "q5": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "0"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "1"\
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
                        "pro": "0"\
                    }, "3": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
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
                        "emp": "1",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "3": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
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
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "3": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "2"\
                    }\
                }, "q9": {\
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
                        "pro": "0"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "2",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "2"\
                    }\
                }, "q10": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "2",\
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
                        "edu": "1",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }\
                }, "q11": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "2"\
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
                        "phi": "2",\
                        "pro": "0"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "5": {\
                        "edu": "0",\
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
                        "pro": "1"\
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
                        "phi": "2",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
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
            'desc': ["As an Educator, you make an impact through the power of your knowledge. Educators are ready at a moment's notice to share resources and information related to reproductive rights.", "By spreading information about abortion access, either in person or virtually, you educate people about their ability to access abortion and raise awareness about reproductive rights."]},\
        'emp': {'title': convertShortToLong('emp'), 'adj': ['compassionate', 'relatable', 'caring'],\
            'desc': ["As an Empath, you make an impact through your compassion. Empaths help those seeking abortions, whether by lending a sympathetic ear or offering a ride to a local clinic.", "By listening to and helping people one-one-one, you know powerful stories about people’s abortion experiences and, with permission, can share these stories to get others involved."]},\
        'org': {'title': convertShortToLong('org'), 'adj': ['creative', 'coordinated', 'strategic'],\
            'desc': ["As an Organizer, you make an impact by working behind the scenes. Organizers ensure activist events related to reproductive rights, such as abortion access, are successful and run smoothly.", "By starting your own events for abortion access or helping existing organizers and events, you bring together activists and empower them to fight for access to abortion."]},\
        'phi': {'title': convertShortToLong('phi'), 'adj': ['resourceful', 'generous', 'benevolent'],\
            'desc': ["As a Philanthropist, you make an impact by providing resources. Philanthropists support reproductive rights by increasing the resources of abortion funds and other pro-choice organizations.", "By donating money and/or other resources to activist organizations, clinics, and abortion funds, you support access to abortion and activism for reproductive rights."]},\
        'pro': {'title': convertShortToLong('pro'), 'adj': ['fearless', 'passionate', 'confident'],\
            'desc': ["As a Protestor, you make an impact by publicly advocating for reproductive rights. Protestors visibly share their opinions on reproductive rights like abortion access and ensure their voices are heard.", "By attending protests and marches to support abortion access, you voice the concerns and opinions of many other activists and help work towards better access to abortion for all."]}\
        }
    return styleInfo[styleName]

# Get intro text for a style
def getStyleIntro(styleName, quizStatus, styleRanks, stylePerc):
    returnStr = ''
    if quizStatus:
        adjList = ['primary', 'secondary', 'tertiary']
        indexNum = int(styleRanks.index(styleName))
        if 0 <= indexNum <= 2:
            returnStr = f'Your {adjList[indexNum]} activism style ({stylePerc[indexNum]}%) is'
        elif 3<= indexNum <= 4:
            returnStr = f'Your activism style ({stylePerc[indexNum]}%) could also be'
    else:
        returnStr = 'Your activism style could be'
    return returnStr

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
            'I offered my local business as a venue for a pro-choice fundraiser'],\

        'pro': \
            ["I attended a women's rights march to protest bodily autonomy being restricted",\
            'I help interview potential protest supporters to make sure they are trustworthy',\
            "I actively prevent pro-life supporters from harassing people going to Planned Parenthood"]
    }
    return mapDescDict[styleName]

# Get 'Get Involved' recs for a style
def getInvolved(styleName):
    styleInvolveDict = {\
        'edu': [\
            # Suggestion 1
            {'preview': [\
                "Explain recent legal developments on abortion access",\
                "As of late 2022, the legal status of abortion varies by state and legislative changes. As an educator, you can explain recent developments and keep people informed."\
            ], 'info': [\
                ("How can I keep track of legal developments to share with others?", "It's important to have a list, either physical or mental, of trustworthy news outlets. Once you have this list, you can periodically check recent articles, particularly on the issue of abortion, to learn about developments. This will also help provide sources for anyone who asks."),\
                ("Who should I explain legal developments to?", "You can explain legal developments to anyone who you think could benefit from knowing the information and who you are comfortable discussing access to abortion with. Reproductive rights affect everyone, and so anyone could benefit from accurate information on abortion's legality in their location!")\
            ]},\
            # Suggestion 2
            {'preview': [\
                "Post educational content online",\
                "As an educator, you are equipped to share accurate, pertinent information on abortion access. Sharing this information can help people stay informed on the topic and raise awareness about access to abortion."\
            ], 'info': [\
                ("What content should I be posting online?", "There's a lot of helpful information related to abortion: how to get access to a pregnancy test, where to go for an abortion, etc. So long as the information could potentially help seeking abortion seeker, sharing that information is a helpful and valid form of activism."),\
                ("Where should I post the content online?", "You could post the content on your social media of choice, or on a different platform that feels more relevant. Wherever you choose to post, it's also helpful to think about whether or not you'd like to remain anonymous beforehand.")\
            ]}],      
        'emp': [\
            # Suggestion 1
            {'preview': [\
                "Join online support communities for abortion seekers",\
                "Abortion seekers need support from empathetic listeners, and often search for that support online. As an empath, you can join online support communities and provide the support they need during this difficult time."\
            ], 'info': [\
                ("How can I find online support communities to join?", "Online support communities exist across many different social media platforms. Two particularly common platforms are Facebook and Reddit. You could either search for Facebook and Reddit communities you'd like to join and provide support through, or look for communities on a different social media that you prefer."),\
                ("What are some online support communities for Bloomington specifically?", "There aren't many public-facing support communities for abortion seekers in Bloomington specifically. Some broader groups, such as the r/Bloomington subreddit, are vocally pro-choice. You could either join broader groups like these or look for support communities not focused on Bloomington specifically."),\
                ("What will I do as a community member?", "As a member of an online support community for abortion seeker, your primary task is to be available. Members looking for an empathetic ear don't post at regularly scheduled intervals—they post when they most need support. So, set aside some time to be available and read through recent community posts.")\
            ]},\
            #Suggestion 2
            {'preview': [\
                "Volunteer at local abortion clinics",\
                "As an empath, you excel at listening to others' stories and validating their experiences. Volunteering at local clinics can give you an opportunity to help people one-on-one and support vulnerable community members."\
            ], 'info': [\
                ("How can I find abortion clinics to volunteer at?", "You can look for potential abortion clinics to volunteer at by using websites such as ProChoice.org or AbortionFinder.org. You could also use search engines, e.g., Google, to look for clinics in specific towns or other pro-choice organizations looking for volunteers. Be sure to distinguish between pro-choice¬ and pro-life clinics. Pro-life clinic, also known as women's health centers, often use similar language to their pro-choice counterparts but do not support access to abortion."),\
                ("Where can I volunteer in Bloomington?", "If you're wanting to volunteer in Bloomington, IN specifically, two options are: Planned Parenthood, a pro-choice abortion clinic, or All-Options, a pro-choice organization supporting abortion seekers"),\
                ("What will I do as a volunteer?", "Volunteers' roles and responsibilities vary, based on an individual clinic's current needs. Some common volunteer activities are escorting patients, entering data, assisting with education programs. If you have a specific role in mind, you can always contact the clinic and ask!")\
            ]}],\
        'org': [\
            # Suggestion 1
            {'preview': [\
                "Volunteer to help organize existing events",\
                "Existing events are an important part of fighting for reproductive rights. As an organizer, you have valuable management skills that can help these events be successful."\
            ], 'info': [\
                ("How can I find existing events?", "Where to find will on the location and organization. Broadly, online search engines, e.g., Google, can help you find you events in an area you are familiar with. Alternatively, if you're familiar with the area, you could look at in-person billboards and contact organizations you are aware of."),\
                ("Are there any events to help with in Bloomington?", "Many of the larger scale protests occur in Indianapolis, not Bloomington. But there are many small events, such as fundraisers or letter writing, that happen in Bloomington successfully. There isn't one overarching organizer for all these events, so you'll need to look event by event."),\
                ("How exactly can I help organize these events?", "There are many valuable skills you could bring to managing an event. You could create fliers to advertise the event, secure a venue for the event, find potential donors to fund the event, etc.")\
            ]},\
            #Suggestion 2
            {'preview': [\
                "Organize new pro-choice events to support abortion access",\
                "As an organizer, you can also create new events that support access to abortion. From fundraisers to protests, there are a wide variety of ways you can create a supportive event."\
            ], 'info': [\
                ("What kind of event should I create?", "The type of event you create usually corresponds to the impact you want to have. Trying to donate money to an abortion clinic? Hold a fundraiser! Want to raise awareness about abortion access? Have a protest or a march!  Worried about upcoming legislative? Create a letter writing event targeting local legislators."),\
                ("How will I get the resources in Bloomington to fund the event?", "Getting resources to fund an event is difficult, and there is no easy answer. But, many Bloomington residents are passionate about supporting abortion access. So, a good starting point is connecting with likeminded advocates, pooling your resources, and decided what type of event those resources would allow you to host."),\
                ("Where in Bloomington can I host the event?", "You could host an event in a public area, or rent a venue. Another option specifically for Bloomington is contacting local business owners. Several Bloomington businesses have previously hosted pro-choice events like fundraisers. Try to target businesses that explicitly self-describe as women owned, pro-choice, and/or LGBTQIA+ affirming.")\
            ]}],\
        'phi': [\
            # Suggestion 1
            {'preview': [\
                "Donate to abortion clinics and pro-choice organizations",\
                "Local abortion clinics and pro-choice organizations need both money and resources to continue operating. As a philanthropist, you can donate the needed resources and empower the clinic to continue helping people in need."\
            ], 'info': [\
                ("How do I find clinics and organizations to support?", "Using online resources like ProChoice.org or AbortionFinder.org can help you verified clinics to donate to. Organizations can be more difficult to find. You can use search engines, e.g., Google, to find organizations and their related events. Based on the information available, you'll have to make a decision on whether you can trust them with your resources."),\
                ("What kind of resources should I donate?", "What resources are needed will depend on the specific clinic and its needs. Generally, monetary donations are always welcomes; if there are other resources you would like to donate, you can contact the clinic or organization and inquire if they would accept that donation."),\
                ("Where in Bloomington can I donate?", "If you're wanting to donate to Bloomington organization specifically, two options are: Planned Parenthood, a pro-choice abortion clinic, or All-Options, a pro-choice organization supporting abortion seekers.")\
            ]},\
            #Suggestion 2
            {'preview': [\
                "Provide local activists with resources",\
                "Local activists who are passionate about supporting abortion access need resources to do so. Providing them those resources is another way you, as a philanthropist, can contribute to reproductive rights activism."\
            ], 'info': [\
                ("How do I find activists to support?", "Finding likeminded, trustworthy activists to support can be difficult, and there is no one way to do so. Broadly, talk to local friends and/or acquaintances of yours to get a better idea of who else is passionate about supporting abortion access, and how you could possibly support them."),\
                ("What kind of resources do activists need?", "The type of resources needed will depend on the activist. Protestors might need funds to travel to a march, whereas Organizers might need to a venue. Once you have found activists to support, work with them to understand how you can best support their unique needs.")\
            ]}],\
        'pro': [\
            # Suggestion 1
            {'preview': [\
                "Attend protests and marches",\
                "As a protestor, your comfort with public support makes you a great fit for protests and marches. Attending these events can be a great way for you to support reproductive rights!"\
            ], 'info': [\
                ("How do I find protests/marches to attend?", "Contacting local organizations or searching online, e.g., with Google, can be good ways to identify upcoming protests and marches. Be sure to research the organizers and their security measures before attending to protect yourself."),\
                ("Are there any protests/marches in Bloomington?", "Most protests and marches usually happen in Indianapolis, not Bloomington. But it is still possible for a protest or march to occur in Bloomington! Keep an eye on local Bloomington social media groups, e.g., r/Bloomington subreddit, more any discussion of protests."),\
                ("What do I do at protests/marches?", "There are many different ways to protests. Some protestors prefer to yell slogans; others wave signs; and others just stand in solidarity. What precisely you do at protests and marches will depend on what you feel comfortable doing—protest in whatever way works for you!")\
            ]},\
            #Suggestion 2
            {'preview': [\
                "Share your beliefs on abortion access",\
                "As a protestor, you are more comfortable taking a public stance on controversial stance than others. By sharing your beliefs, you raise awareness and encourage others less willing to share to nonetheless get involved."\
            ], 'info': [\
                ("What beliefs should I share?", "Any strongly held convictions on abortion access, reproductive rights, or other pro-choice issues would be helpful to share. If something feels relevant for others to know about post-Roe v. Wade, definitely share that!"),\
                ("How should I share my beliefs, and with whom?", "You can share your beliefs however and with whomever you would like.  Whether you’re sharing on Instagram or at family dinner, with lifelong friends or work acquaintances, sharing your beliefs will be a powerful statement. Share where you feel most comfortable doing so.")\
            ]}]\
        }

    return styleInvolveDict[styleName]

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
