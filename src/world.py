import events
import stocks
import Player

class World:
    def __init__(self,events,stocks,player):
        self.events = events.Events()
        self.stocks = stocks.Stock()
        self.player = player.Player()
    def run(self):
        self.events.run()
        self.stocks.run()
        self.player.run()
    def stop(self):
        self.events.stop()
        self.stocks.stop()
        self.player.stop()
    def pause(self):
        self.events.pause()
        self.stocks.pause()
        self.player.pause()
    def resume(self):
        self.events.resume()
        self.stocks.resume()
        self.player.resume()
    def restart(self):
        self.events.restart()
        self.stocks.restart()
        self.player.restart()
    def save(self):
        self.events.save()
        self.stocks.save()
        self.player.save()
    def load(self):
        self.events.load()
        self.stocks.load()
        self.player.load()
    def quit(self):
        self.events.quit()
        self.stocks.quit()
        self.player.quit()
    def exit(self):
        self.events.exit()
        self.stocks.exit()
        self.player.exit()
    def help(self):
        self.events.help()
        self.stocks.help()
        self.player.help()
    