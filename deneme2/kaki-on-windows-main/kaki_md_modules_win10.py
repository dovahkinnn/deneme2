"""
This is an example of kaki app usin kivymd modules.
"""
import os
from collections import OrderedDict 
import datetime
from kivy.clock import Clock
import pyrebase
from firebase import firebase
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton,MDIconButton
from kivymd.uix.dialog import MDDialog
import requests
from kivymd.uix.list import OneLineListItem,TwoLineListItem
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine,MDExpansionPanelOneLine
from kivy.uix.image import AsyncImage
# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """ Hi Windows users """

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "kaki_md_module/screenmanager.kv"),
        os.path.join(os.getcwd(), "kaki_md_module/welcomescreen.kv"),
        os.path.join(os.getcwd(), "kaki_md_module/loginscreen.kv"),
        os.path.join(os.getcwd(), "kaki_md_module/mainscreen.kv"),
        os.path.join(os.getcwd(), "kaki_md_module/signupscreen.kv"),
        os.path.join(os.getcwd(), "kaki_md_module/anaekran.kv"),
        os.path.join(os.getcwd(), "kaki_md_module/anaekran2.kv"),
        os.path.join(os.getcwd(), "kaki_md_module/content.kv"),
        
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "kaki_md_module.screenmanager",
        "WelcomeScreen": "kaki_md_module.welcomescreen",
        "LoginScreen": "kaki_md_module.loginscreen",
        "MainScreen": "kaki_md_module.mainscreen",
        "SignupScreen": "kaki_md_module.signupscreen",
        "Anaekran": "kaki_md_module.anaekran",
        "Anaekran2": "kaki_md_module.anaekran2",
        "Content": "kaki_md_module.content",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):
        config={
            "apiKey": "AIzaSyC71mT-LhIio4H8e6-Wf-NJRe9tyA1K_ME",
            "authDomain": "kivyyyy-a3d06.firebaseapp.com",
            "projectId": "kivyyyy-a3d06",
            "storageBucket": "kivyyyy-a3d06.appspot.com",
            "messagingSenderId": "554392168771",
            "appId": "1:554392168771:web:ec2fb0944a88eb300967f6",
            "measurementId": "G-PJT9EK802Q",
            "databaseURL": "https://kivyyyy-a3d06-default-rtdb.europe-west1.firebasedatabase.app"
        }
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()
        self.url  = "https://kivyyyy-a3d06-default-rtdb.europe-west1.firebasedatabase.app/.json"
        self.strng=Factory.MainScreenManager()
        self.auth=firebase.auth()
        return self.strng

    def signup(self):
        signupEmail = self.strng.get_screen('signupscreen').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupscreen').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split())>1:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_username_dialog)
            self.dialog = MDDialog(title = 'Invalid Username',text = 'Please enter username without space',size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail,signupPassword)
            user=self.auth.create_user_with_email_and_password(signupEmail, signupPassword)
            
            signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".","-")
            signup_info = signup_info.replace("\'","")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url = self.url,json = to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'
    auth = 'sz6sDYPXqMmnZnp77Ff911hCqgvegOGsKnI2oBng'

    def login(self):
        loginEmail = self.strng.get_screen('loginscreen').ids.login_email.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text
        
        self.auth.sign_in_with_email_and_password(loginEmail,loginPassword)
        self.strng.get_screen('loginscreen').manager.current = 'first'
        from firebase import firebase
        signupEmail = self.strng.get_screen('loginscreen').ids.login_email.text




        firebase = firebase.FirebaseApplication('https://kivyyyy-a3d06-default-rtdb.europe-west1.firebasedatabase.app/.json', None)
        
        result = firebase.get('/',None, )


        for i in result:
            for c in result[i]:

                try:

                    a=(result[i][c])
                    try:
                        res = OrderedDict(reversed(list(a.items()))) 
                        for t in res:
                            a=res[t]
                            aimg = AsyncImage(source='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQkvawEwC7dsigR6U-zh3CdUQ5kW6_1DzN4Q&usqp=CAU')
                            self.strng.get_screen('first').ids.task_items.add_widget(
                            MDExpansionPanel(
                                image=aimg,  # panel icon
                                content=self.strng.get_screen('hakan'),  # panel content
                                panel_cls=MDExpansionPanelOneLine(text=a,on_release=self.play_song),  # panel class
                            )
                        )
                    except AttributeError:
                        pass
                    

                except TypeError :
                    pass

                        #self.strng.get_screen('first').ids.task_items.add_widget(OneLineListItem(size= (1000, 150),text=a, on_release=self.play_song))

                           


    def close_username_dialog(self,obj):
        self.dialog.dismiss()
    def play_song(self, onelinelistitem):
        print('play:', onelinelistitem.text)
    def refresh_callback(self, *args):
        """A method that updates the state of your application
        while the spinner remains on the screen."""

        def refresh_callback(interval):
            
            from firebase import firebase
            
            self.strng.get_screen('first').ids.task_items.clear_widgets()
            firebase = firebase.FirebaseApplication('https://kivyyyy-a3d06-default-rtdb.europe-west1.firebasedatabase.app/.json', None)
            
            result = firebase.get('/',None, )

            for i in result:
                for c in result[i]:

                    try:

                        a=(result[i][c])
                        try:
                            res = OrderedDict(reversed(list(a.items()))) 
                            for t in res:
                                a=res[t]
                                
                                self.strng.get_screen('first').ids.task_items.add_widget(
                                MDExpansionPanel(
                                    icon="account",  # panel icon
                                    content=self.strng.get_screen('hakan'),  # panel content
                                    panel_cls=MDExpansionPanelOneLine(text=a,on_release=self.play_song),  # panel class
                                )
                            )
                        except AttributeError:
                            pass
                        

                    except TypeError :
                        pass

            self.strng.get_screen('first').ids.refresh_layout.refresh_done()

        Clock.schedule_once(refresh_callback, 1)    
        
    
    def addTask(self):
        from firebase import firebase
        
        aa = self.strng.get_screen('loginscreen').ids.login_email.text
        tweet = self.strng.get_screen('second').ids.tweet_text.text
        current_time = datetime.datetime.now()
        current_time=str(current_time)
        x = current_time.replace(' ', '')
        z = x.replace(':', '')
        c = z.replace('.', '')
        c2 = c.replace('-', '')
        newtext = aa.replace('.', '-')

        
        self.db.child(newtext).child("tweet").child(c2).set(tweet)
        







# finally, run the app
if __name__ == "__main__":
    LiveApp().run()