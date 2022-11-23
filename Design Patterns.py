#< Singleton >#
"""
#> 1: With one inner private class
class SingletonObject(object):
    class __SingletonObject():
        def __init__(self):
            self.val = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()

        return SingletonObject.instance

    #access to the private "__SingletonObject" class
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)


#> 2: simple
class SingletonObject():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


#> 3: lazy instantiation
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("mikhaym obj ro eejad konim...")
        else:
            print("obj ghablan eejad shode", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
#s0 = Singleton()
#s1 = Singleton()
#print("obj eejad shode", Singleton.getInstance())
#s2 = Singleton()
#s3 = Singleton()
"""



#< Monostate >#
"""
#> 1
class Monostate:
    _shared_state = {"1":"2"}
    def __init__(self):
        self.x = 150
        self.__dict__ = self._shared_state
        pass


#> 2:  Better (Because You Can Set Attr)
class Monostate():
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj
"""


#< Factory:Simple Factory >#
"""
#> 1: 
from abc import ABCMeta, abstractmethod

class Book(metaclass = ABCMeta):
    @abstractmethod
    def num_of_pages(self):
        pass

class Head_First_Python(Book):
    def num_of_pages(self):
        print("500")
class Python_CookBook(Book):
    def num_of_pages(self):
        print("300")

#Publication Factory
class PublicationFactory():
    def Book_publicator(self, object_type):
        return eval(object_type)().num_of_pages()

#Client code
if __name__ == '__main__':
    pf = PublicationFactory()
    book = input("che ketabi ro chap konam, Head_First_Python ya Python_CookBook?")
    pf.Book_publicator(book)
"""

#< Factory::Factory Method >#
"""
#> 1:
from abc import ABCMeta, abstractmethod

#Product
class Section(metaclass = ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("PersonalSection")
class AlbumSection(Section):
    def describe(self):
        print("AlbumSection")
class PatentSection(Section):
    def describe(self):
        print("PatentSection")
class PublicationSection(Section):
    def describe(self):
        print("PublicationSection")

#Creator
class Profile(metaclass = ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSections(self, section):
        self.sections.append(section)

class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class facebook(Profile):
    def createProfile(self):
            self.addSections(PersonalSection())
            self.addSections(AlbumSection())

#Client
if __name__ == '__main__':
    profile_input = input("Che profile ro vasat eejad konam?")
    profile = eval(profile_input.lower())()
    print("profile skhte shode:", type(profile).__name__)
    print("profile daraye section haye roberoo mibashad:", profile.getSections())


"""

#< Factory:Abstract Factory >#
"""
#> 1:
from abc import ABCMeta, abstractmethod

#AbstractFactory
class CoffeeFactory(metaclass = ABCMeta):
    @abstractmethod
    def createCoffeeWithOutMilk(self):
        pass
    @abstractmethod
    def createCoffeeWithMilk(self):
        pass

#ConcreteFactory
class ItalianCoffeeFactory(CoffeeFactory):
    def createCoffeeWithOutMilk(self):
        return ItalianEspresso()
    def createCoffeeWithMilk(self):
        return ItalianCappucino()

class FrenchCoffeeFactory(CoffeeFactory):
    def createCoffeeWithOutMilk(self):
        return FrenchEspresso()
    def createCoffeeWithMilk(self):
        return FrenchCappucino()

#AbstractProduct
class CoffeeWithOutMilk(metaclass = ABCMeta):
    @abstractmethod
    def prepare(self, CoffeeWithOutMilk):
        pass

class CoffeeWithMilk(metaclass = ABCMeta):
    @abstractmethod
    def serve(self, CoffeeWithOutMilk):
        pass

#ConcreteProduct
class ItalianEspresso(CoffeeWithOutMilk):
    def prepare(self):
        print("Prepare ", type(self).__name__)

class ItalianCappucino(CoffeeWithMilk):
    def serve(self, CoffeeWithOutMilk):
        print(type(self).__name__, " is served with sheep's milk on ", type(CoffeeWithOutMilk).__name__)

class FrenchEspresso(CoffeeWithOutMilk):
    def prepare(self):
        print("Prepare ", type(self).__name__)

class FrenchCappucino(CoffeeWithMilk):
    def serve(self, CoffeeWithOutMilk):
        print(type(self).__name__, " is served with cow's milk on ", type(CoffeeWithOutMilk).__name__)

#Client
class CoffeeStore:
    def __init__(self):
        pass
    def makeCoffee(self):
        for factory in [ItalianCoffeeFactory(), FrenchCoffeeFactory()]:
            self.factory = factory
            self.CoffeeWithOutMilk = self.factory.createCoffeeWithOutMilk()
            self.CoffeeWithMilk = self.factory.createCoffeeWithMilk()
            self.CoffeeWithOutMilk.prepare()
            self.CoffeeWithMilk.serve(self.CoffeeWithOutMilk)

Coffee = CoffeeStore()
Coffee.makeCoffee()

"""



