"""
Main part implementation
"""
from src.gui import Application

if __name__ == '__main__':
    app = Application()
    app.change_resolution(1280,1024)
    app.run()
