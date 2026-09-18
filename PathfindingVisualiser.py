import math
import sys
import random

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
)

from PyQt6.QtCore import (
    Qt
)

from screeninfo import (
    get_monitors
)


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.MenuWindow()
        self.TutorialInfo()
        self.MainProgramRun()
        self.setGeometry(0, 20, 1500, 750)
        self.setWindowTitle('Pathfinding Algorithm Visualiser App')

    def MenuWindow(self):
        layout = QGridLayout()
        self.setLayout(layout)
        self.title = QLabel('Pathfinding Algorithm Visualiser')
        self.title.setProperty("class", "Title")
        layout.addWidget(self.title, 0, 1)

        mainPageButton = QPushButton('Main Application')
        tutorialButton = QPushButton('Tutorial')

        mainPageButton.setProperty("class", "menubutton")
        tutorialButton.setProperty("class", "menubutton")

        layout.addWidget(mainPageButton, 1, 0)
        layout.addWidget(tutorialButton, 1, 2)

        tutorialButton.clicked.connect(lambda checked: self.showWindow(self.tutorial1))
        tutorialButton.clicked.connect(self.close)
        mainPageButton.clicked.connect(lambda checked: self.showWindow(self.mainProgram))
        mainPageButton.clicked.connect(self.close)

    def TutorialInfo(self):
        self.tutorial1 = Tutorial()
        self.tutorial1.tutorialText('''
Hello and welcome to my Pathfinding Algorithm Visualiser.
Click return or skip to navigate to the main menu.
Click back or next to flick between the tutorial slides.
        ''')
        self.tutorial1.nextButton.clicked.connect(lambda checked: self.showWindow(self.tutorial2))
        self.tutorial1.nextButton.clicked.connect(self.tutorial1.close)
        self.tutorial1.backButton.setText('Return')
        self.tutorial1.backButton.clicked.connect(self.tutorial1.close)
        self.tutorial1.backButton.clicked.connect(self.show)
        self.tutorial1.skipButton.clicked.connect(self.tutorial1.close)
        self.tutorial1.skipButton.clicked.connect(self.showMaximized)

        self.tutorial2 = Tutorial()
        self.tutorial2.tutorialText('''
Good job! Nice button clicking skills you have there :)
Once you finish this tutorial or decide to skip, 
please click the Main Application button to get started
        ''')
        self.tutorial2.nextButton.clicked.connect(lambda checked: self.showWindow(self.tutorial3))
        self.tutorial2.nextButton.clicked.connect(self.tutorial2.close)
        self.tutorial2.backButton.clicked.connect(lambda checked: self.showWindow(self.tutorial1))
        self.tutorial2.backButton.clicked.connect(self.tutorial2.close)
        self.tutorial2.skipButton.clicked.connect(self.tutorial2.close)
        self.tutorial2.skipButton.clicked.connect(self.showMaximized)

        self.tutorial3 = Tutorial()
        self.tutorial3.tutorialText('''
Once you are on the main application,
You can choose to draw your own mazes for the pathfinding algorithms
(Or use the random maze generators provided in the Maze Generation Tab)
to traverse through.
        ''')
        self.tutorial3.nextButton.clicked.connect(lambda checked: self.showWindow(self.tutorial4))
        self.tutorial3.nextButton.clicked.connect(self.tutorial3.close)
        self.tutorial3.backButton.clicked.connect(lambda checked: self.showWindow(self.tutorial2))
        self.tutorial3.backButton.clicked.connect(self.tutorial3.close)
        self.tutorial3.skipButton.clicked.connect(self.tutorial3.close)
        self.tutorial3.skipButton.clicked.connect(self.showMaximized)

        self.tutorial4 = Tutorial()
        self.tutorial4.tutorialText('''
Once you have chosen your maze or have drawn your own,
please navigate to the Algorithm Picker tab 
to choose the algorithm you would like to see.\n
After you have chosen the algorithm, 
Click start/stop to watch it in action.
Click clear Maze or generate a new maze to view another algorithm in action.
        ''')
        self.tutorial4.backButton.clicked.connect(lambda checked: self.showWindow(self.tutorial3))
        self.tutorial4.backButton.clicked.connect(self.tutorial4.close)
        self.tutorial4.nextButton.clicked.connect(self.tutorial4.close)
        self.tutorial4.nextButton.clicked.connect(lambda checked: self.showWindow(self.tutorial5))
        self.tutorial4.skipButton.clicked.connect(self.tutorial4.close)
        self.tutorial4.skipButton.clicked.connect(self.showMaximized)

        self.tutorial5 = Tutorial()
        self.tutorial5.tutorialText('''
The 'x's displayed show the path that the 
Pathfinding Algorithms found the shortest.\n
The 'o's displayed show the the nodes that the
Pathfinding Algorithms searched.\n
However, as you will see, not all algorithms
Find the shortest paths.
        ''')

        self.tutorial5.backButton.clicked.connect(lambda checked: self.showWindow(self.tutorial4))
        self.tutorial5.backButton.clicked.connect(self.tutorial5.close)
        self.tutorial5.nextButton.clicked.connect(self.tutorial5.close)
        self.tutorial5.nextButton.clicked.connect(lambda checked: self.showWindow(self.tutorial6))
        self.tutorial5.skipButton.clicked.connect(self.tutorial5.close)
        self.tutorial5.skipButton.clicked.connect(self.showMaximized)

        self.tutorial6 = Tutorial()
        self.tutorial6.tutorialText('''
With that said, what is a pathfinding algorithm exactly?
Pathfinding algorithms are a graph searching tool
which is used to find the shortest distance between
two chosen nodes by traversing the graph. 

These are often used in many modern day apps such as
google maps. The premise of the creation of this app 
is to help people visualise how some of the most popular 
algorithms traverse across mazes.

Don't forget to have fun!
         ''')
        self.tutorial6.backButton.clicked.connect(lambda checked: self.showWindow(self.tutorial5))
        self.tutorial6.backButton.clicked.connect(self.tutorial6.close)
        self.tutorial6.nextButton.setText('Finish')
        self.tutorial6.nextButton.clicked.connect(self.tutorial6.close)
        self.tutorial6.nextButton.clicked.connect(self.showMaximized)
        self.tutorial6.skipButton.clicked.connect(self.tutorial6.close)
        self.tutorial6.skipButton.clicked.connect(self.showMaximized)

    def MainProgramRun(self):
        self.mainProgram = MainProgram()
        self.mainProgram.setProperty("class", "mainProgram")
        self.mainProgram.returnButton.clicked.connect(self.close)
        self.mainProgram.optionsLayout.addWidget(self.mainProgram.returnButton)
        self.mainProgram.returnButton.clicked.connect(self.mainProgram.close)
        self.mainProgram.returnButton.clicked.connect(self.showMaximized)

    def showWindow(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.showMaximized()


class MainProgram(QWidget):
    def __init__(self):
        super().__init__()
        self.MainProgramWindow()
        self.mainProgramGrid()
        self.AlgorithmPicker()
        self.MazePicker()
        self.isPerfectMaze = False
        self.isImperfectMaze = False
        self.hasStarted = False
        self.setGeometry(0, 0, 1500, 750)
        #self.setFixedSize(1500, 850)
        self.setWindowTitle('Pathfinding Algorithm Visualiser')

    def MainProgramWindow(self):
        pageLayout = QHBoxLayout()
        self.optionsLayout = QVBoxLayout()
        self.mainLayout = QGridLayout()
        mainButtonLayout = QHBoxLayout()
        mainTitleLayout = QHBoxLayout()
        self.setLayout(pageLayout)
        self.makeEmptyGrid()

        mainTitle = QLabel('Pathfinding Algorithm Visualiser')
        mainTitle.setProperty("class", "mainTitle")
        mainTitleLayout.addWidget(mainTitle, alignment=Qt.AlignmentFlag.AlignHCenter)

        pageLayout.addLayout(self.mainLayout)
        pageLayout.addLayout(self.optionsLayout)
        self.mainLayout.addLayout(mainButtonLayout, 2, 1)
        self.mainLayout.addLayout(mainTitleLayout, 0, 1)

        AlgorithmPickerButton = QPushButton('Algorithm Picker')
        AlgorithmPickerButton.setProperty("class", "menubutton")
        self.optionsLayout.addWidget(AlgorithmPickerButton)

        MazeGenerator = QPushButton('Maze Generation')
        MazeGenerator.setProperty("class", "menubutton")
        self.optionsLayout.addWidget(MazeGenerator)

        self.start = QPushButton('Start')
        self.start.clicked.connect(lambda: self.startPathfindingAlgorithms())
        mainButtonLayout.addWidget(self.start)
        self.start.setProperty("class", "menubutton")

        clear = QPushButton('Clear Maze')
        clear.clicked.connect(self.makeEmptyGrid)
        mainButtonLayout.addWidget(clear)
        clear.setProperty("class", "menubutton")

        self.returnButton = QPushButton('Return')
        self.returnButton.setProperty("class", "menubutton")

        AlgorithmPickerButton.clicked.connect(lambda checked: self.showWindow(self.algorithmsScreen))
        AlgorithmPickerButton.clicked.connect(lambda checked: self.closeOtherWindow(self.mazeGeneratorScreen))
        AlgorithmPickerButton.clicked.connect(lambda checked: self.closeOtherWindow(self.algorithmsScreen.info))

        MazeGenerator.clicked.connect(lambda checked: self.showWindow(self.mazeGeneratorScreen))
        MazeGenerator.clicked.connect(lambda checked: self.closeOtherWindow(self.algorithmsScreen))
        MazeGenerator.clicked.connect(lambda checked: self.closeOtherWindow(self.algorithmsScreen.info))

    def closeEvent(self, event):
        # closes all windows when this one is exited
        QApplication.closeAllWindows()

    def mainProgramGrid(self):
        self.mainGrid = Grid()
        self.mainGrid.blankGrid(self.mainGrid.grid)

    def AlgorithmPicker(self):
        self.algorithmsScreen = AlgorithmPicker()
        self.Dijkstra = False
        self.BiDirectionalDijkstra = False
        self.Greedy = False

        self.algorithmsScreen.dijkstraButton.clicked.connect(lambda: self.setDijkstraTrue())
        self.algorithmsScreen.bidirectionalDijkstraButton.clicked.connect(lambda: self.setBiDirectionalDijkstraTrue())
        self.algorithmsScreen.greedyButton.clicked.connect(lambda: self.setGreedyTrue())
        self.algorithmsScreen.returnButton.clicked.connect(self.algorithmsScreen.close)
    def setDijkstraTrue(self):
        self.algorithmsScreen.dijkstraButton.setText("Dijkstra's Algorithm\nChosen")
        self.algorithmsScreen.bidirectionalDijkstraButton.setText("Bi-Directional Dijkstra's\nAlgorithm")
        self.algorithmsScreen.greedyButton.setText("Greedy Best First Search")
        self.start.setText('Start')
        self.Dijkstra = True
        self.BiDirectionalDijkstra = False
        self.Greedy = False

    def setBiDirectionalDijkstraTrue(self):
        self.algorithmsScreen.dijkstraButton.setText("Dijkstra's Algorithm")
        self.algorithmsScreen.bidirectionalDijkstraButton.setText("Bi-Directional Dijkstra's\nAlgorithm Chosen")
        self.algorithmsScreen.greedyButton.setText("Greedy Best First Search")
        self.start.setText('Start')
        self.Dijkstra = False
        self.BiDirectionalDijkstra = True
        self.Greedy = False

    def setGreedyTrue(self):
        self.algorithmsScreen.dijkstraButton.setText("Dijkstra's Algorithm")
        self.algorithmsScreen.bidirectionalDijkstraButton.setText("Bi-Directional Dijkstra's\nAlgorithm")
        self.algorithmsScreen.greedyButton.setText("Greedy Best First Search\nChosen")
        self.start.setText('Start')
        self.Dijkstra = False
        self.BiDirectionalDijkstra = False
        self.Greedy = True

    def startPathfindingAlgorithms(self):
        def showDijkstra(gridType):
            self.mainGrid = Grid()
            self.mainGrid.dijkstra(gridType)
            self.mainLayout.addWidget(self.mainGrid, 1, 1)
            self.mainGrid = Grid()
            self.mainGrid.blankGrid(self.mainGrid.grid)
            self.hasStarted = True

        def showBiDirectionalDijkstra(gridType):
            self.mainGrid = Grid()
            self.mainGrid.BiDirectionalDijkstra(gridType)
            self.mainLayout.addWidget(self.mainGrid, 1, 1)
            self.mainGrid = Grid()
            self.mainGrid.blankGrid(self.mainGrid.grid)
            self.hasStarted = True

        def showGreedy(gridType):
            self.mainGrid = Grid()
            self.mainGrid.Greedy(gridType)
            self.mainLayout.addWidget(self.mainGrid, 1, 1)
            self.mainGrid = Grid()
            self.mainGrid.blankGrid(self.mainGrid.grid)
            self.hasStarted = True

        if not self.Dijkstra and not self.BiDirectionalDijkstra and not self.Greedy:
            self.start.setText('Choose Algorithm')

        if self.Dijkstra and self.noMaze:
            self.emptyGridCopy = [[self.emptyGrid[x][y] for y in range(len(self.emptyGrid[0]))] for x in
                                  range(len(self.emptyGrid))]
            showDijkstra(self.emptyGrid)
            self.emptyGrid = [[self.emptyGridCopy[x][y] for y in range(len(self.emptyGridCopy[0]))] for x in
                              range(len(self.emptyGridCopy))]

        elif self.Dijkstra and self.isPerfectMaze:
            self.perfectCopy = [[self.perfect[x][y] for y in range(len(self.perfect[0]))] for x in
                                range(len(self.perfect))]
            showDijkstra(self.perfect)
            self.perfect = [[self.perfectCopy[x][y] for y in range(len(self.perfectCopy[0]))] for x in
                            range(len(self.perfectCopy))]

        elif self.Dijkstra and self.isImperfectMaze:
            self.imperfectCopy = [[self.imperfect[x][y] for y in range(len(self.imperfect[0]))] for x in
                                  range(len(self.imperfect))]
            showDijkstra(self.imperfect)
            self.imperfect = [[self.imperfectCopy[x][y] for y in range(len(self.imperfectCopy[0]))] for x in
                              range(len(self.imperfectCopy))]

        if self.BiDirectionalDijkstra and self.noMaze:
            self.emptyGridCopy = [[self.emptyGrid[x][y] for y in range(len(self.emptyGrid[0]))] for x in
                                  range(len(self.emptyGrid))]
            showBiDirectionalDijkstra(self.emptyGrid)
            self.emptyGrid = [[self.emptyGridCopy[x][y] for y in range(len(self.emptyGridCopy[0]))] for x in
                              range(len(self.emptyGridCopy))]

        elif self.BiDirectionalDijkstra and self.isPerfectMaze:
            self.perfectCopy = [[self.perfect[x][y] for y in range(len(self.perfect[0]))] for x in
                                range(len(self.perfect))]
            showBiDirectionalDijkstra(self.perfect)
            self.perfect = [[self.perfectCopy[x][y] for y in range(len(self.perfectCopy[0]))] for x in
                            range(len(self.perfectCopy))]

        elif self.BiDirectionalDijkstra and self.isImperfectMaze:
            self.imperfectCopy = [[self.imperfect[x][y] for y in range(len(self.imperfect[0]))] for x in
                                  range(len(self.imperfect))]
            showBiDirectionalDijkstra(self.imperfect)
            self.imperfect = [[self.imperfectCopy[x][y] for y in range(len(self.imperfectCopy[0]))] for x in
                              range(len(self.imperfectCopy))]

        if self.Greedy and self.noMaze:
            self.emptyGridCopy = [[self.emptyGrid[x][y] for y in range(len(self.emptyGrid[0]))] for x in
                                  range(len(self.emptyGrid))]
            showGreedy(self.emptyGrid)
            self.emptyGrid = [[self.emptyGridCopy[x][y] for y in range(len(self.emptyGridCopy[0]))] for x in
                              range(len(self.emptyGridCopy))]

        elif self.Greedy and self.isPerfectMaze:
            self.perfectCopy = [[self.perfect[x][y] for y in range(len(self.perfect[0]))] for x in
                                range(len(self.perfect))]
            showGreedy(self.perfect)
            self.perfect = [[self.perfectCopy[x][y] for y in range(len(self.perfectCopy[0]))] for x in
                            range(len(self.perfectCopy))]

        elif self.Greedy and self.isImperfectMaze:
            self.imperfectCopy = [[self.imperfect[x][y] for y in range(len(self.imperfect[0]))] for x in
                                  range(len(self.imperfect))]
            showGreedy(self.imperfect)
            self.imperfect = [[self.imperfectCopy[x][y] for y in range(len(self.imperfectCopy[0]))] for x in
                              range(len(self.imperfectCopy))]

    def makeEmptyGrid(self):
        self.mainGrid = Grid()
        self.emptyGrid = self.mainGrid.blankGrid(self.mainGrid.grid)
        self.mainLayout.addWidget(self.mainGrid, 1, 1)
        self.mainGrid = Grid()
        self.mainGrid.blankGrid(self.mainGrid.grid)
        self.isPerfectMaze = False
        self.isImperfectMaze = False
        self.noMaze = True

    def MazePicker(self):
        self.mazeGeneratorScreen = MazePicker()
        self.mazeGeneratorScreen.perfectMaze.clicked.connect(lambda: self.updatePerfectGrid(self.mainGrid.grid))
        self.mazeGeneratorScreen.imperfectMaze.clicked.connect(lambda: self.updateImperfectGrid(self.mainGrid.grid))
        self.mazeGeneratorScreen.returnButton.clicked.connect(self.mazeGeneratorScreen.close)

    def updatePerfectGrid(self, newGrid):
        self.mainGrid = Grid()
        self.perfect = self.mainGrid.createMaze(newGrid, 'perfect')
        self.mainLayout.addWidget(self.mainGrid, 1, 1)
        self.mainGrid = Grid()
        self.mainGrid.blankGrid(self.mainGrid.grid)
        self.isPerfectMaze = True
        self.isImperfectMaze = False
        self.noMaze = False

    def updateImperfectGrid(self, newGrid):
        self.mainGrid = Grid()
        self.imperfect = self.mainGrid.createMaze(newGrid, 'imperfect')
        self.mainGrid.createMaze(newGrid, 'imperfect')
        self.mainLayout.addWidget(self.mainGrid, 1, 1)
        self.mainGrid = Grid()
        self.mainGrid.blankGrid(self.mainGrid.grid)
        self.isImperfectMaze = True
        self.isPerfectMaze = False
        self.noMaze = False

    def closeOtherWindow(self, windowToCheck):
        if windowToCheck.isVisible():
            windowToCheck.hide()

    def showWindow(self, window):
        if window.isVisible():
            window.hide()
            window.show()
        else:
            window.show()


class Tutorial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tutorial')
        self.setGeometry(0, 0, 1500, 750)

        self.layout = QGridLayout()
        bottomButtonsLayout = QHBoxLayout()
        skipButtonLayout = QHBoxLayout()
        self.layout.addLayout(skipButtonLayout, 0, 0)
        self.layout.addLayout(bottomButtonsLayout, 2, 0)
        self.setLayout(self.layout)

        self.backButton = QPushButton('Back')
        self.nextButton = QPushButton('Next')
        self.skipButton = QPushButton('Skip')

        self.backButton.setProperty("class", "tutorialButton")
        self.nextButton.setProperty("class", "tutorialButton")
        self.skipButton.setProperty("class", "skipButton")

        bottomButtonsLayout.addWidget(self.backButton)
        bottomButtonsLayout.addWidget(self.nextButton)
        skipButtonLayout.addWidget(self.skipButton, alignment=Qt.AlignmentFlag.AlignRight)

    def tutorialText(self, info):
        text = info
        tutorialText = QLabel(text)
        tutorialText.setProperty("class", "tutorialText")
        tutorialText.setStyleSheet(f"qproperty-alignment: {int(Qt.AlignmentFlag.AlignLeft)};")
        self.layout.addWidget(tutorialText, 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)


class AlgorithmPicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1090, 29, 747, 949)
        self.setFixedSize(417, 850)
        self.setWindowTitle('AlgorithmPickerTab')

        layout = QVBoxLayout()
        self.setLayout(layout)

        algorithmlayout = QVBoxLayout()
        infoLayout = QHBoxLayout()

        self.info = InfoScreen()

        infoButton = QPushButton('Info')
        infoButton.setProperty("class", "mazeAndAlgorithmButton")
        infoButton.clicked.connect(lambda: self.info.showWindow(self.info))
        infoLayout.addWidget(infoButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.dijkstraButton = QPushButton("Dijkstra's Algorithm")
        self.dijkstraButton.setProperty("class", "mazeAndAlgorithmButton")
        algorithmlayout.addWidget(self.dijkstraButton, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.greedyButton = QPushButton("Greedy Best First Search")
        self.greedyButton.setProperty("class", "mazeAndAlgorithmButton")
        algorithmlayout.addWidget(self.greedyButton, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.bidirectionalDijkstraButton = QPushButton("Bi-Directional Dijkstra's\nAlgorithm")
        self.bidirectionalDijkstraButton.setProperty("class", "mazeAndAlgorithmButton")
        algorithmlayout.addWidget(self.bidirectionalDijkstraButton, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.returnButton = QPushButton('Return')
        self.returnButton.setProperty("class", "mazeAndAlgorithmButton")
        self.returnButton.clicked.connect(self.close)
        algorithmlayout.addWidget(self.returnButton, alignment=Qt.AlignmentFlag.AlignVCenter)

        layout.addLayout(infoLayout)
        layout.addLayout(algorithmlayout)

    def closeInfo(self):
        self.info.close()


class MazePicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1090, 29, 747, 949)
        self.setFixedSize(417, 850)
        self.setWindowTitle('Maze Generator Tab')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.perfectMaze = QPushButton('Perfect Maze Generator')
        self.perfectMaze.setProperty("class", "mazeAndAlgorithmButton")
        self.layout.addWidget(self.perfectMaze)

        self.imperfectMaze = QPushButton('Imperfect Maze Generator')
        self.imperfectMaze.setProperty("class", "mazeAndAlgorithmButton")
        self.layout.addWidget(self.imperfectMaze)

        self.returnButton = QPushButton('Return')
        self.returnButton.setProperty("class", "mazeAndAlgorithmButton")
        self.returnButton.clicked.connect(self.close)
        self.layout.addWidget(self.returnButton)


class InfoScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1090, 29, 747, 949)
        self.setFixedSize(417, 850)
        self.setWindowTitle('Algorithm Information Tab')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.dijkstraInfo = QLabel('''
Dijkstra's Algorithm works by viewing 
each cell around it one at a time equally.
As a result, it will always find the
shortest path of any maze. It works for
both directed and undirected mazes.
However, it only works for weighted 
graphs.
        ''')
        self.dijkstraInfo.setProperty("class", "InfoText")
        self.layout.addWidget(self.dijkstraInfo)

        self.greedyInfo = QLabel('''
Greedy Best First Search uses a heuristic 
approach by utilising the distance 
between the current node and the end 
node. The algorithm uses this to only 
explore nodes that are as close as 
possible to the end node. As a result
it is weighted and may not find the 
shortest path.
        ''')
        self.greedyInfo.setProperty("class", "InfoText")
        self.layout.addWidget(self.greedyInfo)

        self.bidirectionalDijkstraInfo = QLabel('''
Like the singular version, it is also 
weighted. However, Bidirectional
Dijkstra may not find the shortest 
path. It works by simultaneously 
carrying out two searches: one from 
the start node and one from the end 
node. The stopping condition for this 
version is where these searches meet.
        ''')
        self.bidirectionalDijkstraInfo.setProperty("class", "InfoText")
        self.layout.addWidget(self.bidirectionalDijkstraInfo)

        self.returnButton = QPushButton('Return')
        self.returnButton.setProperty("class", "mazeAndAlgorithmButton")
        self.returnButton.clicked.connect(self.close)
        self.layout.addWidget(self.returnButton)

    def showWindow(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()


class Grid(QWidget):
    def __init__(self):
        super().__init__()

        #change this to the specs of the screen being used
        for monitors in get_monitors():
            screenWidth = monitors.width
            screenHeight = monitors.height

        gridHeight = math.trunc(15.4687*math.log10(screenHeight)-35.8142)
        gridWidth = math.trunc(15.4687*math.log10(screenWidth*1.37)-35.8142)

        if gridHeight % 2 ==0:
            self.rowLength = gridHeight - 1
            self.columnLength = gridWidth -1
        else:
            self.rowLength = gridHeight
            self.columnLength = gridWidth

        self.gridLayout = QGridLayout()
        self.setLayout(self.gridLayout)
        self.gridLayout.setSpacing(0)
        self.grid = []
        self.createGrid()

    def createGrid(self):
        for rows in range(1, self.rowLength + 1):
            row = []
            for columns in range(1, self.columnLength + 1):
                row.append('  ')
            self.grid.append(row)

        # border
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                if i == 0 or i == (len(self.grid) - 1):
                    self.grid[i][j] = '# '
                else:
                    if j == 0 or j == (len(self.grid[i]) - 1):
                        self.grid[i][j] = '# '
        return self.grid

    def blankGrid(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '# ':
                    border = QPushButton('start')
                    border.setProperty('class', 'border')
                    self.gridLayout.addWidget(border, i, j)

                if self.grid[i][j] == '  ':
                    space = QPushButton('  ')
                    space.setProperty('class', 'space')
                    space.clicked.connect(lambda _, i=i, j=j: changeToWall(grid, i, j))
                    self.gridLayout.addWidget(space, i, j)

                if i == 1 and j == 1:
                    start = QPushButton('start')
                    start.setProperty('class', 'space')
                    self.gridLayout.addWidget(start, i, j)

                if i == self.rowLength - 2 and j == self.columnLength - 2:
                    end = QPushButton('end')
                    end.setProperty('class', 'space')
                    self.gridLayout.addWidget(end, i, j)

        def changeToWall(grid, row, column):
            grid[row][column] = 'X '
            wall = QPushButton('  ')
            wall.setProperty('class', 'wall')
            wall.clicked.connect(lambda: changeToPath(grid, row, column))
            self.gridLayout.addWidget(wall, row, column)

        def changeToPath(grid, row, column):
            grid[row][column] = '  '
            space = QPushButton('  ')
            space.setProperty('class', 'space')
            space.clicked.connect(lambda: changeToWall(grid, row, column))
            self.gridLayout.addWidget(space, row, column)

        return grid

    def createMaze(self, grid, mazetype):
        usedNums = []
        # assigning random numbers to each node as weights
        nodeNum = 1
        for i in range(1, self.rowLength - 1):
            for j in range(1, self.columnLength - 1):
                uniqueNum = False
                while not uniqueNum:
                    randomNum = random.randint(0, (self.rowLength - 2) * (self.columnLength - 2) - 1)
                    if randomNum in usedNums:
                        randomNum = random.randint(0, (self.rowLength - 2) * (self.columnLength - 2) - 1)
                    else:
                        uniqueNum = True
                        usedNums.append(randomNum)

                if (i % 2 == 0) or (j % 2 == 0):
                    if (j % 2 == 1) or (j % 2 == 0):
                        grid[i][j] = str(randomNum)
                else:
                    grid[i][j] = 'n' + str(nodeNum)
                    nodeNum += 1

        #create adjacency list
        adjList = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                # creating an adjacency list
                if grid[i][j][0] == 'n':
                    node = []
                    node.append(grid[i][j])

                    # check right
                    if grid[i][j + 1].isdigit():
                        node.append(int(grid[i][j + 1]))
                    else:
                        node.append(999)

                    # check up
                    if grid[i - 1][j].isdigit():
                        node.append(int(grid[i - 1][j]))
                    else:
                        node.append(999)

                    # check left
                    if grid[i][j - 1].isdigit():
                        node.append(int(grid[i][j - 1]))
                    else:
                        node.append(999)

                    # check down
                    if grid[i + 1][j].isdigit():
                        node.append(int(grid[i + 1][j]))
                    else:
                        node.append(999)

                    adjList.append(node)

        #generate maze
        visited = []
        seen = []
        seen.append(adjList[0])
        for d in range(0, int((self.rowLength * self.columnLength) * 2)):
            smallest = 999
            for i in range(0, len(seen)):
                for j in range(1, len(seen[i])):
                    if seen[i][j] < smallest and seen[i][j] not in visited:
                        smallest = seen[i][j]

            #updates smallest
            if smallest not in visited:
                visited.append(smallest)

            #finds connected node
            for i in range(len(adjList)):
                for j in range(len(adjList[i])):
                    if adjList[i][j] == smallest:
                        if adjList[i] not in seen:
                            seen.append(adjList[i])

            # removes smallest
            for i in range(1, len(grid) - 1):
                for j in range(1, len(grid[i]) - 1):
                    if grid[i][j].isdigit():
                        if int(grid[i][j]) == smallest:
                            if (grid[i + 1][j] == '   ' and grid[i - 1][j] == '   ') or (
                                    grid[i][j + 1] == '   ' and grid[i][j - 1] == '   '):
                                pass
                            else:
                                grid[i][j] = '   '

            # removes the connecting cell
            for k in range(0, len(seen)):
                for i in range(0, len(grid)):
                    for j in range(0, len(grid[i])):
                        if grid[i][j] in seen[k]:
                            grid[i][j] = '   '

        # formatting grid
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j].isdigit():
                    grid[i][j] = 'X '
                elif grid[i][j] == '   ':
                    grid[i][j] = '  '
                else:
                    grid[i][j] = '# '

        #making imperfect
        if mazetype == 'imperfect':
            # if the breakWall hits this number, the wall will disappear
            breakNumber = 3
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    breakWall = random.randint(1, 3)
                    if breakWall == breakNumber:
                        if grid[i][j] == 'X ' and grid[i + 1][j] == '  ' and grid[i - 1][j] == '  ':
                            if grid[i][j + 1] == 'X ' and grid[i][j - 1] == 'X ':
                                grid[i][j] = '  '

                        elif grid[i][j] == 'X ' and grid[i][j + 1] == '  ' and grid[i][j - 1] == '  ':
                            if grid[i + 1][j] == 'X ' and grid[i - 1][j] == 'X ':
                                grid[i][j] = '  '

        #displaying maze
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '# ':
                    border = QPushButton('  ')
                    border.setProperty('class', 'border')
                    self.gridLayout.addWidget(border, i, j)
                if grid[i][j] == '  ':
                    space = QPushButton('  ')
                    space.setProperty('class', 'space')
                    space.clicked.connect(lambda _, i=i, j=j: changeToWall(grid, i, j))
                    self.gridLayout.addWidget(space, i, j)
                if grid[i][j] == 'X ':
                    wall = QPushButton('  ')
                    wall.setProperty('class', 'wall')
                    wall.clicked.connect(lambda _, i=i, j=j: changeToPath(grid, i, j))
                    self.gridLayout.addWidget(wall, i, j)

                if i == 1 and j == 1:
                    start = QPushButton('start')
                    start.setProperty('class', 'space')
                    self.gridLayout.addWidget(start, i, j)

                if i == self.rowLength - 2 and j == self.columnLength - 2:
                    end = QPushButton('end')
                    end.setProperty('class', 'space')
                    self.gridLayout.addWidget(end, i, j)

        def changeToWall(grid, row, column):
            grid[row][column] = 'X '
            wall = QPushButton('  ')
            wall.setProperty('class', 'wall')
            wall.clicked.connect(lambda: changeToPath(grid, row, column))
            self.gridLayout.addWidget(wall, row, column)

        def changeToPath(grid, row, column):
            grid[row][column] = '  '
            space = QPushButton('  ')
            space.setProperty('class', 'space')
            space.clicked.connect(lambda: changeToWall(grid, row, column))
            self.gridLayout.addWidget(space, row, column)

        return grid

    def dijkstra(self, grid):
        # giving each space a number to refer back to
        grid[1][1] = '00'
        visited = [0]
        self.loopCounter = 0
        # continues until the last node is not found
        while not grid[self.rowLength-2][self.columnLength-2].isdigit():
            self.loopCounter += 1
            # adding the distances of each node from the start node
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    # checking if the end node has been found
                    if grid[i][j].isdigit():
                        if int(grid[i][j]) in visited:
                            if grid[i][j + 1] == '  ':
                                grid[i][j + 1] = str(int(grid[i][j]) + 1)

                            if grid[i + 1][j] == '  ':
                                grid[i + 1][j] = str(int(grid[i][j]) + 1)

                            if grid[i][j - 1] == '  ':
                                grid[i][j - 1] = str(int(grid[i][j]) + 1)

                            if grid[i - 1][j] == '  ':
                                grid[i - 1][j] = str(int(grid[i][j]) + 1)

            if self.loopCounter == 150:
                break
            visited.append(visited[-1] + 1)

        if self.loopCounter != 150:
            endNode = grid[self.rowLength - 2][self.columnLength - 2]
            temp = int(endNode)
            # adding the end node to the shortest path
            grid[self.rowLength - 2][self.columnLength - 2] = '. '
            for loop in range(0, int(endNode)):
                # adding the distances of each node from the start node
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        if grid[i][j] == '. ':
                            if grid[i][j + 1].isdigit():
                                if int(grid[i][j + 1]) == temp - 1:
                                    grid[i][j + 1] = '. '
                                    temp -= 1

                            if grid[i + 1][j].isdigit():
                                if int(grid[i + 1][j]) == temp - 1:
                                    grid[i + 1][j] = '. '
                                    temp -= 1

                            if grid[i][j - 1].isdigit():
                                if int(grid[i][j - 1]) == temp - 1:
                                    grid[i][j - 1] = '. '
                                    temp -= 1

                            if grid[i - 1][j].isdigit():
                                if int(grid[i - 1][j]) == temp - 1:
                                    grid[i - 1][j] = '. '
                                    temp -= 1

        # formatting grid
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '# ':
                    border = QPushButton('  ')
                    border.setProperty('class', 'border')
                    self.gridLayout.addWidget(border, i, j)
                if grid[i][j] == '  ':
                    space = QPushButton('  ')
                    space.setProperty('class', 'space')
                    self.gridLayout.addWidget(space, i, j)

                if grid[i][j] == 'X ':
                    wall = QPushButton('  ')
                    wall.setProperty('class', 'wall')
                    self.gridLayout.addWidget(wall, i, j)

                if grid[i][j] == '. ':
                    wall = QPushButton('x')
                    wall.setProperty('class', 'spacePath')
                    self.gridLayout.addWidget(wall, i, j)

                if self.loopCounter != 150:
                    # if there is a path make it green
                    if grid[i][j].isdigit():
                        wall = QPushButton('o')
                        wall.setProperty('class', 'spaceLooked')
                        self.gridLayout.addWidget(wall, i, j)

                else:
                    # if there isn't a path, make it red
                    if grid[i][j].isdigit():
                        wall = QPushButton('o')
                        wall.setProperty('class', 'noSolution')
                        self.gridLayout.addWidget(wall, i, j)

                if i == 1 and j == 1:
                    start = QPushButton('start')
                    start.setProperty('class', 'space')
                    self.gridLayout.addWidget(start, i, j)

                if i == self.rowLength - 2 and j == self.columnLength - 2:
                    end = QPushButton('end')
                    end.setProperty('class', 'space')
                    self.gridLayout.addWidget(end, i, j)

        return grid

    def BiDirectionalDijkstra(self, grid):
        # giving each space a number to refer back to
        grid[1][1] = 's00'
        visited = [0]
        # end node
        grid[self.rowLength - 2][self.columnLength - 2] = 'e00'
        # when the two searches reach each other
        reached = False
        # continues until the last node is not found
        # if there is no solution, the counter will reach a certain number, exit the loop
        self.loopCounter = 0
        maxLoops = (self.columnLength-4) + (self.rowLength-4)
        while not reached:
            self.loopCounter += 1
            # adding the distances of each node from the start node
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    # checking if the end node has been found
                    if grid[i][j][1:].isdigit():
                        if int(grid[i][j][1:]) in visited:
                            # first tree
                            if grid[i][j][0] == 's':
                                # checking if trees touched
                                if grid[i][j + 1][0] == 'e' and grid[i][j + 1][1:] not in visited:
                                    reached = True
                                elif grid[i][j + 1] == '  ':
                                    grid[i][j + 1] = 's' + str(int(grid[i][j][1:]) + 1)

                                # checking if trees touched
                                if grid[i + 1][j][0] == 'e' and grid[i + 1][j][1:] not in visited:
                                    reached = True
                                elif grid[i + 1][j] == '  ':
                                    grid[i + 1][j] = 's' + str(int(grid[i][j][1:]) + 1)

                                # checking if trees touched
                                if grid[i][j - 1][0] == 'e' and grid[i][j - 1][1:] not in visited:
                                    reached = True
                                elif grid[i][j - 1] == '  ':
                                    grid[i][j - 1] = 's' + str(int(grid[i][j][1:]) + 1)

                                # checking if trees touched
                                if grid[i - 1][j][0] == 'e' and grid[i - 1][j][1:] not in visited:
                                    reached = True
                                elif grid[i - 1][j] == '  ':
                                    grid[i - 1][j] = 's' + str(int(grid[i][j][1:]) + 1)

                            # second tree
                            if grid[i][j][0] == 'e':
                                # checking if trees touched
                                if grid[i][j + 1][0] == 's' and grid[i][j + 1][1:] not in visited:
                                    reached = True
                                elif grid[i][j + 1] == '  ':
                                    grid[i][j + 1] = 'e' + str(int(grid[i][j][1:]) + 1)

                                # checking if trees touched
                                if grid[i + 1][j][0] == 's' and grid[i + 1][j][1:] not in visited:
                                    reached = True
                                elif grid[i + 1][j] == '  ':
                                    grid[i + 1][j] = 'e' + str(int(grid[i][j][1:]) + 1)

                                # checking if trees touched
                                if grid[i][j - 1][0] == 's' and grid[i][j - 1][1:] not in visited:
                                    reached = True
                                if grid[i][j - 1] == '  ':
                                    grid[i][j - 1] = 'e' + str(int(grid[i][j][1:]) + 1)

                                # checking if trees touched
                                if grid[i - 1][j][0] == 's' and grid[i - 1][j][1:] not in visited:
                                    reached = True
                                elif grid[i - 1][j] == '  ':
                                    grid[i - 1][j] = 'e' + str(int(grid[i][j][1:]) + 1)

                                if grid[i][j][0] == 's' or grid[i][j][0] == 'e':
                                    border = QPushButton('o')
                                    border.setProperty('class', 'spaceLooked')
                                    self.gridLayout.addWidget(border, i, j)

            visited.append(visited[-1] + 1)

            if self.loopCounter == maxLoops:
                break

        temp = visited[-1]
        # adding the junction to the shortest path
        numberOfPaths = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j][1:].isdigit():
                    if int(grid[i][j][1:]) == temp:
                        sFound = False
                        eFound = False
                        if numberOfPaths < 1:
                            if grid[i][j + 1][0] == 'e' and grid[i][j + 1][1:].isdigit():
                                eFound = True
                            elif grid[i][j + 1][0] == 's' and grid[i][j + 1][1:].isdigit():
                                sFound = True

                            if grid[i + 1][j][0] == 'e' and grid[i + 1][j][1:].isdigit():
                                eFound = True
                            elif grid[i + 1][j][0] == 's' and grid[i + 1][j][1:].isdigit():
                                sFound = True

                            if grid[i][j - 1][0] == 'e' and grid[i][j - 1][1:].isdigit():
                                eFound = True
                            elif grid[i][j - 1][0] == 's' and grid[i][j - 1][1:].isdigit():
                                sFound = True

                            if grid[i - 1][j][0] == 'e' and grid[i - 1][j][1:].isdigit():
                                eFound = True
                            elif grid[i - 1][j][0] == 's' and grid[i - 1][j][1:].isdigit():
                                sFound = True

                            if eFound is True and sFound is True:
                                grid[i][j] = '. '
                                numberOfPaths += 1

        for loop in range(0, temp):
            # adding the distances of each node from the start node
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == '. ':
                        if temp == visited[-1]:
                            count = 1
                            sRouteFound = False
                            eRouteFound = False
                            if count <= 2:
                                if grid[i][j + 1][1:].isdigit():
                                    if int(grid[i][j + 1][1:]) == temp - 1:
                                        if grid[i][j + 1][0] == 's':
                                            sRouteFound = True
                                            grid[i][j + 1] = '. '
                                            count += 1
                                        else:
                                            eRouteFound = True
                                            grid[i][j + 1] = '. '
                                            count += 1

                            if count <= 2:
                                if grid[i + 1][j][1:].isdigit():
                                    if int(grid[i + 1][j][1:]) == temp - 1:
                                        if not sRouteFound or not eRouteFound:
                                            if not sRouteFound:
                                                if grid[i + 1][j][0] == 's':
                                                    sRouteFound = True
                                                    grid[i + 1][j] = '. '
                                                    count += 1

                                            if not eRouteFound:
                                                if grid[i + 1][j][0] == 'e':
                                                    eRouteFound = True
                                                    grid[i + 1][j] = '. '
                                                    count += 1

                            if count <= 2:
                                if grid[i][j - 1][1:].isdigit():
                                    if int(grid[i][j - 1][1:]) == temp - 1:
                                        if not sRouteFound or not eRouteFound:
                                            if not sRouteFound:
                                                if grid[i][j - 1][0] == 's':
                                                    sRouteFound = True
                                                    grid[i][j - 1] = '. '
                                                    count += 1

                                            if not eRouteFound:
                                                if grid[i][j - 1][0] == 'e':
                                                    eRouteFound = True
                                                    grid[i][j - 1] = '. '
                                                    count += 1

                            if count <= 2:
                                if grid[i - 1][j][1:].isdigit():
                                    if int(grid[i - 1][j][1:]) == temp - 1:
                                        if not sRouteFound or not eRouteFound:
                                            if not sRouteFound:
                                                if grid[i - 1][j][0] == 's':
                                                    grid[i - 1][j] = '. '
                                                    count += 1

                                            if not eRouteFound:
                                                if grid[i - 1][j][0] == 'e':
                                                    grid[i - 1][j] = '. '
                                                    count += 1

                        else:
                            if grid[i][j + 1][1:].isdigit() and int(grid[i][j + 1][1:]) == temp - 1:
                                grid[i][j + 1] = '. '

                            elif grid[i + 1][j][1:].isdigit() and int(grid[i + 1][j][1:]) == temp - 1:
                                grid[i + 1][j] = '. '

                            elif grid[i][j - 1][1:].isdigit() and int(grid[i][j - 1][1:]) == temp - 1:
                                grid[i][j - 1] = '. '

                            elif grid[i - 1][j][1:].isdigit() and int(grid[i - 1][j][1:]) == temp - 1:
                                grid[i - 1][j] = '. '

            temp -= 1

        # formatting grid
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '# ':
                    border = QPushButton('  ')
                    border.setProperty('class', 'border')
                    self.gridLayout.addWidget(border, i, j)
                if grid[i][j] == '  ':
                    space = QPushButton('  ')
                    space.setProperty('class', 'space')
                    self.gridLayout.addWidget(space, i, j)

                if grid[i][j] == 'X ':
                    wall = QPushButton('  ')
                    wall.setProperty('class', 'wall')
                    self.gridLayout.addWidget(wall, i, j)

                if grid[i][j] == '. ':
                    wall = QPushButton('x')
                    wall.setProperty('class', 'spacePath')
                    self.gridLayout.addWidget(wall, i, j)

                if self.loopCounter != maxLoops:
                    if grid[i][j][0] == 'e' or grid[i][j][0] == 's':
                        wall = QPushButton('o')
                        wall.setProperty('class', 'spaceLooked')
                        self.gridLayout.addWidget(wall, i, j)

                else:
                    if grid[i][j][0] == 'e' or grid[i][j][0] == 's':
                        wall = QPushButton('o')
                        wall.setProperty('class', 'noSolution')
                        self.gridLayout.addWidget(wall, i, j)

                if i == 1 and j == 1:
                    start = QPushButton('start')
                    start.setProperty('class', 'space')
                    self.gridLayout.addWidget(start, i, j)

                if i == self.rowLength - 2 and j == self.columnLength - 2:
                    end = QPushButton('end')
                    end.setProperty('class', 'space')
                    self.gridLayout.addWidget(end, i, j)

        return grid

    def Greedy(self, grid):
        endCord = [self.rowLength - 2, self.columnLength - 2]

        def heuristic(i, j):
            verticalDistance = endCord[0] - i
            horizontalDistance = endCord[1] - j
            heuristic = verticalDistance + horizontalDistance
            return heuristic

        shortestDistance = heuristic(1, 1)
        grid[1][1] = str(shortestDistance)
        nodeFound = False
        # finding the initial distance
        self.loopCounter = 0
        maxLoops = int((self.rowLength*self.columnLength)*1.5)
        while not nodeFound:
            self.loopCounter += 1
            deadEnd = True
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j].isdigit():
                        if grid[i][j + 1] == '  ':
                            if heuristic(i, j + 1) < shortestDistance:
                                shortestDistance = heuristic(i, j + 1)
                                if shortestDistance < 10:
                                    grid[i][j + 1] = '0' + str(heuristic(i, j + 1))
                                    deadEnd = False
                                else:
                                    grid[i][j + 1] = str(heuristic(i, j + 1))
                                    deadEnd = False

                        elif grid[i + 1][j] == '  ':
                            if heuristic(i + 1, j) < shortestDistance:
                                shortestDistance = heuristic(i + 1, j)
                                if shortestDistance < 10:
                                    grid[i + 1][j] = '0' + str(heuristic(i + 1, j))
                                    deadEnd = False
                                else:
                                    grid[i + 1][j] = str(heuristic(i + 1, j))
                                    deadEnd = False

                        elif grid[i][j - 1] == '  ':
                            if heuristic(i, j - 1) < shortestDistance:
                                shortestDistance = heuristic(i, j - 1)
                                if shortestDistance < 10:
                                    grid[i][j - 1] = '0' + str(heuristic(i, j - 1))
                                    deadEnd = False
                                else:
                                    grid[i][j - 1] = str(heuristic(i, j - 1))
                                    deadEnd = False

                        elif grid[i - 1][j] == '  ':
                            if heuristic(i - 1, j) < shortestDistance:
                                shortestDistance = heuristic(i - 1, j)
                                if shortestDistance < 10:
                                    grid[i - 1][j] = '0' + str(heuristic(i - 1, j))
                                    deadEnd = False
                                else:
                                    grid[i - 1][j] = str(heuristic(i - 1, j))
                                    deadEnd = False

                    if grid[self.rowLength-2][self.columnLength-2].isdigit():
                        nodeFound = True

            if deadEnd:
                shortestDistance += 1

            if self.loopCounter == maxLoops:
                break

        grid[1][1] = 'n00'
        # drawing the shortest path
        for loop in range(self.rowLength + self.columnLength):
            for i in range(0, len(grid)):
                for j in range(0, len(grid[i])):
                    if grid[i][j][0] == 'n':
                        if grid[i][j + 1].isdigit():
                            grid[i][j + 1] = 'n' + str(int(grid[i][j][1:]) + 1)

                        if grid[i + 1][j].isdigit():
                            grid[i + 1][j] = 'n' + str(int(grid[i][j][1:]) + 1)

                        if grid[i][j - 1].isdigit():
                            grid[i][j - 1] = 'n' + str(int(grid[i][j][1:]) + 1)

                        if grid[i - 1][j].isdigit():
                            grid[i - 1][j] = 'n' + str(int(grid[i][j][1:]) + 1)

        if self.loopCounter != maxLoops:
            temp = int(grid[self.rowLength-2][self.columnLength-2][1:])
            grid[self.rowLength-2][self.columnLength-2] = '. '
            while grid[1][1] != '. ':
                for i in range(0, len(grid)):
                    for j in range(0, len(grid[i])):
                        if grid[i][j] == '. ':
                            if grid[i][j + 1][1:].isdigit() and int(grid[i][j + 1][1:]) == temp - 1:
                                grid[i][j + 1] = '. '

                            elif grid[i + 1][j][1:].isdigit() and int(grid[i + 1][j][1:]) == temp - 1:
                                grid[i + 1][j] = '. '

                            elif grid[i][j - 1][1:].isdigit() and int(grid[i][j - 1][1:]) == temp - 1:
                                grid[i][j - 1] = '. '

                            elif grid[i - 1][j][1:].isdigit() and int(grid[i - 1][j][1:]) == temp - 1:
                                grid[i - 1][j] = '. '

                temp -= 1

        # formatting grid
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '# ':
                    border = QPushButton('  ')
                    border.setProperty('class', 'border')
                    self.gridLayout.addWidget(border, i, j)
                if grid[i][j] == '  ':
                    space = QPushButton('  ')
                    space.setProperty('class', 'space')
                    self.gridLayout.addWidget(space, i, j)

                if grid[i][j] == 'X ':
                    wall = QPushButton('  ')
                    wall.setProperty('class', 'wall')
                    self.gridLayout.addWidget(wall, i, j)

                if grid[i][j] == '. ':
                    wall = QPushButton('x')
                    wall.setProperty('class', 'spacePath')
                    self.gridLayout.addWidget(wall, i, j)

                if self.loopCounter != maxLoops:
                    if grid[i][j][0] == 'n':
                        wall = QPushButton('o')
                        wall.setProperty('class', 'spaceLooked')
                        self.gridLayout.addWidget(wall, i, j)

                else:
                    if grid[i][j][0] == 'n':
                        wall = QPushButton('o')
                        wall.setProperty('class', 'noSolution')
                        self.gridLayout.addWidget(wall, i, j)

                if i == 1 and j == 1:
                    start = QPushButton('start')
                    start.setProperty('class', 'space')
                    self.gridLayout.addWidget(start, i, j)

                if i == self.rowLength - 2 and j == self.columnLength - 2:
                    end = QPushButton('end')
                    end.setProperty('class', 'space')
                    self.gridLayout.addWidget(end, i, j)

        return grid


app = QApplication(sys.argv)
menu = Menu()

app.setStyleSheet('''
    QWidget {
        background-color: "#8CC084";
    }

    .Title {
        font-size: 50px;
        font-weight: bold;
        color: '#E8E5DA';
    }

    .menubutton {
        font-size: 40px;
        font-weight: bold;
        color: '#968E85';
        background-color: '#C1D7AE';
        border-radius: 8px;
        border: 4px solid '#5CA253';
    }
    
    .menubutton:hover {
        background-color: '#8CC084';
    }
   
    .mainProgram {
        background-color: '#8CC084';
    }   
    
    .mainTitle {
        font-size: 40px;
        font-weight: bold;
        color: '#726b62';
        background-color: rgba(0,0,0,0%);
    }
    
    .tutorialButton:hover {
        background-color: '#304C89';
    }
       
    .tutorialText {
        font-size: 30px;
        font-weight: bold;
        color: '#968E85';
        background-color: '#C1D7AE';
        border-radius: 8px;
        border: 4px solid '#5CA253';
    }
    
    .tutorialButton {
        font-size: 40px;
        font-weight: bold;
        color: '#968E85';
        background-color: '#C1D7AE';
        border-radius: 8px;
        border: 4px solid '#5CA253';
    }
    
    .tutorialButton:hover {
        background-color: '#8CC084';
    }
    
    .skipButton {
        font-size: 40px;
        font-weight: bold;
        color: '#968E85';
        background-color: '#C1D7AE';
        border-radius: 8px;
        border: 4px solid '#5CA253';
        width: 110%;
    }
    
    .skipButton:hover {
        background-color: '#8CC084';
    }
    
    .mazeAndAlgorithmButton {
        font-size: 30px;
        font-weight: bold;
        color: '#968E85';
        background-color: '#C1D7AE';
        border-radius: 8px;
        border: 4px solid '#5CA253';
    }
    
    .mazeAndAlgorithmButton:hover {
        background-color: '#8CC084';
    }
    
    .InfoText {
        font-size: 20px;
        font-weight: bold;
        color: '#968E85';
        background-color: '#C1D7AE';
        border-radius: 8px;
        border: 4px solid '#5CA253';
    }
    
    .border {
        background-color: '#AAA49D';
        color: '#AAA49D';
        font-size: 20px;
        font-weight: bold;
        padding: 19px 10px;
        border-radius: 5px;
        border: 3px solid '#8D857C';
 
    }
    
    .wall {
        background-color: '#DFC57C';
        font-size: 20px;
        padding: 19px 10px;
        border-radius: 5px;
        border: 3px solid '#D3AF4A';
    }
    
    .wall:hover {
        background-color: '#DBBD6B';
    }
    
    .space {
        background-color: '#EFE3BD';
        font-size: 20px;
        color: '#000000';
        font-weight: bold;
        padding: 19px 10px;
        border-radius: 5px;
        border: 3px solid '#E7D69C';
    }
    
    .spacePath {
        background-color: '#EFE3BD';
        font-size: 20px;
        color: '#3e704f';
        font-weight: bold;
        padding: 19px 10px;
        border-radius: 5px;
        border: 3px solid '#E7D69C';
    }
    
    .spaceLooked {
        background-color: '#EFE3BD';
        font-size: 20px;
        color: '#56AE57';
        padding: 19px 10px;
        border-radius: 5px;
        border: 3px solid '#E7D69C';
    }
    
    .noSolution {
        background-color: '#EFE3BD';
        font-size: 20px;
        font-weight: bold;
        color: '#ff6961';
        padding: 19px 10px;
        border-radius: 5px;
        border: 3px solid '#E7D69C';
    }
    
    .space:hover {
        background-color: '#F3EACE';
    }
    
    .spacePath:hover {
        background-color: '#F3EACE';
    }
    
    .spaceLooked:hover {
        background-color: '#F3EACE';
    }
    
    .noSolution:hover {
        background-color: '#F3EACE';
    }
   
''')

menu.showMaximized()
sys.exit(app.exec())
