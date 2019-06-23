import sublime
import sublime_plugin
import json
from urllib.request import urlopen
from urllib.error import URLError

class SynonymSelectionInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self, view):
        self.view = view

    def selected_word(self):
        return 'selected_word'

    def list_items(self):
        word_region = self.view.sel()[0]
        word = self.view.substr(word_region)
        datamuse_result = DataMuseApiCall().run(word)
        if not datamuse_result:
          sublime.status_message('API could not find any synonyms for the selected string. Please try something else.')
        else:
          return datamuse_result


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
    sublime.status_message('Requesting data from datamuse API')
    result = self.datamuse_result(word)
    sublime.status_message('Successfully read from datamuse API')

    return list(map(self.item_to_word, result))

  def datamuse_result(self, word):
      try:
        response = urlopen('https://api.datamuse.com/words?ml=' + word)
      except TypeError as err:
          return sublime.status_message(str(err))
      except URLError as err:
          return sublime.status_message('Error connecting to datamuse API')

      result = json.loads(response.read().decode('utf-8'))

      return(result)


  def item_to_word(self, synonym):
      return synonym['word']
