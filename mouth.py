from images import *

class Mouth(Images):
    def __init__(self, teeth_color, tongue_color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Values.
        self.teeth_color = teeth_color
        self.tongue_color = tongue_color
        
    #Animation states.
    #Happy.
    def happy(self):
        self._reset_matris()
        lips = [[0, 1, 2, 3, 4, 5, 6, 7], [0, 7], [1, 6], [2, 3, 4, 5]]
        teeth = [[], [1, 2, 3, 4, 5, 6], [2, 3, 4, 5]]
        self._spawn_dots(self.color, lips)
        self._spawn_dots(self.teeth_color, teeth)
        return self.matris
    
    #Smile.
    def smile(self):
        self._reset_matris()
        lips = [[], [1, 6], [2, 3, 4, 5]]
        self._spawn_dots(self.color, lips)
        return self.matris

    #Neutral.
    def neutral(self):
        self._reset_matris()
        lips = [[], [], [1, 2, 3, 4, 5, 6]]
        self._spawn_dots(self.color, lips)
        return self.matris
    
    #Long.
    def long(self):
        self._reset_matris()
        lips = [[], [], [0, 1, 2, 3, 4, 5, 6, 7]]
        self._spawn_dots(self.color, lips)
        return self.matris

    #Sad.
    def sad(self):
        self._reset_matris()
        lips = [[], [], [2, 3, 4, 5], [1, 6]]
        self._spawn_dots(self.color, lips)
        return self.matris

    #Animations.
    #Warm animation.
    def warm_0(self):
        self._reset_matris()
        lips = [[], [1, 6], [2, 3, 4, 5]]
        self._spawn_dots(self.color, lips)
        return self.matris
    
    def warm_1(self):
        self._reset_matris()
        lips = [[], [1, 3, 4, 6], [2, 5]]
        self._spawn_dots(self.color, lips)
        return self.matris

    #Talking animation states.
    #A.
    def a_letter(self):
        self._reset_matris()
        lips = [[1, 2, 3, 4, 5, 6], [1, 6], [1, 6], [2, 3, 4, 5]]
        self._spawn_dots(self.color, lips)
        return self.matris
    
    #B.
    def b_letter(self):
        self._reset_matris()
        lips = [[3, 4], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [3, 4]]
        self._spawn_dots(self.color, lips)
        return self.matris
    
    #D.
    def d_letter(self):
        self._reset_matris()
        lips = [[2, 3, 4, 5], [1, 6], [1, 6], [2, 3, 4, 5]]
        self._spawn_dots(self.color, lips)
        teeth = [[], [2, 3, 4, 5], [2, 3, 4, 5]]
        self._spawn_dots(self.teeth_color, teeth)
                
        return self.matris

    #E.
    def e_letter(self):
        self._reset_matris()
        lips = [[2, 3, 4, 5], [1, 6], [2, 3, 4, 5]]
        self._spawn_dots(self.color, lips)
        return self.matris
    
    #FVW.
    def fvw_letter(self):
        self._reset_matris()
        lips = [[3, 4], [2, 5], [2, 3, 4, 5], [3, 4]]
        self._spawn_dots(self.color, lips)
        teeth = [[], [3, 4]]
        self._spawn_dots(self.teeth_color, teeth)
        return self.matris
    
    #H.
    def h_letter(self):
        self._reset_matris()
        lips = [[2, 3, 4, 5], [2, 5], [2, 5], [3, 4]]
        self._spawn_dots(self.color, lips)
        teeth = [[], [3, 4]]
        self._spawn_dots(self.teeth_color, teeth)
        return self.matris
    
    #J.
    def j_letter(self):
        self._reset_matris()
        lips = [[2, 3, 4, 5], [1, 6], [1, 6], [2, 3, 4, 5]]
        tongue = [[], [2, 3, 4, 5], []]
        self._spawn_dots(self.color, lips)
        self._spawn_dots(self.tongue_color, tongue)
        return self.matris

    #K.
    def k_letter(self):
        self._reset_matris()
        lips = [[2, 3, 4, 5], [1, 6], [1, 6], [2, 3, 4, 5]]
        self._spawn_dots(self.color, lips)
        teeth = [[], [2, 3, 4, 5]]
        self._spawn_dots(self.teeth_color, teeth)
        return self.matris
    
    #L.
    def l_letter(self):
        self._reset_matris()
        lips = [[2, 3, 4, 5], [1, 6], [1, 6], [2, 3, 4, 5]]
        tongue = [[], [3, 4], [2, 3, 4, 5]]
        self._spawn_dots(self.color, lips)
        self._spawn_dots(self.tongue_color, tongue)
        return self.matris
    
    #M.
    def m_letter(self):
        self._reset_matris()
        lips = [[], [1, 2, 3, 4, 5, 6], [2, 3, 4, 5]]
        self._spawn_dots(self.color, lips)
        return self.matris
    
    #N.
    def n_letter(self):
        self._reset_matris()
        lips = [[], [1, 2, 3, 4, 5, 6], [2, 5], [3, 4]]
        self._spawn_dots(self.color, lips)
        teeth = [[], [], [3, 4]]
        self._spawn_dots(self.teeth_color, teeth)
        return self.matris
    
    #O.
    def o_letter(self):
        self._reset_matris()
        lips = [[3, 4], [2, 5], [2, 5], [3, 4]]
        self._spawn_dots(self.color, lips)
        return self.matris
    
    #P.
    def p_letter(self):
        self._reset_matris()
        lips = [[3, 4], [2, 3, 4, 5], [2, 3, 4, 5], [3, 4]]
        self._spawn_dots(self.color, lips)
        return self.matris


    #S.
    def s_letter(self):
        self._reset_matris()
        lips = [[2, 3, 4, 5], [1, 6], [2, 5], [3, 4]]
        self._spawn_dots(self.color, lips)
        teeth = [[], [2, 3, 4, 5], [3, 4]]
        self._spawn_dots(self.teeth_color, teeth)
        return self.matris
    
    #T.
    def t_letter(self):
        self._reset_matris()
        lips = [[3, 4], [2, 5], [2, 5], [3, 4]]
        self._spawn_dots(self.color, lips)
        teeth = [[], [3, 4], [3, 4]]
        self._spawn_dots(self.teeth_color, teeth)
        return self.matris
    
    #U.
    def u_letter(self):
        self._reset_matris()
        lips = [[2, 3, 4, 5], [2, 5], [2, 5], [3, 4]]
        self._spawn_dots(self.color, lips)
        return self.matris
    
    #Q.
    def q_letter(self):
        self._reset_matris()
        lips = [[2, 3, 4, 5], [2, 3, 4, 5], [2, 5], [3, 4]]
        self._spawn_dots(self.color, lips)
        return self.matris
