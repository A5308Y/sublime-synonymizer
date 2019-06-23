import sublime
import sublime_plugin
import json
import urllib

class SynonymSelectionInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self, view):
        self.view = view

    def selected_word(self):
        return 'selected_word'

    def list_items(self):
        word_region = self.view.sel()[0]
        word = self.view.substr(word_region)
        return DataMuseApiCall().run(word)


class SynonymizerCommand(sublime_plugin.TextCommand):
  def run(self, edit, selected_word):
    word_region = self.view.sel()[0]
    self.view.replace(edit, word_region, selected_word)

  def input(self, args):
      if 'selected_word' not in args:
          return SynonymSelectionInputHandler(self.view)
      return None

class DataMuseApiCall():
  def run(self, word):
      response = urllib.request.urlopen('https://api.datamuse.com/words?ml=' + word)
      content = response.read()
      return list(map(self.item_to_word, json.loads(content.decode('utf-8'))))

  def item_to_word(self, synonym):
      return synonym['word']
