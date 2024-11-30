class ModelBaseReflexAgent:
    roomPrevState={
        
    }
    def __init__(self,desiredTemp,rooms):
        self.desiredTemp=desiredTemp
        for room,state in rooms.items():
            self.roomPrevState[room]=False
    def Sense(self,currentTemp):
        self.currentTemp= currentTemp
        return currentTemp
    def Actuator(self,room):
        if self.currentTemp>self.desiredTemp and self.roomPrevState[room]!=False:
            action="Turn Off the Heater of"
            self.roomPrevState[room]=False
        elif self.currentTemp<self.desiredTemp and self.roomPrevState[room]!=True: 
            action="Turn ON the Heater of"
            self.roomPrevState[room]=True
        else:
            if self.roomPrevState[room]==True:
                action=f"Heater is Already On of"
            else:    
                action=f"Heater is Already Off of"
        return action 
rooms={
    "LivingRoom":33,
    "DiningRoom":15,
    "BedRoom1":25,
    "BedRoom2":18,
    "BedRoom3":27
    
}
desireTemp=20     
agent=ModelBaseReflexAgent(desireTemp,rooms)
for room,temp in rooms.items():
    agent.Sense(temp)
    print(f"{agent.Actuator(room)} {room}")
print(f"Now States of Heaters are {agent.roomPrevState}")        