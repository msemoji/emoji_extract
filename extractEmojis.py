#!/usr/bin/env python

# Extract list of emojis and unique emojis from content
# This Python 3 code is from August 2020 by mswartz2@gmu.edu

# dependencies
import re # if re not on system do pip install re
import regex
import ast

# part of this repo
import Unicode_emojis_list as emojis


"""
Code examples

#list of all from Unicode which includes some variants of renderings of same emoji
# list_of_all_v13_emojis = emojis.list_of_all_emojis


# sample text to test
some_text_string_maybe_with_emojis = "RT @atmention: 12 ** 👨🏾‍👩🏾‍👧🏾‍👦🏾 🗳❤️🇦🇺😃🟠 smiles🟠4️⃣🍎🇦 👪🏿 👩🏿‍💻 🗳🗳️"


# Get list of emojis in order of appearance in text
list_of_emojis_in_text = getEmojisFromText(some_text_string_maybe_with_emojis)

# Get list of unique emojis in the emoji list, sorted
list_of_unique_emojis_in_text = getUniqueEmojisFromEmojiList(list_of_emojis_in_text)

"""
 
# CODE TO GET EMOJIS FROM TEXT

# compile emojis from the list of emojis into one massive string for regex to find exact emoji matches

all_emojis_str=''
for emoji in emojis.list_of_all_emojis:
    all_emojis_str += emoji
all_emojis_pattern = re.compile('['+all_emojis_str+']')

list_of_Unicode_emojis = emojis.list_of_emojis



# function to get list of emojis from text with fix for numbers from keycaps
# it's kind of slow but effective
def getEmojisFromText(string_of_text):
    try:  
        sequences_list = regex.findall(r'\X', string_of_text) # break into sequences
        emoji_list_w_numbers =list(filter(all_emojis_pattern.match, sequences_list)) # get emojis plus any numbers
        # fix any numbers that are actually emoji keycaps in the text
        exclude_numbers =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "*", "#"]
        temp_emoji_list = []
        for seq in emoji_list_w_numbers:
            if seq not in exclude_numbers:
                temp_emoji_list.append(seq)
        # make sure emojis are Unicode emojis
        emojis_to_fix = set(temp_emoji_list).difference(set(temp_emoji_list).intersection(emojis.list_of_emojis))
        emoji_list = []
        for e in temp_emoji_list:
            if e not in emojis_to_fix:
                emoji_list.append(e)
            else:
                emoji_list.append(fixDuplicateEmoji(e))
    except:
        emoji_list = []
    return emoji_list
    
# function to get sorted list of unique emojis from list of emojis
def getUniqueEmojisFromEmojiList(emoji_list):    
    if type(emoji_list)==list:
        return sorted(list(set(emoji_list)))
    else:
        try:
            return sorted(list(set(ast.literal_eval(emoji_list))))
        except:
            return []
    
# get new text that has repaired unqualified emojis in text
def repairEmojisInText(string_of_text):
    if type(string_of_text)!=str:
        string_of_text = str(string_of_text)
    try:
        sequences_list = regex.findall(r'\X', string_of_text) # break into sequences
        emoji_list_w_numbers =list(filter(all_emojis_pattern.match, sequences_list)) # get emojis plus any numbers
        # fix any numbers that are actually emoji keycaps in the text
        exclude_numbers =  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', "*", "#"]
        emojis_found = []
        for seq in emoji_list_w_numbers:
            if seq not in exclude_numbers:
                emojis_found.append(seq)
        fixed_sequence_list = []
        emoji_list = []
        fixed_text = ''
        for seq in sequences_list:
            if seq in emojis_found:
                fixed_emoji = fixDuplicateEmoji(seq)
                fixed_sequence_list.append(fixed_emoji)
                emoji_list.append(fixed_emoji)
            else:
                fixed_sequence_list.append(seq)
        
        fixed_text = ''.join(fixed_sequence_list)
        return fixed_text
    except:
        return ''
        
        
