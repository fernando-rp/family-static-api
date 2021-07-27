
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": "Jackson",
            "age": 33,
            "lucky_numbers": [7,13,22]
        },{
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": "Jackson",
            "age": 35,
            "lucky_numbers": [10,14,3]
        } ,{
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": "Jackson",
            "age": 5,
            "lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        n_member = dict()
        n_member["first_name"]= str(member["first_name"])
        n_member["last_name"]=self.last_name
        n_member["age"]=int(member["age"])
        n_member["lucky_numbers"]=list(member["lucky_numbers"])

        if "id" in member:
            n_member["id"]=member["id"]
        else:
            n_member["id"]=self._generateId()
 
        self._members.append(n_member)
        return n_member

    def get_member(self, id):
        # fill this method and update the return
        members=self.get_all_members()
        for index in range(len(members)):
            if (members[index]['id'] == id):
                return members[index]

    def delete_member(self, id):
        # fill this method and update the return
        members=self.get_all_members()
        for index in range(len(members)):
            if members[index]["id"] == id:
                members.pop(index)
                msg={"done": True}    
                return msg

    def update_member(self, member,id):
        members=self.get_all_members()
        for index in range(len(members)):
            if members[index]["id"] == id:
                members[index].update(member)
                msg={"done": True}    
                return msg


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
