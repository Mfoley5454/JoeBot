#Generates very basic language model
#Will later handle sentence generation once that point comes
#TODO May want to make some specifications on when a '.' appears


def createUnigrams(dataString):
    unigrams = dataString.split()
    return unigrams


def createBigrams(dataString):
    unigramData = dataString.split()
    bigramList = []
    isFirstWord = True
    firstWord = unigramData[0]
    prev = ""
    for word in unigramData:
        if ((word == firstWord) and (isFirstWord == True)):
            isFirstWord = False
            prev = word
        else:
            bigram = [prev, word]
            bigramList.append(bigram)
            prev = word
    return bigramList

def createTrigrams(dataString):
    unigramData = dataString.split()
    trigramList = []
    isFirstWord = True
    isSecondWord = False
    firstWord = unigramData[0]
    secondWord = unigramData[1]
    oneStep = ""
    twoStep = ""
    for word in unigramData:
        if((word == firstWord) and (isFirstWord == True)):
            twoStep = word
            isFirstWord = False
            isSecondWord = True
        elif((word == secondWord) and (isSecondWord == True)):
            oneStep = word
            isSecondWord = False
        else:
            trigram = [twoStep, oneStep, word]
            twoStep = oneStep
            oneStep = word
            trigramList.append(trigram)
    return trigramList
