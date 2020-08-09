# emoji_extract
This repo contains Python code to extract emojis from text and show the emojis as a list and unique emoji list. It also includes examples of how to get the most used emoji in a dataset across rows or users.

<p>The extractEmojis.py is the code to process the emojis in data. It uses the re and regex libraries. May need to pip install re if you don't have it. This code also uses the Unicode v13 January 2020 emoji lists provided here in the Unicode_emojis_list.py which is loaded automatically by extractEmojis.py. This list of emojis was compiled from Unicode:  https://unicode.org/Public/emoji/13.0/emoji-test.txt 

<p> This code can handle keycaps, flags, families, compound emojis, and modifiers just fine. 

<p>To use the code, examples are provided in Demo_Extract_Emojis_from_Text.
<br>
Example code snippet:<br>
import extractEmojis<br>
some_text = "Some emoji 👨🏾‍👩🏾‍👧🏾‍👦🏾 🗳❤️🇦🇺😃🌹 smiles🌹4️⃣🍎🇦 👪🏿 👩🏿‍💻 🗳🗳️"<br>
emojis_list = extractEmojis.getEmojisFromText(some_text)<br>
unique_emojis = extractEmojis.getUniqueEmojisFromEmojiList(emojis_list)<br>
<br>
list of unique emojis result is ['4️⃣', '❤️', '🇦', '🇦🇺', '🌹', '🍎', '👨🏾\u200d👩🏾\u200d👧🏾\u200d👦🏾', '👩🏿\u200d💻', '👪🏿', '🗳️', '😃']<br>

<p> There may be differences with the way your device or web browser displays the emojis even when it is the correct Unicode emoji. Don't worry about it, it just is the way it is. When in doubt, you can alway refer to Unicode emoji charts or emojipedia.org to verify an emoji rendering and support for your device.

<p> The demo code demonstrates how to process emojis in rows of data using pandas.Below is a screenshot showing the sample data text, emoji list, and unique emojis generated with this code.
 
![screenshot of demo](/demo_extract_emojis.png)


