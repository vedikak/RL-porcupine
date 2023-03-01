# Cell class to represent each cell in the lattice
class Cell:
    def __init__(self) -> None:
        # self.is_home = False
        # self.is_target = False
        self.cell_assc_heat = 0
        self.pain_level = 0
        self.score=0
        

    # update heat level in the environment
    def addHeat(self,surrounding_8,surrounding_16,world_temp=0):
        total_heat=0
        for i in surrounding_8:
            if i>1:
                total_heat=total_heat+(i-1)
        for i in surrounding_16:
            if i>2:
                total_heat=total_heat+(i-2)

        # self.cell_assc_heat += world_temp

    # update pain level in the environment
    def addPain(self, pain_unit=0.0):
        self.pain_level += pain_unit

    # update target pheromone level in the environment
    # def addTargetHeat(self, pher_unit=0.2):
        # self.target_pher_level += pher_unit
        
    # evoporates the pheromone in the environment as time goes by
    # def evoporate(self, evoporation_rate=0.99):
    #     self.home_pher_level *= evoporation_rate
    #     self.target_pher_level *= evoporation_rate
        
    # disperse the heat to surrounding cell depending on differnce
    # in concentration
    # def disperse(self, surrounding_cell, type="home", dispersion_rate=0.04):
    def disperse(self, surrounding_cell,dispersion_rate=0.04):
        avg_heat_level_env = sum(surrounding_cell)/len(surrounding_cell)
        # if type == "home":
        heat_difference = avg_heat_level_env - self.cell_assc_heat
        self.cell_assc_heat += heat_difference*dispersion_rate
        # # elif type == "target":
        #     pher_difference = avg_heat_level_env - self.target_pher_level
        #     self.target_pher_level += pher_difference*dispersion_rate

    # set cells as either home or target
    # def load(self, **kwarg):
    #     if kwarg['line'] == 'H':
    #         self.setCell(is_home=True, is_target=False, home_pher_level=0, target_pher_level=0)
    #     elif kwarg['line'] == 'F':
    #         self.setCell(is_home=False, is_target=True, home_pher_level=0, target_pher_level=0)
    #     else:
    #         self.setCell(home_pher_level=0, target_pher_level=0)
    
    def setCell(self,cell_assc_heat=0.0, pain_level=0.0):
        # self.is_home = is_home
        # self.is_target = is_target
        self.cell_assc_heat = cell_assc_heat
        self.pain_level = pain_level
        self.score=self.score

    def addScore(self, cell_assc_heat, pain_level):
        self.cell_assc_heat = cell_assc_heat
        self.pain_level = pain_level
        self.score=self.cell_assc_heat + self.pain_level  

    def getCell(self):
        cell_data = {
            # "is_home" : self.is_home,
            # "is_target" : self.is_target,
            "cell_assc_heat" : self.cell_assc_heat,
            "pain_level" :self.pain_level,
            "score" :self.score
            # "target_pher_level" : self.target_pher_level,
        }
        return cell_data