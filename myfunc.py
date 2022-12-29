# CONTENT -> /quiz
# Get question text for Q1-12
def getQDesc(qNum):
    qDescs = ["As an advocate, you would like to explain complicated issues.", "As an advocate, you would like to publicly support important causes.", "As an advocate, you would like to plan support behind-the-scenes.", "As an advocate, you would like to provide resources to other advocates.", "As an advocate, you would like to help people 1-on-1.", "As an advocate, you would be worried about your privacy and/or anonymity.", "As an advocate, you would be worried about your time restraints.", "As an advocate, you would be worried about retaliation from people who disagree with your beliefs.", "As an advocate, you would be worried about judgement from peers and/or family.", "As an advocate, how difficult is it for you to donate money?", "As an advocate, how difficult is it for you to donate resources?", "As an advocate, how difficult is it for you to share information?"]
    return qDescs[qNum-1]

# Get likert scale labels
def getQLabels(qNum):
    qLabels = [["strongly agree", "agree", "neutral", "disagree", "strongly disagree"], ["very easy","easy","neutral","hard","very hard"]]
    if 1 <= qNum <= 9:
        return qLabels[0]
    elif 10 <= qNum <= 12:
        return qLabels[1]

# Calculate style rankings
def getStyleRanks(answerList):
    styleTally = [['edu', 0], ['emp', 0], ['org', 0], ['phi', 0], ['pro', 0]]
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
    styleList = ["Educator", "Empath", "Organizer", "Philanthropist", "Protestor"]
    for i, entry in enumerate(styleTally):
        styleTally[i].append(styleList[i])
        entry[1] = int(round(entry[1]*100/totalWeights, 0))
        
    # Sort
    return sorted(styleTally, key=lambda x: x[1], reverse=True)

# CONTENT -> /style
# Get style desc
def getStyleInfo(styleName):
    styleInfo = {\
        'edu': {'title': 'Educator', 'adj': ['curious', 'questioning', 'perceptive'],\
            'desc': 'You make an impact through the power of your knowledge. You spread information about abortion access either in person or on social media. Educators are ready at a moments notice to share resources and information related to abortion access to their followers or those around them!'},\
        'emp': {'title': 'Empath', 'adj': ['compassionate', 'relatable', 'caring'],\
            'desc': 'You make an impact through your compassion by listening to stories of those who have experiences with abortion access. You are able to share what you have heard to spread awareness. Empaths are always ready to help those around them whether it is lending an ear to listen or a ride to a local clinic.'},\
        'org': {'title': 'Organizer', 'adj': ['creative', 'coordinated', 'strategic'],\
            'desc': 'You make an impact through by working behind the scenes in supporting pro-choice efforts. You may attend virtual events or help plan in-person events by creating fliers or finding other ways to spread the word. Organizers ensure virtual or in-person events related to abortion access are effective and run smoothly.'},\
        'phi': {'title': 'Philanthropist', 'adj': ['resourceful', 'generous', 'benevolent'],\
            'desc': 'You make an impact by providing financial support or resources to abortion access efforts. You make a difference by giving resources to organizations that provide and increase abortion access. Philanthropists are powerful in increasing the resources of abortion funds and other pro-choice organizations.'},\
        'pro': {'title': 'Protestor', 'adj': ['fearless', 'passionate', 'confident'],\
            'desc': 'You make an impact by showing up at protests and pro-choice other events to show your support for abortion access. You are willing to physically show up to show your support by traveling to larger cities or going to local events. Protestors visibly share their opinions on abortion access and ensure their voices are heard.'}\
        }
    return styleInfo[styleName]

# Get intro text for a style
def getStyleIntro(styleName, quizStatus, topThree):
    styleIntro = {x: 'Your advocacy style could also be' for x in ['edu', 'emp', 'org', 'phi', 'pro']}
    if quizStatus:
        for i, adj in enumerate(['primary', 'secondary', 'tertiary']):
            styleIntro[topThree[i]] = f'Your {adj} advocacy style is'
    else:
        for k in styleIntro.keys():
            styleIntro[k] = 'Your advocacy style could be'
    return styleIntro[styleName]

# Calculate map desc orientation
def getMapOrient(posNum):
    if posNum in [1, 2, 5, 6, 9, 10]:
        return 'right'
    elif posNum in [3, 4, 7, 8, 11, 12]:
        return 'left'

# Get community map img positions
def getMapPos(styleName):
    posNum = {\
        'edu': [4, 10],\
        'emp': [4, 6],\
        'org': [1, 8],\
        'phi': [4, 9],\
        'pro': [4, 6],
    }

    posOrientList = []
    for num in posNum[styleName]:
        posOrientList.append([num, getMapOrient(num)])
    return posOrientList

# Get map desc text    
def getMapDesc(styleName):
    mapDescDict = {\
        'edu': \
            ['I created a social media page to share questions that concerned people can ask their local legislator',\
            'I shared my beliefs on abortion access to my social media followers'],\
        'emp': \
            ['I offer to give women rides to abortion clinics in or out of state.',\
            'I listen to peoples’ stories, so they have a space to share without being judged.'],\
        'org': \
            ['I made flyers to advertise a local bakery’s fundraiser sale.',\
            'I used my marketing experience to help a local advocacy organization recruit volunteers.'],\
        'phi': \
            ['I donated to a local abortion fund to support women in my community.',\
            'As a local business owner, I signed an open letter urging lawmakers to support access to abortion.'],\

        'pro': \
            ['I attended a women’s rights march to protest women’s bodies being restricted.',\
            'I help interview potential protest supporters to make sure they are trustworthy.']
    }
    return mapDescDict[styleName]