#< Facade >#
"""
#Subsystems
class Presenter():
    def __init__(self):
        print("Maraseme shoma che roozi ast va chand saat va che noe marasemi ast?")
    def setPresentation(self):
        print("4shanbe, 2saat, Jashne voroodi haye jadid")
class TheaterGroup():
    def __init__(self):
        print("Theater tanz bashe ya jedi?")
    def setTheater(self):
        print("Tanz")
class Caterer():
    def __init__(self):
        print("che paziraee?")
    def setCatering(self):
        print("Keyk, abmiveh, sib")
class Lecturer():
    def __init__(self):
        print("Mozooe sokhanrani?")
    def setLecture(self):
        print("Tafavot haye daneshgah ba dabirestan")
class MusicGroup():
    def __init__(self):
        print("chand track ejra konim va az che sabki?")
    def setMusic(self):
        print("2, Sonati")

#Client
class You():
    def __init__(self):
        print("You:: BARGOZARI JASHN NYAZ BE KARHAYE ZYADI DARAD")
    def askEventManager(self):
        print("You:: Tamame karha ro misparam be anjoman")
        em = EventManager()
        em.arrange()
    def __del__(self):
        print("You:: Tashakor az bachehaye anjoman ke tamame kar ha ro anjam dadand")    

#Facade
class EventManager():
    def __init__(self):
        print("EventManager:: Bezar Man Ba Tamame afrad hamahang konam\n")
    def arrange(self):
        self.presenter = Presenter()
        self.presenter.setPresentation()
        self.theaterGroup = TheaterGroup()
        self.theaterGroup.setTheater()
        self.caterer = Caterer()
        self.caterer.setCatering()
        self.lecturer = Lecturer()
        self.lecturer.setLecture()
        self.musicGroup = MusicGroup()
        self.musicGroup.setMusic()

you = You()
you.askEventManager()


"""



#< Proxy >#
"""
from abc import ABCMeta, abstractmethod

#Subject
class Pardakhtan(metaclass = ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

#RealSubject
class Bank(Pardakhtan):
    def __init__(self):
        self.card = None
        self.account = None
    def __getAccount(self):
        self.account = self.card
        return self.account
    def __mojoodiDashtan(self):
        print("Bank:: chech mikonad k aya account", self.__getAccount(), "b andaze kafi mojoodi darad ya na")
        return False
    def setCard(self, card):
        self.card = card
    def do_pay(self):
        if self.__mojoodiDashtan():
            print("Bank:: Hazineh pardakht shod")
            return True
        else:
            print("Bank:: Mojoodi Nakafi")
            return False

#Proxy
class Card(Pardakhtan):
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card = input("Proxy:: Shomare Card ra vared kon ")
        self.bank.setCard(card)
        return self.bank.do_pay()

#Client
class You:
    def __init__(self):
        print("You:: Mikham ye pirahan bekharam")
        self.card = Card()
        self.isPurchased = None
    def pardakht(self):
        self.isPurchased = self.card.do_pay()
    def __del__(self):
        if self.isPurchased:
            print("You:: Pirahan ra kharidam")
        else:
            print("You:: poolam baraye kharid pirahan kafi nabood")

you = You()
you.pardakht()
"""



