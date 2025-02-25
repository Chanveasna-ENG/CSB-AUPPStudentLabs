import pandas as pd

class handleText:
    def __init__(self, filename):
        self.text = None
        try:
            file = open(filename, "r")
            self.text = file.read()
            file.close()
        except FileNotFoundError:
            print('File not found')
            return
        except:
            print('There was an Error loading the file')
            return
        
    def analyze_content(self):
        if self.text is None:
            return 'There was an error loading the file'
        self.nChars = len(self.text)
        self.nWords = len(self.text.split())
        self.nSimilar = len(set(self.text.split()))
        self.nLine = len(self.text.splitlines())
    
    def generate_summary(self):
        if self.text is None:
            return 'There was an error loading the file'
        return f'Word count: {self.nWords}\nCharacter count: {self.nChars}\nLine count: {self.nLine}\nSimilar count: {self.nSimilar}'

class handleCSV:
    def __init__(self, filename):
        self.data = None
        try:
            self.data = pd.read_csv(filename)
        except FileNotFoundError:
            print('File not found')
            return
        except:
            print('There was an Error loading the file')
            return

    def generate_summary(self):
        if self.data is None:
            return 'There was an error loading the file'
        return self.data.describe(include='all')

class handleExcel:
    def __init__(self, filename):
        self.data = None
        try:
            self.data = pd.read_excel(filename)
        except FileNotFoundError:
            print('File not found')
            exit(1)
        except:
            print('There was an Error loading the file')
            exit(1)
    def generate_summary(self):
        if self.data is None:
            return 'There was an error loading the file'
        return self.data.describe()