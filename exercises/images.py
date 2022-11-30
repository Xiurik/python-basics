import os
import sys

from PIL import Image

'''
#? Open an image, conver to a thumbnail and save it.

astro = Image.open('exercises/pokemons/astro.jpg')
astro.thumbnail((400,400))
astro.save('exercises/pokemons/mini-astro.jpg')
'''

#* Grab first and second arguments
args = sys.argv
currentFolder = ''
outputFolder = ''

if len(args) > 1:
  currentFolder = f'exercises/{args[1]}'
  outputFolder = f'exercises/{args[2]}'
elif len(args) < 1:
  print('Missing arguments')
  
#* Check if output folder exist, if not, create
if not os.path.exists(outputFolder):
  os.makedirs(outputFolder)

#* loop through pokemons folder and conver to PNG, then save it to output folder
for fn in os.listdir(currentFolder):
  if fn.startswith('astro'):
    continue
  
  file, ext = os.path.splitext(fn)
  nf = f'{outputFolder}{file}.png'
  
  if os.path.exists(nf) is True:
    print('File already exists')
    continue
  
  try:
    with Image.open(f'{currentFolder}{fn}') as im:
      im.save(nf, 'png')
  except OSError as ose:
    print(ose)