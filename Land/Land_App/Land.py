import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Rectangle
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import csv
import os.path
from kivy.uix.slider import Slider
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionBarException
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionItem
from kivy.uix.actionbar import ActionButton
from kivy.utils import get_color_from_hex
from kivy.factory import Factory
from kivy.uix.checkbox import CheckBox
from kivy import properties
from kivy.uix.scrollview import ScrollView
from kivy.uix.carousel import Carousel
from kivy.effects.kinetic import KineticEffect
from kivy.base import runTouchApp
from kivy.uix.dropdown import DropDown


###from <file that has the class in> import <the class name you want to import>
##
###from your main script
##
##from folder.file import Klasa
##
###OR
##
##from folder import file
##k = file.Klasa()
##
###OR
##
##import folder.file as myModule
##k = myModule.Klasa()





############################################# LOGIN WINDOW ################################################################     

class LoginWindow(Screen):

    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def loginbtn(self):
        destination = "/Users/iantaylor/Desktop/PyVirtualEnvironments/Land/CSV/"
        
        with open (destination + 'VALIDATE.csv', 'w')as userinfo:
            writer = csv.writer(userinfo, dialect = 'excel')
            writer.writerow(['EMAIL', 'PASSWORD'])
            writer.writerow([' ', ' '])

        with open (destination + 'LandList.csv', 'w')as LandList:
            writer = csv.writer(LandList, dialect = 'excel')
            writer.writerow(['NAME','LOCATION',''])
            
        
        with open(destination + 'VALIDATE.csv', 'r') as userlog:
            Lgin = False
            em = self.email.text
            pw = self.password.text
            reader = csv.reader(userlog, dialect = 'excel')
            for row in reader:
                if (row[0] != em) or (row[1] != pw):
                    Lgin = False
                else:
                    print('email:', row[0], 'password:', row[1])
                    Lgin = True
                    break
                
            if Lgin == True:
                return True
            if Lgin == False:
                return False

############################################# CREATE HOST ACCOUNT WINDDOW ##########################################################  

class CreateHostAccount1Window(Screen):
    pass

############################################# CREATE HOST ACCOUNT WINDDOW 2 ##########################################################

class CreateHostAccount2Window(Screen):
    pass

############################################# CREATE USER ACCOUNT WINDDOW ##########################################################

class CreateUserAccountWindow(Screen):
    pass

############################################# EXPLORE LAND WINDOW ################################################################     

class ExploreLandWindow(Screen):
    Search = ObjectProperty(None)
    
    def SearchBtn(self):
        return Search.SearchPressed()
    
############################################# BROWSE LAND WINDOW ################################################################
    
class BrowseLandWindow(Screen):
    
    def rockclimbing():
        return Search.SearchPressed()

############################################# FAVORITES WINDOW ################################################################     
    
        

class FavoritesWindow(Screen):
    pass


############################################# PROFILE WINDOW ################################################################     

class ProfileWindow(Screen):
    pass


############################################# FAQ WINDOW ################################################################     

class FAQWindow(Screen):
    pass

############################################# WINDOW MANAGER ################################################################     

