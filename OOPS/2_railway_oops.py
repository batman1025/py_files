class RailwayForm():
    formType = "RailwayForm"
    def pdata(self):
        print(f"Name is {self.name}")
        print(f"Train Name is {self.train}")
    
avikApp = RailwayForm()
avikApp.name = input("Enter Your Name : ")
avikApp.train = input("Enter Your Train Name : ")
avikApp.pdata()