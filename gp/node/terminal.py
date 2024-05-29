from .baseline import Node

import numpy as np

# Arrival time of request
class ATR(Node):
    def __init__(self):
         super(ATR,self).__init__()
    def __repr__(self):
        return "ATR"
    def _GetHumanExpressionSpecificNode(self, args):
        return "ATR"
    def getSymbol(self):
        return "ATR"
    def GetOutput(self, X):
        return X.r.arrival

# Start date of request
class SDR(Node):
    def __init__(self):
         super(SDR,self).__init__()
    def __repr__(self):
        return "SDR"
    def _GetHumanExpressionSpecificNode(self, args):
        return "SDR"
    def getSymbol(self):
        return "SDR"
    def GetOutput(self, X):
        return X.r.tw_start

# Due date of request
class DDR(Node):
    def __init__(self):
         super(DDR,self).__init__()
    def __repr__(self):
        return "DDR"
    def _GetHumanExpressionSpecificNode(self, args):
        return "DDR"
    def getSymbol(self):
        return "DDR"
    def GetOutput(self, X):
        return X.r.tw_end
    
# distance to the customer being considered
class DCC(Node):
    def __init__(self):
         super(DCC,self).__init__()
    def __repr__(self):
        return "DCC"
    def _GetHumanExpressionSpecificNode(self, args):
        return "DCC"
    def getSymbol(self):
        return "DCC"
    def GetOutput(self, X):
        return X.r.tw_end
    
# customer can ready to served
class CRS(Node):
    def __init__(self):
         super(CRS,self).__init__()
    def __repr__(self):
        return "CRS"
    def _GetHumanExpressionSpecificNode(self, args):
        return "CRS"
    def getSymbol(self):
        return "CRS"
    def GetOutput(self, X):
        return X.r.earliness

# the amount of time till customer due date
class CDS(Node):
    def __init__(self):
         super(CDS,self).__init__()
    def __repr__(self):
        return "CDS"
    def _GetHumanExpressionSpecificNode(self, args):
        return "CDS"
    def getSymbol(self):
        return "CDS"
    def GetOutput(self, X):
        return X.r.lateness

# truck remaining capacity
class TRC(Node):
    def __init__(self):
         super(TRC,self).__init__()
    def __repr__(self):
        return "TRC"
    def _GetHumanExpressionSpecificNode(self, args):
        return "TRC"
    def getSymbol(self):
        return "TRC"
    def GetOutput(self, X):
        return X.truck.capacity

# drone remaining capacity
class DRC(Node):
    def __init__(self):
         super(DRC,self).__init__()
    def __repr__(self):
        return "DRC"
    def _GetHumanExpressionSpecificNode(self, args):
        return "DRC"
    def getSymbol(self):
        return "DRC"
    def GetOutput(self, X):
        return X.drone.capacity

# drone remaining battery
class DRB(Node):
    def __init__(self):
         super(DRB,self).__init__()
    def __repr__(self):
        return "DRB"
    def _GetHumanExpressionSpecificNode(self, args):
        return "DRB"
    def getSymbol(self):
        return "DRB"
    def GetOutput(self, X):
        return X.drone.battery

# waiting time of drone to meet truck again

# customer demand (maybe not because we will solve stochastic demand problem)


 ##############################################################   
class Rand(Node):
    def __init__(self):
        super(Rand, self).__init__()
    def __repr__(self):
        return "Rand"
    def _GetHumanExpressionSpecificNode(self, args):
        return "Rand"
    def getSymbol(self):
        return "Rand"
    def GetOutput(self, X):
        return np.random.rand()
      
class Const(Node):
    def __init__(self):
        super(Const, self).__init__()
        self.value = np.random.uniform(0, 1)
    def __repr__(self):
        return "Const"
    def _GetHumanExpressionSpecificNode(self, args):
        return "Const"
    def getSymbol(self):
        return "Const"
    def GetOutput(self, X):
        return self.value
    def GetSurrogateOutput(self, X):
        return self.value 

    def mutate_value(self):
        self.value = self.value + np.random.normal(0, 0.1)           

####################################################################