#< Observer >#
"""
#> 1
#Subject(Object)
class Subject:
    def __init__(self):
        self.__observers = []
    def register(self, observer):
        self.__observers.append(observer)
    def notifyEveryOne(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

#Observers
class Observer1:
    def __init__(self, subject):
        subject.register(self)
    def notify(self, subject, *args, **kwargs):
        print(type(self).__name__, args, 'az', subject, 'reside ast')
class Observer2:
    def __init__(self, subject):
        subject.register(self)
    def notify(self, subject, *args):
        print(type(self).__name__, args, 'az', subject, 'reside ast')

sub = Subject()
obs1 = Observer1(sub)
obs2 = Observer2(sub)
sub.notifyEveryOne('Warning')


#> 2
from abc import ABCMeta, abstractmethod
#Subject
class Publisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestBooks = None
    def register(self, subscriber):
        self.__subscribers.append(subscriber)
    def deregister(self):
        return self.__subscribers.pop()
    def subscribers(self):
        return [type(s).__name__ for s in self.__subscribers]
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()
    def addBooks(self, books):
        self.__latestBooks = books
    def getBooks(self):
        return "Taze haye enteshar: ", self.__latestBooks

#Observer
class Subscriber(metaclass = ABCMeta):
    @abstractmethod
    def update(self):
        pass

#ConcreteObserver1
class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)
    def update(self):
        print(type(self).__name__, self.publisher.getBooks())
#ConcreteObserver2
class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)
    def update(self):
        print(type(self).__name__, self.publisher.getBooks())
#ConcreteObserver3
class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)
    def update(self):
        print(type(self).__name__, self.publisher.getBooks())

if __name__ == '__main__':
    pub = Publisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(pub)
    print("\nSubscribers: ", pub.subscribers())
    pub.addBooks("Advanced python")
    pub.notifySubscribers()
    print("\nUnregistered :", type(pub.deregister()).__name__)
    print("\nSubscribers: ", pub.subscribers)

"""



#< Command >#
"""
#> 1:
class Installer():

    def __init__(self, source, installation_folder):
        self.choices = []
        self.source = source
        self.installation_folder = installation_folder

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying", self.source, "to", self.installation_folder)
            else:
                print("amalyati anjam nashod")

if __name__ == '__main__':
    installer = Installer('python', 'D:')
    installer.preferences({'pyhton': True})
    installer.preferences({'C++': False})
    installer.execute()


#> 2:
from abc import ABCMeta, abstractmethod

#Command
class Command(metaclass = ABCMeta):
    def __init__(self, rec):
        self.rec = rec
    @abstractmethod
    def execute(self):
        pass

#ConcreteCommand
class ConcreteCommand(Command):
    def __init__(self, rec):
        self.rec = rec
    def execute(self):
        self.rec.action()

#Reciever
class Reciever:
    def action(self):
        print("Action")

#Invoker
class Invoker:
    def command(self, com):
        self.com = com
    def execute(self):
        self.com.execute()

if __name__ == '__main__':
    rec = Reciever()
    com = ConcreteCommand(rec)
    invoker = Invoker()
    invoker.command(com)
    invoker.execute()                             


#> 3:
from abc import ABCMeta, abstractmethod
#Command
class Order(metaclass = ABCMeta):
    @abstractmethod
    def execute(self):
        pass

#ConcreteCommand
class BuyHouse(Order):
    def __init__(self, house):
        self.house = house
    def execute(self):
        self.house.buy()

class SellHouse(Order):
    def __init__(self, house):
        self.house = house
    def execute(self):
        self.house.sell()

#Reciever
class HouseTrade:
    def buy(self):
        print("shoma khane ra mikharid")
    def sell(self):
        print("shoma khane ra mifrushid")

#Invoker
class Agent:
    def __init__(self):
        self.__orderQueue = []
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

#Client
if __name__ == '__main__':
    house = HouseTrade()
    buyHouse = BuyHouse(house)
    sellHouse = SellHouse(house)
    #invoker
    agent = Agent()
    agent.placeOrder(buyHouse)
    agent.placeOrder(sellHouse)         

"""