# function to get a list of emojis with counts
def getUniqueEmojiWithCounts(list_of_lists_of_unique_emojis):
    long_list_of_emojis_used = []
    for sublist in list_of_lists_of_unique_emojis:
        long_list_of_emojis_used += sublist
    # unique emojis used
    unique_emojis_used_in_dataset = sorted(list(set(long_list_of_emojis_used)))
    # count of rows with that emoji
    list_with_tuples_of_emojis_with_count_of_rows = []
    for emoji in unique_emojis_used_in_dataset:
        list_with_tuples_of_emojis_with_count_of_rows.append((emoji, long_list_of_emojis_used.count(emoji)))
    # sort the list of tuples in descending order
    most_used_emojis_with_cnt_rows = sorted(list_with_tuples_of_emojis_with_count_of_rows, key = lambda x: x[1], reverse=True)
    return most_used_emojis_with_cnt_rows
    


# HELPER FUNCTION BELOW    
# helper functions below to fix appearance of duplicate emojis used in getEmojisFromText
# globals
keycap = b'\\u20e3'.decode('unicode_escape')
emoji_variation_selector = b'\\ufe0f'.decode('unicode_escape')
text_variation_selector = b'\\ufe0e'.decode('unicode_escape')
joiner = b'\\u200d'.decode('unicode_escape') # zero-width-joiner
cancel_tag= b'\\U000e007f'.decode('unicode_escape')

emoji_parts = [joiner, emoji_variation_selector, text_variation_selector,cancel_tag]

## MODIFIERS
# skin tones
light =  b'\\U0001f3fb'.decode('unicode_escape')
medium_light =  b'\\U0001f3fc'.decode('unicode_escape')
medium =  b'\\U0001f3fd'.decode('unicode_escape')
med_dark =  b'\\U0001f3fe'.decode('unicode_escape')
dark =  b'\\U0001f3ff'.decode('unicode_escape')
skintones = [light,medium_light,medium,med_dark,dark]

# genders
female =  b'\\u2640'.decode('unicode_escape')
male = b'\\u2642'.decode('unicode_escape')
transgender = b'\\u26a7'.decode('unicode_escape')
genders = [female,male,transgender]


emoji_modifiers = skintones + genders



