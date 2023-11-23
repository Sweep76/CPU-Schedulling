import copy


def LRU(pageReplacementAlgorithm, pageReferences, numberOfFrames):
    print(pageReplacementAlgorithm)
    print(pageReferences)
    print(numberOfFrames)

    numberOfFrames = int(numberOfFrames)
    frames = [[] for _ in range(numberOfFrames)]
    hitOrFault = []

    blankCount = 0
    nonBlankCount = numberOfFrames

    for x in range(numberOfFrames):
        currentPage = pageReferences[x]
        # copy the first few pages directly into the storage
        for _ in range(blankCount):
            frames[x].append("_")

        for _ in range(nonBlankCount):
            frames[x].append(currentPage)

        blankCount += 1
        nonBlankCount -= 1
        hitOrFault.append("F")

    framesDetails = {"frames": frames, "hitOrFault": hitOrFault, "remark": "None."}

    framesDetailsSet = []
    framesDetailsSet.append(framesDetails)

    for y in range(numberOfFrames, len(pageReferences)):
        frames = copy.deepcopy(frames)
        hitOrFault = copy.deepcopy(hitOrFault)
        currentPage = pageReferences[y]
        doesExist = False

        # check if the page exists
        existingPages = []
        for z in range(numberOfFrames):
            if frames[z][-1] == currentPage:
                doesExist = True
            # append the frames with the latest pages. if it is a fault, the appropriate page will be replaced later
            frames[z].append(frames[z][-1])
            existingPages.append(frames[z][-1])

        if not doesExist:
            # currentPage does not exist, so it is a fault
            visitedPages = []
            trav = y - 1
            while trav >= 0 and len(visitedPages) != len(existingPages):
                page = pageReferences[trav]
                if not page in visitedPages and page in existingPages:
                    visitedPages.append(page)
                trav -= 1

            # the last value of visitedPages[] is the least recently used
            # since the values of frames[] appear in the same order as the values of existingPages[], .index() can be used on existingPages to determine the frames[] row index of the desired value
            indexReplace = existingPages.index(visitedPages[-1])

            hitOrFault.append("F")
            remark = f"{frames[indexReplace][-1]} replaced by {currentPage}."
            # replace the number replaced by the algorithm
            frames[indexReplace][-1] = currentPage
        else:
            # currentPage exists in either of the frames, so it is a hit
            hitOrFault.append("H")
            remark = "None"

        framesDetails = {"frames": frames, "hitOrFault": hitOrFault, "remark": remark}
        framesDetailsSet.append(framesDetails)

        # calculate hits and faults
        numberOfHits = hitOrFault.count("H")
        numberOfFaults = hitOrFault.count("F")
        hitsPercentage = numberOfHits / len(pageReferences) * 100
        faultsPercentage = numberOfFaults / len(pageReferences) * 100

        statistics = {
            "numberOfHits": numberOfHits,
            "numberOfFaults": numberOfFaults,
            "hitsPercentage": hitsPercentage,
            "faultsPercentage": faultsPercentage,
        }

    print(framesDetailsSet)
    print(statistics)

    return framesDetailsSet, statistics

    # for frames[x]

    # else:
    #   # implement the FIFO algo
    #   # check if currentPage exists
