import copy

candidate_nomination = True
candidate_list = []
voterlist=[]
voter_registering = True

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while (voter_registering):
    print("Any new registering voters?")
    new_voter = input()
    if new_voter.isalpha(): 
        if new_voter.lower() == 'no' or 'n' or 'end':
            voter_registering = False
    if is_number(new_voter):
        voterlist.append(new_voter)
while (candidate_nomination):
    print("List all candidates")
    new_candidate = input()
    candidate_filtered = ''.join(c for c in new_candidate if c.isalpha())
    if candidate_filtered.lower() == "end":
        candidate_nomination = False
    else:
        candidate_list.append(new_candidate)
candidate_uncertain = True
while (candidate_uncertain):
    for i in range(len(candidate_list)):
        print(candidate_list[i])
    print("Would you like to confirm these candidates? Y/N")
    user_satisfied = input()
    user_satisfied = ''.join(c for c in user_satisfied if c.isalpha()).lower()
    if user_satisfied == "y":
        candidate_uncertain = False
    else:
        print("Which candidate would you like to change?")
        changed_candidate = input()
        new_changed_candidate = ''.join(c for c in changed_candidate if c.isalpha())
        print("Changed or removed?")
        change_undone = True
        candidate_fate = ''.join(c for c in input() if c.isalpha()).lower()
        if candidate_fate == "removed":
            for i in range(len(candidate_list)):
                if candidate_list[i] == new_changed_candidate:
                    candidate_list.pop(i)
                    change_undone = False
                    break
        if candidate_fate == "changed":
            print("What would you like it changed to?")
            new_candidate = input()
            for i in range(len(candidate_list)):
                if candidate_list[i] == new_changed_candidate:
                    candidate_list[i] = new_candidate
                    break
dictionary_votes = {}
for i in voterlist:
    dictionary_votes[i]={}
    for j in candidate_list:        
        dictionary_votes[i][j]={}
        for x in range(len(candidate_list)):
            dictionary_votes[i][j][x]=0
for i in range(len(voterlist)):
    print("Can you please provide your voter id?")
    voter_id = input()
    if voter_id in voterlist:
        mutable_candidate_list= copy.copy(candidate_list)
        for j in range(len(mutable_candidate_list)):
            voter_certain = True
            for z in range(len(mutable_candidate_list)):
                print("[ ]", mutable_candidate_list[z])
            while(voter_certain):
                print("Who is your #", j+1, " pick?")
                if len(mutable_candidate_list)==0:
                    voter_certain= False
                for k in range(len(mutable_candidate_list)):
                    pick = input()
                    pick_location = 0
                    pick = ''.join(c for c in pick if c.isalpha())
                    print("Would you like to confirm this candidate? Y/N, then display your next choice")
                    for l in range(len(mutable_candidate_list)):
                        if mutable_candidate_list[l]== pick:
                            print("[x]", mutable_candidate_list[l])
                        else:
                            print("[ ]",mutable_candidate_list[l])
                    decision = input().upper()
                    if decision == "Y":
                        for m in range(len(mutable_candidate_list)):
                            dictionary_votes[voter_id][pick][j]+=1    #There is a KeyError here doesn't allow for either yes or no    
                            if pick in mutable_candidate_list:
                                mutable_candidate_list.remove(pick)
                                voter_certain = False
                    else:
                        continue
                else:
                    continue
            else:
                continue
    else:
        print("Contact administrator, since you haven't registered")
def requiredvotes(candidates):
    requiredpercentage = 100/int(candidates)
    requiredvotes = requiredpercentage*len(voterlist)/100
    return requiredvotes
print("How many winners are there?")
winners = input()
minimum_votes = requiredvotes(winners)
for i in voterlist:
    over_minimum[i]=0
over_minimum = {voterlist}
for i in range(voterlist):
    over_minimum[i] = {voterlist[i]:0}
winners_list = []
polls=candidate_list
def votes_for_candidate(k,l):
    total_votes = 0
    for j in voterlist:
        temp = dictionary_votes[j][k][l]
        if int(temp)>minimum_votes:
            over_minimum[j]= int(temp)-minimum_votes
            winners_list.append(k)
        total_votes+=dictionary_votes[j][k][l]
    return total_votes
stage =0
def lowest_candidate(l):
    lowest_candidate=''
    lowest_candidate_votes = 100
    person_who_loses = ''
    for j in voterlist:
        for k in candidate_list:
            print(k)
            lowest_candidate = dictionary_votes[j][k][l]
            print(lowest_candidate)
            if lowest_candidate<lowest_candidate_votes:
                lowest_candidate_votes = dictionary_votes[j][k][l]
                person_who_loses_temp = dictionary_votes[j][k]
                person_who_loses = list(dictionary_votes[j].keys())[list(dictionary_votes[j].values()).index(person_who_loses_temp)]
                stage+=1
                return lowest_candidate,person_who_loses
def allocate_votes(candidate,stage):
    voter_allocation = []
    for z in voterlist:
        if dictionary_votes[z][candidate][stage]==1:
            voter_allocation.append(z)
            dictionary_votes[z][candidate][stage]-=1
    for j in candidate_list:
        for l in voter_allocation:
            if dictionary_votes[0][j][stage-1] ==1:
                dictionary_votes[0][j][stage]+=1
votes = 0
while(len(winners_list)<winners):
    for i in range(len(candidate_list)):
        votes_for_candidates(candidate_list[i],stage)
    low=lowest_candidate(stage)
    allocate_votes(low,stage)
print(winners_list)
