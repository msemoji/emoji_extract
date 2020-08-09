# emoji_extract
This repo contains Python 3 code to extract emojis from text, show emojis as a list and unique emoji list, and generate list of most used emojis with counts of use (e.g. rows or users). This also include demo code as .py and .ipynb.

<p> This code can handles the latest emojis including keycaps, flags, families, "compound" emojis with components and modifiers just fine. 

<p>The extractEmojis.py is the code to process the emojis in data. It uses the ast, re, and regex libraries. May need to pip install those three if you don't have them. This code also uses the Unicode v13 January 2020 emoji lists provided here in the Unicode_emojis_list.py which is loaded automatically by extractEmojis.py. This list of emojis was compiled from Unicode:  https://unicode.org/Public/emoji/13.0/emoji-test.txt 

<p>To use the code, examples are provided in Demo_Extract_Emojis_from_Text.
<br>
Example code snippet:<br>
import extractEmojis<br>
some_text = "Some emoji 👨🏾‍👩🏾‍👧🏾‍👦🏾 🗳❤️🇦🇺😃🌹 smiles🌹4️⃣🍎🇦 👪🏿 👩🏿‍💻 🗳🗳️"<br>
emojis_list = extractEmojis.getEmojisFromText(some_text)<br>
unique_emojis = extractEmojis.getUniqueEmojisFromEmojiList(emojis_list)<br>
<br>
list of unique emojis result is ['4️⃣', '❤️', '🇦', '🇦🇺', '🌹', '🍎', '👨🏾\u200d👩🏾\u200d👧🏾\u200d👦🏾', '👩🏿\u200d💻', '👪🏿', '🗳️', '😃']<br>
<br>
<br>
list of top 5 most used emojis in sample dataset as list of tuples with emoji and count of users or rows that used it is:<br>
[('❤️', 5), ('🔵', 5), ('💥', 4), ('🤣', 4), ('🇺🇸', 3)]
<br>
<p> There may be differences with the way your device or web browser displays the emojis even when it is the correct Unicode emoji. Don't worry about it, it just is the way it is. When in doubt, you can alway refer to Unicode emoji charts https://unicode.org/emoji/charts/full-emoji-list.html or https://emojipedia.org/ to verify an emoji rendering and support for your device.

<p> Sample output as produced from the demo code and sample data provided showing the sample data text, emoji list, and unique emojis generated with this code.
 
![screenshot of demo](/demo_extract_emojis.png)


