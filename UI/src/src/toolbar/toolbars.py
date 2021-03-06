"""This module handles all the toolbars of the UI."""
from PyQt5 import QtCore, QtGui, QtWidgets

class ToolBarTop(QtWidgets.QToolBar):
    """This class inherits from a QToolBar.
       It contains all components for the toolbar at the top of the screen."""

    def __init__(self, height):
        super().__init__()
              
        self.setFixedHeight(int(height * 0.075))
        self.setMovable(False)
        self.button_list = []
        
        self.create_font(height)
        self.create_page_buttons()
        self.create_help_button()
        self.create_screen_button()
        self.add_buttons()

    def create_font(self, height):
        """Creates the font used in the toolbar."""
        self.toolbar_font = QtGui.QFont()
        self.toolbar_font.setFamily("Segoe UI")
        self.toolbar_font.setPixelSize(int(0.035 * height))
        self.toolbar_font.setBold(True)

    def create_page_buttons(self):
        """Creates the different buttons used in the toolbar for moving to different pages."""
        self.map_button = QtWidgets.QAction('Map')
        self.map_button.setFont(self.toolbar_font)
        self.button_list.append(self.map_button)

        self.graphs_button = QtWidgets.QAction('Grafieken')
        self.graphs_button.setFont(self.toolbar_font)
        self.button_list.append(self.graphs_button)

        self.scenario_button = QtWidgets.QAction("Scenario's")
        self.scenario_button.setFont(self.toolbar_font)
        self.button_list.append(self.scenario_button)

        self.manual_control_button = QtWidgets.QAction("Handmatige Besturing")
        self.manual_control_button.setFont(self.toolbar_font)
        self.button_list.append(self.manual_control_button)

        self.figure_button = QtWidgets.QAction("Cijfers")
        self.figure_button.setFont(self.toolbar_font)
        self.button_list.append(self.figure_button)
    
    def create_help_button(self):
        """Creates the help button for the toolbar."""
        self.help_button = QtWidgets.QAction('Hulp')
        self.help_button.setFont(self.toolbar_font)
        self.button_list.append(self.help_button)
    
    def create_screen_button(self):
        """Creates the button to go to the second screen page."""
        self.screen_button = QtWidgets.QAction('Tweede Scherm')
        self.screen_button.setFont(self.toolbar_font)
        self.button_list.append(self.screen_button)
    
    def create_spacer(self):
        """Create two expending widgets (for left and right) 
           to center the buttons on the toolbar."""
        self.spacer_left = QtWidgets.QWidget(self)
        self.spacer_left.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                       QtWidgets.QSizePolicy.Fixed)

        self.spacer_right = QtWidgets.QWidget(self)
        self.spacer_right.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                        QtWidgets.QSizePolicy.Fixed)

    
    def add_buttons(self):
        """Add all buttons and spacers to the toolbar."""
        for i in range(len(self.button_list)):
            spacer = QtWidgets.QWidget(self)
            spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            self.addWidget(spacer)
            self.addAction(self.button_list[i])
        
        spacer = QtWidgets.QWidget(self)
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.addWidget(spacer)

class ToolBarBottom(QtWidgets.QToolBar):
    """This class inherits from a QToolBar.
       It contains all components for the toolbar at the bottom of the screen."""

    def __init__(self, width, height, data):
        super().__init__()
        
        self.setFixedHeight(int(0.075*height))
        self.setMovable(False)
        self.data = data
        
        self.create_font(height)
        self.create_labels(width)
        self.create_exit_button()

    def create_font(self, height):
        """Create a font to use for the text."""
        self.toolbar_font = QtGui.QFont()
        self.toolbar_font.setFamily("Segoe UI")
        self.toolbar_font.setPixelSize(int(0.035 * height))
        self.toolbar_font.setBold(True)
    
    def create_labels(self, width):
        """Create a QLabel to display the current settings."""
        self.mode_title_label = QtWidgets.QLabel(self)
        self.mode_title_label.setFixedWidth(int(width * 0.10))
        self.mode_title_label.setFixedHeight(self.height())
        self.mode_title_label.setText("Modus: ")
        self.mode_title_label.setFont(self.toolbar_font)
        self.mode_title_label.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.addWidget(self.mode_title_label)

        self.mode_label = QtWidgets.QLabel(self)
        self.mode_label.setFixedWidth(int(width* 0.50))
        self.mode_label.setFixedHeight(self.height())
        self.mode_label.setText("Gestopt")
        self.mode_label.setFont(self.toolbar_font)
        self.addWidget(self.mode_label)

        if self.data.CONNECTED:
            text = 'Ja'
        else:
            text = 'Nee'
        self.connection_label = QtWidgets.QLabel(self)
        self.connection_label.setFixedWidth(int(width * 0.30))
        self.connection_label.setFixedHeight(self.height())
        self.connection_label.setText(f"PI verbonden: {text}")
        self.connection_label.setFont(self.toolbar_font)
        self.addWidget(self.connection_label)
    
    def update_text(self):
        """Update the toolbar to display the current settings."""
        mode, details = self.data.get_mode()

        if mode == 'manual':
            self.mode_label.setText(f"{mode.capitalize()} (Zon: {details[0]}%, "
                                    f"Wind: {details[1]}%, Vraag: {details[2]}%)")
        elif mode == 'scenario':
            self.mode_label.setText(f"{mode.capitalize()} ({details})")
        elif mode == 'stop':
            self.mode_label.setText("Gestopt")
        else:
            self.mode_label.setText("Onbekend")
    
    def create_exit_button(self):
        """Creates the button to go exit the application."""
        self.exit_button = QtWidgets.QAction('Exit')
        self.exit_button.setFont(self.toolbar_font)
        self.addAction(self.exit_button)