#< Template Method >#
"""
#> 1: Simple
from abc import ABCMeta, abstractmethod
#AbstractClass
class Compiler(metaclass = ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass
    @abstractmethod
    def compileToObject(self):
        pass
    @abstractmethod
    def run(self):
        pass
    #TemplateMethod
    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

#Concrete class
class IOSCompiler(Compiler):
    def collectSource(self):
        print("collecting source code")
    def compileToObject(self):
        print("compiling source code to obj code")
    def run(self):
        print("program running")

ios = IOSCompiler()
ios.compileAndRun()                



#> 2:
from abc import ABCMeta, abstractmethod
class AbstractClass(metaclass = ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def operation1(self):
        pass
    @abstractmethod
    def operation2(self):
        pass
    @abstractmethod
    def operation3(self):
        pass
    def templateMethod(self):
        print("Tartib amaliat in shekli mibashad:aval: operation2, dovom: operation3, sevom: operation1")
        self.operation2()
        self.operation3()
        self.operation1()

class ConcreteClass(AbstractClass):
    def operation1(self):
        print("operation1 anjam shod")
    def operation2(self):
        print("operation2 anjam shod")
    def operation3(self):
        print("operation3 anjam shod")

#Client
class Client():
    def action(self):
        self.concreteClass = ConcreteClass()
        self.concreteClass.templateMethod()

client = Client()
client.action()                       

"""



#< MVS Compund Patter >#
"""
class Model():
    peyks = {
            'KamtarAz30kg'  :{'price':10000},
            '30-70kg'       :{'price':15000},
            '70-100kg'      :{'price':20000},
            'BalatarAz100kg':{'price':30000},
            }

class View():
    def list_peyks(self, peyks):
        for pek in peyks:
            print(pek, '')
    def list_price(self, peyks):
        for pek in peyks :
            print("Hazineye peyk baraye", pek, "mishavad", Model.peyks[pek]['price'])

class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View()
    def get_peyks(self):
        peyks = self.model.peyks.keys()
        return(self.view.list_peyks(peyks))
    def get_price(self):
        peyks = self.model.peyks.keys()
        return(self.view.list_price(peyks))

class Client():
    controller = Controller()
    print("peyk haye mojood")
    controller.get_peyks()
    print("hazineha")
    controller.get_price()                      

"""


#< The State >#
"""
#> 1: Simple
from abc import ABCMeta, abstractmethod

class State(metaclass = ABCMeta):
    @abstractmethod
    def handling(self):
        pass

class ConcreteState1(State):
    def handling(self):
        print("ConcreteState1")
class ConcreteState2(State):
    def handling(self):
        print("ConcreteState2")

class Context(State):
    def __init__(self):
        self.state = None
    def getState(self):
        return self.state
    def setState(self, state):
        self.state = state
    def handling(self):
        self.state.handling()

context = Context()
state1 = ConcreteState1()
state2 = ConcreteState2()
context.setState(state2)
context.handling()                                      


#> 2:
from abc import ABCMeta, abstractmethod

class State(metaclass = ABCMeta):
    @abstractmethod
    def action(self):
        pass

class OpenState(State):
    def action(self):
        print("Darb baste shod")

class CloseState(State):
    def action(self):
        print("Darb baz shod")

class DoorContext(State):
    def __init__(self):
        self.state = None
    def getState(self):
        return self.state
    def setState(self, state):
        self.state = state
    def action(self):
        self.state.action()

context = DoorContext()
context.getState()
open_state = OpenState()
close_state = CloseState()
context.setState(close_state)
context.action()         


#> 3:
#State
class MobileState():
    name = "state"
    allowed = []
    def switch(self, state):
        if state.name in self.allowed:
            print("vaziat konooni: ", self, "tagheer yaft be => ", state.name)
            self.__class__ = state
        else:
            print("vaziat konooni: ", self, "tagheer yaft be => ", state.name, "EMKAN PAZIR NIST")
    def __str__(self):
        return self.name

#ConcreteState
class Off(MobileState):
    name = "Off"
    allowed = ['On']
class On(MobileState):
    name = "On"
    allowed = ['Off', 'Restart', 'Airplane']
class Restart(MobileState):
    name = "Restart"
    allowed = ['On']
class Airplane(MobileState):
    name = "Airplane"
    allowed = ['On', 'Off', 'Restart']

#Context
class MobileContext():
    def __init__(self, model='HTC'):
        self.model = model
        self.state = Off()
    def change(self, state):
        self.state.switch(state)

if __name__ == "__main__":
    mob = MobileContext()
    mob.change(On)
    mob.change(Off)
    mob.change(On)
    mob.change(Restart)
    mob.change(On)
    mob.change(Airplane)
"""
