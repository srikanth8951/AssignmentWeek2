# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:38:11 2020

@author: hvsri
"""

def get_matrix(text, c=1, r=1):
    if c * r >= len(text):
        return (c, r)

    if not (c >= r and c - r < 1):
        r += 1
    else:
        c += 1
    return get_matrix(text, c, r)
    

def encode(plain_text):
    normalized_text = ''.join(c.lower() for c in plain_text if c.isalnum())
    
    if not normalized_text:
        return ''

    columns, rows = get_matrix(normalized_text)
    
    chunks = [normalized_text[i * columns: i * columns + rows + 1] for i in range(0, rows + 1)]

    partials = [[] for _ in range(rows + 1)]
    
    for chunk in chunks:
        for i in range(columns):
            if i < len(chunk):
                partials[i].append(chunk[i])
    
    final = [''.join(p) for p in partials if p]
    
    result = ' '.join(final)
    
    expected_length = (columns * rows) + (rows - 1)
    if len(result) < expected_length: 
        result += ' ' * (expected_length - len(result))
    return result

plain_text = input('Enter the text: ')

print(encode(plain_text))