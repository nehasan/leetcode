'''
Author: Nahid Hasan Khan
A driver file to parse UCL multiple match scores, aggregate them and \
    finally output the sorted-aggregated scores
The file utilizes popular HeapSort algorithm to pick the top scorer
'''
import string
import re
from typing import Dict, List
# from heapq import heapify, heappush, heappop

'''
Class: MyHeap
A custom written heap algorithm that sorts data comes in a hashtable
'''
class MyHeap:
    def __init__(self) -> None:
        # Initialize the self heap data
        self.heap = []


    def sort(self, input: Dict) -> List:
        '''
        Returns list of sorted tuples
        Arguments:
        input - input data, must be dict
        '''

        # Convert the hash data into a list
        self.heap = list(input.items())
        _sorted = []

        # Until the heap is empty keep heapifying and popping the top most value
        while self.heap:
            self.heapiFy()
            # Insert the top value to a new list which is a final result
            _sorted.append(self.heapPop())
        
        # print(f'--- DEBUG final sorted tuples: {_sorted}')
        return _sorted


    def heapiFy(self) -> None:
        '''
        Heapifies the internal self.heap data (list)
        Returns None
        Arguments None
        '''
        
        def swap(idx1, idx2) -> None:
            '''
            Swaps two values of the internal self.heap based on two indices
            Returns None
            Arguments:
            idx1 - first index, must be int
            idx2 - second index, must be int
            '''
            temp = self.heap[idx1]
            self.heap[idx1] = self.heap[idx2]
            self.heap[idx2] = temp


        # Popular heapify algorithm that identifies parent: heap[i] and \
        #   two children leftChild: heap[2 * i + 1], rightChild: heap[2 * i + 2] // 0 index based
        # Theory: Parent node should be greater than child nodes // in case max-heap and vice versa
        for i in range(len(self.heap)):
            parent = self.heap[i]
            lChild = () if ((2 * i + 1)) > (len(self.heap) - 1) else self.heap[(2 * i) + 1]
            rChild = () if ((2 * i + 2)) > (len(self.heap) - 2) else self.heap[(2 * i) + 2]

            # Swap the parent and left child node if parent is less and keep heapifying until all the nodes are done
            if lChild and parent[1] < lChild[1]:
                swap(i, (2 * i) + 1)
                self.heapiFy()
            
            # Swap the parent and right child node if parent is less and keep heapifying until all the nodes are done
            if rChild and parent[1] < rChild[1]:
                swap(i, (2 * i) + 2)
                self.heapiFy()
        
        # print(f'--- DEBUG heap after heapify: {self.heap}')


    def heapPop(self) -> List:
        '''
        Pops the first element of the heap list
        Returns None
        Arguments None
        '''
        # Theory is, after heapifying we pop the first element from the heap \
        #   place the last element to the top and heapify again to re-build the scrumbled heap
        temp = self.heap[0]
        # Place the last element to the top of the heap
        self.heap[0] = self.heap[-1]
        # Remove the last element from the entire heap data
        self.heap = self.heap[-(len(self.heap)) : -1]

        return temp
        

'''
Class: TeamScore
This class processes several multiple UCL match scores \
    aggregates the scores for individual team and finally \
    outputs the scores in a sorted way
'''
class TeamScore:

    def parseTeamScore(self, scores: string=[]) -> List:
        '''
        Returns parsed and sorted team scores in descending order
        Arguments:
        scores - array of strings contains several UCL match results
        format: <team1> <score>:<score> <team2>
        '''
        # Initialize empty hash for teams
        teams = dict()
        for score in scores:
            # Tokenize the string based on colon (:)
            tokens = score.split(":")

            # Parse first team name and score utilizing regex
            teamOne = re.sub("[0-9]", "", tokens[0]).strip()
            scoreOne = re.sub("[a-zA-Z]", "", tokens[0]).strip()
            # print(f"--- DEBUG: teamOne: {teamOne}, scoreOne: {scoreOne}")

            # Aggregate the score of a particular team in the above defined hashtable (teams)
            # If the team is already in the table then add the last score with the previous score \
            #   else we add the the new key:value data to hashtable
            teams[teamOne] = (teams.get(teamOne) + int(scoreOne)) if teams.get(teamOne) else int(scoreOne)
            
            # Parse the opponent team name and score utilizing regex
            teamTwo = re.sub("[0-9]", "", tokens[1]).strip()
            scoreTwo = re.sub("[a-zA-Z]", "", tokens[1]).strip()
            # print(f"--- DEBUG teamTwo: {teamTwo}, scoreTwo: {scoreTwo}")
            
            teams[teamTwo] = (teams.get(teamTwo) + int(scoreTwo)) if teams.get(teamTwo) else int(scoreTwo)
            # print(f'--- DEBUG unsorted teams: {teams}')
        
        # Sorting hash with builtin 'sorted' algorithm
        # teams = { k: v for k, v in sorted(teams.items(), key=lambda item: item[1], reverse=True) }

        # Sorting hash with custom written heap sort
        # Initialize heap object to start sorting process
        myHeap = MyHeap()

        return myHeap.sort(teams)


def main():
    '''
    Driver main function to test sample inputs
    '''
    obj = TeamScore()
    scores = [
        "Atletico Madrid 2:3 Real Madrid",
        "Real Madrid 4:1 PSG",
        "Barcelona FC 3:2 Manchester City",
        "Liverpool FC 20:10 Arsenal"
    ]
    print(obj.parseTeamScore(scores))

if __name__ == '__main__':
    main()