PI=3.1415926

class Person:
    '''
    我是person
    '''

    def __init__(self,name:str,age:int):
        self.name = name #attribute
        self.age = age #attribute

    #實體方法(instance method)
    def echo(self):
        print(f'我的姓名是:{self.name}')
        print(f'我的age是:{self.age}')

class Student(Person):
    '''
    我是Student
    '''
    def __init__(self,name:str,age:int,score:int):
        super().__init__(name=name,age=age)
        self.__score = score

    @property
    def score(self)->int:
        return self.__score

    def echo(self):
        super().echo()
        print(f'我的score是:{self.score}')


def get_status(bmi:float)->str:
    '''
    docstring
    Parameter:
        bmi:bmi值可以整數或浮點數
    Return:str
        會傳出5個狀態
        - 正常範圍
        - 過重 
        - 輕度肥胖      
    '''
    if bmi >= 35 :
        bmi_str = '重度肥胖'
    elif bmi >= 30 :
        bmi_str = '中度肥胖'
    elif bmi >= 27 :
        bmi_str = '輕度肥胖'
    elif bmi >= 24 :
        bmi_str = '過重'
    elif bmi >= 18.5 :
        bmi_str = '正常範圍'
    else :
        bmi_str = '過輕' 
    return bmi_str
    
def BMI_math(height_cm:float, weight_kg:float)->tuple[float,str]:
    height_m = round(height_cm/100, 2)
    bmi_kg_m2 = round(weight_kg/(height_m**2), 2)
    bmi_str = get_status(bmi_kg_m2)
    return bmi_kg_m2, bmi_str


class BMI:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height 
        self.weight = weight

    def get_BMI(self):
        height_in_meters = self.height / 100
        bmi = self.weight / (height_in_meters ** 2)
        return round(bmi, 2)

    def get_status(self):
        bmi_value = self.get_BMI()
        if bmi_value < 18.5:
            return "你是一隻瘦皮猴~"
        elif 18.5 <= bmi_value < 24:
            return "嘟嘟好~"
        elif 24 <= bmi_value < 27:
            return "有一點超重喔~"
        elif 27 <= bmi_value < 30:
            return "輕量級胖胖~"
        elif 30 <= bmi_value < 35:
            return "中量級胖胖~"
        else:
            return "重量級胖胖~"

        