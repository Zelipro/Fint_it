#Les outils
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from random import randint

#Window Size
#Window.size = [320,600]
#main
class Fint_it(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        main = Builder.load_file("main.kv")
        return main
    
    def on_start(self):
        self.Choisi()
        
    def Change(self,instance):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"
    
    def Option_List(self,instance):
        dic = {"Leave":self.stopp , "Help":self.help , "About as":self.info}
        dic.get(instance.text)()
    
    def info(self):
        self.show_info(title = "info" , text = "Name : Fint it \nAuthor : Elisée ATIKPO")
    def help(self):
        self.show_info(title = "Help" ,text="You have just to write a number beetween 1 and 1000")
    def stopp(self):
        self.show_info(title = "Info",text = "Bye !!!",fonct=self.stop)

    def show_info(self,title,text,fonct=None):
        self.MD = MDDialog(
            title = title,
            text = text,
            buttons = [
                MDFlatButton(
                    text  = "[b]Valider[/b]",
                    on_release= lambda x : self.Ok1(x,fonct)
                )
            ]
        )
        self.MD.open()
    
    def Ok1(self,instance,fonct):
        self.MD.dismiss()
        if fonct:fonct()
    
    def Choisi(self):
        self.Seach = randint(1,100)
        self.Fois = 0
        self.Put_score()
    
    def Score(self,instance):
        self.show_info(title="Score" , text=f"The number of your try is {self.Fois}") 
    
    def Put_score(self):
        self.root.ids.Score.text = f"[b]{str(self.Fois)}[/b]" 
        
    def Go(self,instance):
        Entry = self.root.ids.Entry
        if Entry.text is "":
            Entry.error = True
        elif int(Entry.text) > self.Seach:
            self.show_info(title = "Indice",text="To big")
            self.Fois += 1
            self.Put_score()
            
        elif int(Entry.text) < self.Seach:
            self.show_info(title = "Indice",text="To small")
            self.Fois += 1
            self.Put_score()
            
        else:
            self.show_info(title = "Congratulation" , text=f"Congratulation you find it after {self.Fois} try !",fonct=self.Quest)
            
    def Quest(self):
        self.MD2 = MDDialog(
            title = "Question",
            text = "Continuer ?",
            buttons = [
                MDFlatButton(
                    text  = "[b]Oui[/b]",
                    on_release= lambda x : self.Ok2(x)
                ),
                MDFlatButton(
                    text  = "[b]Non[/b]",
                    on_release= lambda x : self.Non1(x)
                )
            ]
        )
        self.MD2.open()
    
    def Ok2(self,instance):
        self.Choisi()
        self.MD2.dismiss()
    
    def Non1(self,instance):
        self.stopp()
        
Fint_it().run()
