class User:
    def __init__(self,id,name):
        print("new user created")
        self.id=id
        self.name=name
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1
    

user1=User('115','Max')
print(user1.name+" "+user1.id) 
user2=User('116','Toto')
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)