def fixDuplicateEmoji(emoji):
    if type(emoji)!=str or emoji==None or emoji == '':
        return ''
    
    if type(emoji)==str:
        
        # check emoji
        fully_qualified_emoji_list_plus_fixes = []
        emoji_fix_status_list = []
        e = emoji.strip()
        # check if fully qualified
        if e in list_of_Unicode_emojis: #emoji_qualified_list:
            #print('fully qualified')
            fully_qualified_emoji_list_plus_fixes.append(e)
            emoji_fix_status_list.append('fully_qualified')
       # try to fix it
        else: 
            # try 1: add emoji variation
            fix1 = e + emoji_variation_selector # add emoji variation
            if fix1 in list_of_Unicode_emojis:#emoji_qualified_list:
                #print('fix1 worked')
                fully_qualified_emoji_list_plus_fixes.append(fix1)
                emoji_fix_status_list.append('fix1')
            else: # try 2: remove emoji variation
                fix2 = e.replace(emoji_variation_selector,'')
                if fix2 in list_of_Unicode_emojis:#emoji_qualified_list:
                    #print('fix2 worked')
                    fully_qualified_emoji_list_plus_fixes.append(fix2)
                    emoji_fix_status_list.append('fix2')
                else: # try 3: replace text variation with emoji variation
                    fix3 = e.replace(text_variation_selector,emoji_variation_selector)
                    if fix3 in list_of_Unicode_emojis:#emoji_qualified_list:
                        #print('fix3 worked')
                        fully_qualified_emoji_list_plus_fixes.append(fix3)
                        emoji_fix_status_list.append('fix3')
                    else: # try 4: insert emoji variation
                        fix4 = e.replace(keycap, emoji_variation_selector+keycap)
                        if fix4 in list_of_Unicode_emojis:#emoji_qualified_list:
                            #print('fix4 worked')
                            fully_qualified_emoji_list_plus_fixes.append(fix4)
                            emoji_fix_status_list.append('fix4')
                        else: # try 5: fix joiner and add variation selector
                            fix5 = e.replace(joiner,emoji_variation_selector+joiner)+emoji_variation_selector
                            if fix5 in list_of_Unicode_emojis:#emoji_qualified_list:
                                #print('fix5 worked')
                                fully_qualified_emoji_list_plus_fixes.append(fix5)
                                emoji_fix_status_list.append('fix5')
                            else: # try 6: add the cancel tag    
                                fix6 = e + cancel_tag
                                if fix6 in list_of_Unicode_emojis:#emoji_qualified_list:
                                    #print('fix6 worked')
                                    fully_qualified_emoji_list_plus_fixes.append(fix6)
                                    emoji_fix_status_list.append('fix6')
                                else: # check for dupes of parts
                                    dupes_type_list = []
                                    for i in range(len(emoji_parts)):
                                        cnt_dupe_check = e.count(emoji_parts[i])
                                        if cnt_dupe_check > 1:
                                            dupes_type_list.append(i)
                                    if len(dupes_type_list)>0:
                                        fix_check_continue = True
                                        for val in dupes_type_list:
                                            if fix_check_continue == True:
                                                fix7 = e.replace(emoji_parts[val],'',1)# replace first dupe
                                                if fix7 in list_of_Unicode_emojis:
                                                    #print('fix7 worked')
                                                    fully_qualified_emoji_list_plus_fixes.append(fix7)
                                                    emoji_fix_status_list.append('fix7')
                                                    fix_check_continue = False
                                        if fix_check_continue == True: # dupes but not sure how to fix
                                            #print('other')
                                            fully_qualified_emoji_list_plus_fixes.append(e)
                                            emoji_fix_status_list.append('no_fix')
                                                
                                    elif joiner in e:
                                        fix8 = e.replace(joiner,'') # some may have an extra joiner
                                        if fix8 in list_of_Unicode_emojis:
                                            #print('fix8 worked')
                                            fully_qualified_emoji_list_plus_fixes.append(fix8)
                                            emoji_fix_status_list.append('fix8')
                                        
                                        else: # if the order is mixed up
                                            new_emoji = emoji
                                            if type(emoji)==str:
                                                if emoji not in list_of_Unicode_emojis:
                                                    # try to rearrange codepoints to correct order
                                                    skin_found = [skintone for skintone in skintones if skintone in emoji]
                                                    gender_found = [gender for gender in genders if gender in emoji]
                                                    base = [piece for piece in emoji if piece not in emoji_parts and piece not in emoji_modifiers]
                                                    new_emoji = ''
                                                    if len(base)==1:
                                                        new_emoji=base[0]
                                                        if len(skin_found) == 1:
                                                            new_emoji+=skin_found[0]
                                                            if len(gender_found)==1:
                                                                new_emoji+=joiner
                                                                new_emoji+=gender_found[0]
                                                    if new_emoji in list_of_Unicode_emojis:
                                                        fix9 = new_emoji
                                                    else:
                                                        new_emoji+=emoji_variation_selector 
                                                        if new_emoji in list_of_Unicode_emojis:
                                                            fix9 = new_emoji

                                            if fix9 in list_of_Unicode_emojis:
                                                #print('fix9 worked')
                                                fully_qualified_emoji_list_plus_fixes.append(fix9)
                                                emoji_fix_status_list.append('fix9')
                                            else: # not sure what else to try so just keep it (probably a letter)
                                                #print('other') # no fix
                                                fully_qualified_emoji_list_plus_fixes.append(e)
                                                #continue
                                                emoji_fix_status_list.append('no_fix')
                                    
                                    else: # not sure what else to try so just keep it (probably a letter)
                                            #print('other') # no fix
                                            fully_qualified_emoji_list_plus_fixes.append(e)
                                            #continue
                                            emoji_fix_status_list.append('no_fix')                                         
    else:
        return ''#[]#[[],[]]
    return fully_qualified_emoji_list_plus_fixes[0]#, emoji_fix_status_list[0]


