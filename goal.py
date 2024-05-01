class Planner:
    def __init__(self):
        self.li=[]
        
    def add_goal(self,goal):
        self.li.append(goal)
    
    def plann_goals(self):
        while self.li:
            curr_goal=self.li.pop()
            if isinstance(curr_goal,str):
                print("Executing Goal:",curr_goal)
            else:
                print("Decomposing Goal:",curr_goal[0])
                for sub_goal in curr_goal[1:]:
                    self.li.append(sub_goal)

        
obj=Planner()
obj.add_goal('Reach Destination')
obj.add_goal(['Find key','Open door'])
obj.add_goal(['Find map','Find compass'])
obj.plann_goals()