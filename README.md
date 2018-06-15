# grab_wechatInfo
This script uses itchat module to achieve four basic functions: 

# Run send message. 
```python
python grab_wechat.py send
```
Inputted the remark name and the message, the function will send it to that person. If the input is "" or the it equals to the user's name, the function will send the message to the user. Later, send image/file will be added to this script.

# Run collect gender info. 
```python
python grab_wechat.py gender
```
The function collects the number of male, female, and other (unspecified) and compute the proportion of each gender. It renders a html file to visualize gender distribution.

# Run collect geographical distribution of your wechat friends. (China only)
```python
python grab_wechat.py cmap
```
This function returns a html file of the geographical distribution of your friends on the map of China.

# Run collect "what's up" info from all of your friends. 
```python
python grab_wechat.py signature
```
It returns the 30 most frequent words (to simplify and avoid function words, I only collect nouns, adjectives for Chinese and nouns, verbs, and adverbs for English) from Chinese and English. Though people sometimes use emoji or other languages in their "What's up" like Korean, French, etc., I narrows the language down to Chinese and English in order to decrease the difficulty of pos tagging. The function uses THULAC http://thulac.thunlp.org/ to split Chinese sentences and tag Chinese words. For English, I use NLTK to do tokenize and pos tagging.

