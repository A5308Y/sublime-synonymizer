import sublime
import sublime_plugin
import json
import urllib

class SynonymSelectionInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self, view):
        self.view = view

    def name(self):
        return 'name'

    def itemToWord(self, synonym):
        return synonym['word']

    def list_items(self):
        wordRegion = self.view.sel()[0]
        word = self.view.substr(wordRegion)
        response = urllib.request.urlopen('https://api.datamuse.com/words?ml=' + word)
        content = response.read()
        items = list(map(self.itemToWord, json.loads(content.decode('utf-8'))))
        return items


class SynonymizerCommand(sublime_plugin.TextCommand):
  def run(self, edit, name):
    wordRegion = self.view.sel()[0]
    self.view.replace(edit, wordRegion, name)

  def input(self, args):
      print(args)
      if 'name' not in args:
          return SynonymSelectionInputHandler(self.view)
      return None


# TODOs: Threading, context information, error handling, use python-datamuse API?