class WindowManager(ScreenManager):


    ######## FILTER DICTIONARY, THAT CONTAINS TRUE OR FALSE VALUE FOR EVERY ACTIVITY #########
    FilterDictionary = {
        'fishing': False,
        'hunting': False,
        'camping': False,
        'rockclimbing': False,
        'mtview': False,
        'weddingv': False,
        'offroading': False,
        'firearmsyes': False,
        'desertview': False,
        'oceanview': False,
        'hiking': False,
        'house': False,
        'firingrange': False,
        'stage': False
        }

    
    ####### METHOD FOR RESPONDING TO THE SEARCH BUTTON BEING PRESSED ON THE EXPLORE PAGE #####
    def SearchPressed():
        print('search text passed to search method within explore class properly')


    ########## ACTIVITY'S CHECKBOX STATE METHODS (HANDLING ON STATES FROM FILTER CHECK BOXES) ###########
        
    # 1 FISHING
    def Fishing(self, state):
        if state == 'down':
            return self.Activities('fishing', 'True')
        elif state == 'normal':
            return self.Activities('fishing', 'False')

    # 2 HUNTING
    def Hunting(self, state):
        if state == 'down':
            return self.Activities('hunting', 'True')
        elif state == 'normal':
            return self.Activities('hunting', 'False')

    # 3 CAMPING
    def Camping(self, state):
        if state == 'down':
            return self.Activities('camping', 'True')
        elif state == 'normal':
            return self.Activities('camping', 'False')

    # 4 ROCK CLIMBING
    def RockClimbing(self, state):
        if state == 'down':
            return self.Activities('rockclimbing', 'True')
        elif state == 'normal':
            return self.Activities('rockclimbing', 'False')


    # 5 MOUNTAIN VIEW
    def MtView(self, state):
        if state == 'down':
            return self.Activities('mtview', 'True')
        elif state == 'normal':
            return self.Activities('mtview', 'False')

    # 6 WEDDING VENUE
    def WeddingV(self, state):
        if state == 'down':
            return self.Activities('weddingv', 'True')
        elif state == 'normal':
            return self.Activities('weddingv', 'False')


    # 7 OFF ROADING
    def OffRoading(self, state):
        if state == 'down':
            return self.Activities('offroading', 'True')
        elif state == 'normal':
            return self.Activities('offroading', 'False')
        
    # 8 FIREARMSYES
    def FirearmsYes(self, state):
        if state == 'down':
            return self.Activities('firearmsyes', 'True')
        elif state == 'normal':
            return self.Activities('firearmsyes', 'False')

    # 9 DESERT VIEW
    def DesertView(self, state):
        if state == 'down':
            return self.Activities('desertview', 'True')
        elif state == 'normal':
            return self.Activities('desertview', 'False')

    # 10 OCEAN VIEW
    def OceanView(self, state):
        if state == 'down':
            return self.Activities('oceanview', 'True')
        elif state == 'normal':
            return self.Activities('oceanview', 'False')

    # 11 HIKING
    def Hiking(self, state):
        if state == 'down':
            return self.Activities('hiking', 'True')
        elif state == 'normal':
            return self.Activities('hiking', 'False')


    # 12 HOUSE
    def House(self, state):
        if state == 'down':
            return self.Activities('house', 'True')
        elif state == 'normal':
            return self.Activities('house', 'False')

    # 13 FIRING RANGE
    def FiringRange(self, state):
        if state == 'down':
            return self.Activities('firingrange', 'True')
        elif state == 'normal':
            return self.Activities('firingrange', 'False')

    # 14 STAGE
    def Stage(self, state):
        if state == 'down':
            return self.Activities('stage', 'True')
        elif state == 'normal':
            return self.Activities('stage', 'False')


    ######### THE 'ACTIVITIES' METHOD - HANDLES THE RETURNS OF THE ACTIVITY CHECKBOX STATE METHODS

    def Activities(self, activity, boolean):
        # 1 fishing:
        
        if activity == 'fishing' and boolean == 'True':
            self.FilterDictionary['fishing'] = True
        elif activity == 'fishing' and boolean == 'False':
            self.FilterDictionary['fishing'] = False
        
        # 2 hunting:
        
        elif activity == 'hunting' and boolean == 'True':
            self.FilterDictionary['hunting'] = True
        elif activity == 'hunting' and boolean == 'False':
            self.FilterDictionary['hunting'] = False
            
        # 3 camping:
        
        elif activity == 'camping' and boolean == 'True':
            self.FilterDictionary['camping'] = True
        elif activity == 'camping' and boolean == 'False':
            self.FilterDictionary['camping'] = False
            
        #4 rock climbing:
            
        elif activity == 'rockclimbing' and boolean == 'True':
            self.FilterDictionary['rockclimbing'] = True
        elif activity == 'rockclimbing' and boolean == 'False':
            self.FilterDictionary['rockclimbing'] = False

        #5 MOUNTAIN VIEW

        elif activity == 'mtview' and boolean == 'True':
            self.FilterDictionary['mtview'] = True
        elif activity == 'mtview' and boolean == 'False':
            self.FilterDictionary['mtview'] = False

        #6 WEDDING VENUE
        elif activity == 'weddingv' and boolean == 'True':
            self.FilterDictionary['weddingv'] = True
        elif activity == 'weddingv' and boolean == 'False':
            self.FilterDictionary['weddingv'] = False

        #7 OFF ROADING
        elif activity == 'offroading' and boolean == 'True':
            self.FilterDictionary['offroading'] = True
        elif activity == 'offroading' and boolean == 'False':
            self.FilterDictionary['offroading'] = False

        # 8 FIREARMS ALLOWED
        elif activity == 'firearmsyes' and boolean == 'True':
            self.FilterDictionary['firearmsyes'] = True
        elif activity == 'firearmsyes' and boolean == 'False':
            self.FilterDictionary['firearmsyes'] = False

        # 9 DESERT VIEW
        elif activity == 'desertview' and boolean == 'True':
            self.FilterDictionary['desertview'] = True
        elif activity == 'desertview' and boolean == 'False':
            self.FilterDictionary['v'] = False

        # 10 OCEAN VIEW
        elif activity == 'oceanview' and boolean == 'True':
            self.FilterDictionary['oceanview'] = True
        elif activity == 'oceanview' and boolean == 'False':
            self.FilterDictionary['oceanview'] = False

        # 11 HIKING
        elif activity == 'hiking' and boolean == 'True':
            self.FilterDictionary['hiking'] = True
        elif activity == 'hiking' and boolean == 'False':
            self.FilterDictionary['hiking'] = False

        # 12 HOUSE
        elif activity == 'house' and boolean == 'True':
            self.FilterDictionary['house'] = True
        elif activity == 'house' and boolean == 'False':
            self.FilterDictionary['house'] = False

        # 13 FIRING RANGE
        elif activity == 'firingrange' and boolean == 'True':
            self.FilterDictionary['firingrange'] = True
        elif activity == 'firingrange' and boolean == 'False':
            self.FilterDictionary['firingrange'] = False

        # 14 STAGE
        elif activity == 'stage' and boolean == 'True':
            self.FilterDictionary['stage'] = True
        elif activity == 'stage' and boolean == 'False':
            self.FilterDictionary['stage'] = False
            
        #else bracket that should never be raised since all checboxes pass designated values.
        else:
            pass
        
        print(self.FilterDictionary)









############################################# BUILD THE APP ################################################################ 
        
Build_Land = Builder.load_file('land.kv')


class LandOfficialApp(App):
    def build(self):
        return Build_Land


if __name__ == "__main__":
    LandOfficialApp().run()

###########################################################################################################################
