# Sublime Synonymizer

Sublime Package to find and chose synonyms for the selected word.

![demo](img/demo.gif)

## Usage

Select a single word, open the command palette and select "Synonymizer". You will be presented with
a list of possible synonyms to chose from. Select one to replace the selected word.

## TODOs

- Ensure the plugin plays nice with other plugins and sublime core (Threading)
- Use multiple selections as context information
- Investigate if using python-datamuse API is helpful here
- Error handling
- Allow to configure other synonym APIs
- Allow to configure a limit for number of returned words.

## Thanks

https://www.datamuse.com/api that does all the heavy lifting of finding synonyms.
