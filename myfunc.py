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
def getStyles(answerList):
    styleTally = [['edu', 0], ['emp', 0], ['org', 0], ['phi', 0], ['pro', 0]]
    totalWeights = 0

    answerWeighting = {\
                "q1": {\
                    "1": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
                    }\
                }, "q2": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "2"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "0"\
                    }\
                }, "q3": {\
                    "1": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "2",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }\
                }, "q4": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "2"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "0"\
                    }\
                }, "q5": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }\
                }, "q6": {\
                    "1": {\
                        "edu": "0",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "2",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }\
                }, "q7": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "2",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "1"\
                    }\
                }, "q8": {\
                    "1": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "2",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "3": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }\
                }, "q9": {\
                    "1": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "2",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }\
                }, "q10": {\
                    "1": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "0"\
                    }\
                }, "q11": {\
                    "1": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "1",\
                        "phi": "2",\
                        "pro": "0"\
                    }, "2": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "4": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "5": {\
                        "edu": "1",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "0"\
                    }\
                }, "q12": {\
                    "1": {\
                        "edu": "2",\
                        "emp": "1",\
                        "org": "0",\
                        "phi": "0",\
                        "pro": "1"\
                    }, "2": {\
                        "edu": "2",\
                        "emp": "2",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "2"\
                    }, "3": {\
                        "edu": "1",\
                        "emp": "1",\
                        "org": "2",\
                        "phi": "2",\
                        "pro": "1"\
                    }, "4": {\
                        "edu": "0",\
                        "emp": "1",\
                        "org": "1",\
                        "phi": "1",\
                        "pro": "0"\
                    }, "5": {\
                        "edu": "0",\
                        "emp": "0",\
                        "org": "0",\
                        "phi": "0",\
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
    styleList = ["Educator", "Empath", "Organizer", "Philanthropist", "Protestor"]
    for i, entry in enumerate(styleTally):
        styleTally[i].append(styleList[i])
        entry[1] = int(round(entry[1]*100/totalWeights, 0))
        
    # Sort
    return sorted(styleTally, key=lambda x: x[1], reverse=True)